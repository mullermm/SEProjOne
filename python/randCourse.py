import csv
import random

CompletedClasses = ""
ActiveClasses = ""

for x in range (0, random.randint(1,32)):
    with open("courses.csv") as f:
        reader = csv.reader(f, delimiter='~')
        chosen_row = random.choice(list(reader))
        CompletedClasses += chosen_row[0]+chosen_row[1]+' '


for x in range (0, random.randint(3,5)):
    with open("courses.csv") as f:
        reader = csv.reader(f, delimiter='~')
        chosen_row = random.choice(list(reader))
        ActiveClasses += chosen_row[0]+chosen_row[1]+' '


print CompletedClasses
print ''
print ActiveClasses
