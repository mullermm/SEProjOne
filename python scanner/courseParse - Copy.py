#Initialization

ClassDeptShort = []
ClassNum = []
ClassDeptShortandnum = []
ClassTitle = []
ClassCredits = []
description = []
CoreCurric = []
PreReqs = []
DepartmentFull = []
ClassObject = []
ClassID = []

f1=open('out.txt', 'w')



# Main 



file = open("courses.txt")
while True:
    line1 = file.readline()
    if any(str.isdigit(c) for c in (line1[-4:])) and any(str.isalpha(l) for l in (line1[:3])) and len(line1) == 7:
        ClassDeptShort.append(line1[:3])
        ClassNum.append(line1[-4:])
        ClassDeptShortandnum.append(line1.replace("\n", ""))
    if not line1:
        break



for x, dept in enumerate(ClassDeptShort):
    classdeptnum = ClassDeptShort[x] + ClassNum[x]
    with open("courses.txt") as file:
        for num, line in enumerate(file):
            if classdeptnum in line:
                lines = open("courses.txt").readlines()
                ClassTitle.append(lines[num+1])
                ClassCredits.append(lines[num+2])



for z, dept3 in enumerate(ClassDeptShort):
    ClassID.append(z)
for x, dept in enumerate(ClassDeptShort):
    classdeptnum = ClassDeptShort[x] + ClassNum[x]
    with open("courses.txt") as file:
        for num, line in enumerate(file):
            if classdeptnum in line:
                lines = open("courses.txt").readlines()
                i = num + 3
                desc = ""
                while "Core Curriculum Component:" not in lines[i]:
                    if len(lines[i]) == 2:
                        desc += ""
                        i += 1
                    else:
                        desc += lines[i]
                        i += 1
                description.append(desc)
                CoreCurric.append(lines[i])
                PreReqs.append(lines[i+1])



for x, dept in enumerate(ClassDeptShort):
    key = ClassDeptShort[x] + " "
    with open("courses.txt") as file:
        for num, line in enumerate(file):
            if key in line and " " in line[5:6] and " " in line[3:4]:
                DepartmentFull.append(line)




for x, dept in enumerate(PreReqs):
    ClassID.append(x)
for x, dept in enumerate(PreReqs):
    temp = []
    string = str(PreReqs[x])
    if string.find("None") == -1 and len(string) > 4:
        array = string.replace("Prerequisite", "").replace("(", " ").split()
        for tempstring in array:
            if any(str.isdigit(c) for c in (tempstring[-4:])) and any(str.isalpha(l) for l in (tempstring[:3])) and len(tempstring) >= 6:
                temp.append(tempstring)
                for course in temp:
                    try:
                        id = ClassDeptShortandnum.index(course)
                        temp.remove(course)
                        temp.append(id)
                    except ValueError:
                        print("Could Not Determine Course")

        
f1.write("Department~Course Number~Course Title~Credits~Course Description~Core Curiculum~Prerequisites" + "\n")

for x in range (0, len(ClassDeptShort)):

    noNdesc = ClassDeptShort[x].replace("\n", "")
    f1.write(noNdesc + '~')

    noNdesc = ClassNum[x].replace("\n", "")
    f1.write(noNdesc + '~')

    noNdesc = ClassTitle[x].replace("\n", "")
    f1.write(noNdesc + '~')

    noNdesc = ClassCredits[x].replace("\n", "")
    noNdesc = noNdesc.replace(" Semester Credits", "")
    f1.write(noNdesc + '~')

    noNdesc = description[x].replace("\n", " ")
    f1.write(noNdesc + '~')

    noNdesc = CoreCurric[x].replace("\n", "")
    noNdesc = noNdesc.replace("Core Curriculum Component: ", "")
    f1.write(noNdesc + '~')

    noNdesc = PreReqs[x].replace("\n", "")
    noNdesc = noNdesc.replace("Prerequisite(s): ", "")
    f1.write(noNdesc)
        
    f1.write('\n')

f1.close()








