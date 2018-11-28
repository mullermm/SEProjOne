import sys
import ConLib
import csv
from Major import *

transcript = []

def main():
    filename = "C:\\xampp\\htdocs\\subpages_student\\FormattedTranscript.txt"
    with open(filename, "r") as f:
        content = f.readlines()
    for line in content:
        transcript.append(line.rstrip())
    print(transcript)

    major_number = int(sys.argv[1])
    done = functions[major_number](transcript, 1)
    todo = functions[major_number](transcript, 2)

    done = list(set(done))
    todo = list(set(todo))
    
    with open(r"C:\xampp\htdocs\src\csv\courses.csv", mode='r', encoding="utf8") as f, open('done_courses.csv', mode='w') as done_courses_file, open('todo_courses.csv', mode='w') as todo_courses_file:
        done_courses_writer = csv.writer(done_courses_file, delimiter='~', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        done_courses_writer.writerow(["Course Number","Course Title","Credits","Course Description","Core Curiculum","Prerequisites"])
        todo_courses_writer = csv.writer(todo_courses_file, delimiter='~', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        todo_courses_writer.writerow(["Course Number","Course Title","Credits","Course Description","Core Curiculum","Prerequisites"])
        reader = csv.reader(f, delimiter="~")
        for i, line in enumerate(reader):
            if line[0] in done:
                done_courses_writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5]])
            if line[0] in todo:
                todo_courses_writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5]])

if __name__ == "__main__":
    main()

