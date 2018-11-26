import os
import sys

#############################################################
#Will count brakes and edit the text file needed to read in
#the course list and edit it appropriatly.
#############################################################
def countBracksAndPad():

    outFile = open("temp.txt", "w")                 #This will be used to hold our file that we are building
    outFile.write("[\n")                            #Write the first Left Bracket For the whole list

    for line in open("prereqList.txt"):             #For every line in the file
        currentBrak = line.count(",")               #Count how many left brackets there are
        if(currentBrak < 4):                        #If there is less than 5 left brackets
            maxBrak = currentBrak
            outFile.write(line[:len(line) - 2])     #Remove the last bracket from the line
            if(currentBrak == 3):                   #If we need to add one padded x
                outFile.write(",X\n")
            if(currentBrak == 2):                   #If we need to add two padded x
                outFile.write(",X,X\n")
            if(currentBrak == 1):                   #If we need to add three padded x
                outFile.write(",X,X,X\n")
        else:
            outFile.write(line)                     #Writes the line because it already has 5 sub list

    outFile.write("]")                              #Close the file with a left bracket for the whole list
    os.remove("prereqList.txt")                     #Removes the temp file we used to append the blanks to our list
    os.rename('temp.txt', "prereqList.txt")


#############################################################
#Will replace a string in the prereqList.txt with another string
#############################################################
def replaceString(x, y):
    with open('prereqList.txt', 'r') as infile, \
            open('temp.txt', 'w') as outfile:
        data = infile.read()
        data = data.replace(x, y)
        outfile.write(data)

    os.remove("prereqList.txt")  # Removes the temp file we used to append the blanks to our list
    os.rename('temp.txt', "prereqList.txt")

#############################################################
#Will make the list of classes with their respective prereqs
#############################################################
def readInList():
    lines = []
    with open("prereqList.txt") as file:
        for line in file:
            # line = line.replace(",","").replace("[","").replace("]","").strip() .split("'")  # or some other preprocessing
            line = line.strip("\n").split(",")  # or some other preprocessing
            lines.append(line)  # storing everything in memory!

    return lines

#############################################################
#Will take all the prereq sub list and create a list of them
#############################################################
def makeSubList(courseList):
    for i in range(1,len(courseList) - 1):
        for j in range(0,4):
            #if (courseList[i][j].contains("|")):
            if "|" in courseList[i][j]:
                lineBuilder = []
                lineBuilder = courseList[i][j].split("|")
                courseList[i][j] = lineBuilder
    return courseList

#############################################################
#Used to check to see if the class has no prereqs. It looks
#through all of the classes and checks to see if its prereq
#is labeled as 'NONE'. If so, it returns false, otherwise
#it returns true.
#############################################################
def hasPrereq(courseList, classToLookFor):
    for i in range(0,len(courseList) - 1):
        if courseList[i][0] == classToLookFor:
            if courseList[i][1] == "NONE":
                return True
    return False

#############################################################
#Returns true if input is an integer, false if not
#############################################################
def is_int(input):
  try:
    num = int(input)
  except ValueError:
    return False
  return True


#############################################################
#This function is used to check to see if the prereqs for
#a class have been satisfied. It takes in the list of courses
#the class beign checked for prereq completion, and the
#transcript of classes completed. If the prereqs have been
#satisfied, true is returned. Otherwise, false is returned
#############################################################
def prereqMet(courseList, classToLookFor, transcript):
    completedState = True                                               #Will turn false if prereqs have not been met
    for i in range(0,len(courseList) - 1):                              #For all the courses
        if courseList[i][0] == classToLookFor:                          #If the class is found
            for j in range(1,5):                                        #For all 5 sub list
                # Case 1 : Must Complete all of the courses
                if courseList[i][j] == 'X':
                    pass                                                #Do nothing because we dont want errors looking at 'X' as an int
                # Case 2 : Complete a number of a list
                elif is_int(courseList[i][j][0]):                       #If the first item in list is an integer
                    coursesToComplete = int(courseList[i][j][0])        #Number of prereqs to complete
                    coursesCompleted = 0                                #Count the number of courses completed
                    for k in range(1,len(courseList[i][j])):            #For all the courses in the prereq
                        if courseList[i][j][k] in transcript:           #If the course is in transcript
                            coursesCompleted += 1                       #Add to the number of needed completed courses
                    if coursesCompleted < coursesToComplete:            #If the completed courses don't meet the requirements
                        completedState = False                          #The prereq is not completed
                # Case 3: All the courses in the sublist must be completed
                else:
                    for k in range(0, len(courseList[i][j])):           #For all the courses in the sublist
                        if courseList[i][j][k] not in transcript:       # If the course is NOT in transcript
                            completedState = False                      #The prereq is not completed

    return completedState

#############################################################
#This function is used to return a list of prereqs left to
#complete. If there is a need for 1 of the following, it will
#return a list of how many is needed of the remaining list.
#Otherwise, the list will be of all classes needed to take.
#############################################################
def prereqsLeft(courseList, classToLookFor, transcript):
    leftToComplete = ""                                                 #Will turn false if prereqs have not been met
    for i in range(0,len(courseList) - 1):                              #For all the courses
        if courseList[i][0] == classToLookFor:                          #If the class is found
            for j in range(1,5):                                        #For all 5 sub list
                # Case 1 : Must Complete all of the courses
                if courseList[i][j] == 'X':
                    pass                                                #Do nothing because we dont want errors looking at 'X' as an int
                # Case 2 : Complete a number of a list
                elif is_int(courseList[i][j][0]):                       #If the first item in list is an integer
                    coursesToComplete = int(courseList[i][j][0])        #Number of prereqs to complete
                    coursesCompleted = 0                                #Count the number of courses completed
                    for k in range(1,len(courseList[i][j])):            #For all the courses in the prereq
                        if courseList[i][j][k] in transcript:           #If the course is in transcript
                            coursesCompleted += 1                       #Add to the number of needed completed courses
                    if coursesCompleted < coursesToComplete:            #If the completed courses don't meet the requirements
                        if len(leftToComplete) != 0:                    #If this is the first list of prerecs to complete
                            leftToComplete += ","                       #The prereq is not completed. Add it to string to return
                        leftToComplete += "["                           #Begin the list with a bracket
                        coursesNeeded = coursesToComplete - coursesCompleted #Calulate how many prereqs are left to complete
                        leftToComplete += "'" + str(coursesNeeded) + "',"    #Add how many courses are left to take
                        for k in range(1, len(courseList[i][j])):       # For all the courses in the prereq
                            if courseList[i][j][k] not in transcript:       # If the course is in transcript
                                leftToComplete += "'" + courseList[i][j][k] + "',"
                        leftToComplete = leftToComplete[0: len(leftToComplete) - 2] #Remove the last comma from list
                        leftToComplete += "]"                           #Close the list with a bracket

                # Case 3: All the courses in the sublist must be completed
                else:
                    beginingBracAdded = False                           #Used to keep track of if the bracket at the begining of list has been added
                    for k in range(0, len(courseList[i][j])):           #For all the courses in the sublist
                        if courseList[i][j][k] not in transcript:       # If the course is NOT in transcript
                            if beginingBracAdded == False:              #If this is the first prereq in the list to not be completed
                                if len(leftToComplete) != 0:            #If there are previous prereqs not completed
                                    leftToComplete += ","               #add a comma
                                leftToComplete = leftToComplete + "["   #add the begining bracked
                                beginingBracAdded = True                #Backet hass been added to begining so we turn the helper false
                            leftToComplete += "'" + str(courseList[i][j][k] + "', ")    #The prereq is not completed
                    if beginingBracAdded == True:                       #If we added a prereq to leftToComplete
                        leftToComplete = leftToComplete[0:len(leftToComplete) - 2]      #Remove the last comma added in the line above
                        leftToComplete += "]"                           #Add closing bracket for list


    if len(leftToComplete) == 0:
        leftToComplete = "Prereqs Have Been Satisfied"

    return leftToComplete

#############################################################
#This is our driver for this project
#############################################################
def main(option, courseFocusedOn, allScriptARGS):

    #These three lines take the input, preformat it, and then make a list
    # of all the courses with the prerqs. We can then use this course list
    #to check all courses prereqs.
    countBracksAndPad()                         #This will pad the list file so python can read it in as a list of list
    CourseList = readInList()                   #Will read in the list of courses and save it to list
    CourseList = makeSubList(CourseList)        #Create the sublist for each prereq

    # These three lines take any string inputted after the first two arguments
    # and makes a list/string of them. This list can then be treated as a transcript
    transcript = ""
    for i in range(3,len(allScriptARGS)):                                  #For all arguments past the script path, option, and course to look at
        transcript = transcript + allScriptARGS[i].replace(",[]'", "")     #Add the arguments to the trasncript variable


    #Option to check if a class has no prereqs
    try:
        if(int(option) == 1):
            print(hasPrereq(CourseList, courseFocusedOn))
        #Option to return
        elif(int(option) == 2):
            print(prereqMet(CourseList, courseFocusedOn, transcript))
        elif(int(option) == 3):
            print(prereqsLeft(CourseList, courseFocusedOn, transcript))
        else:
            raise ValueError('Option was not 1,2, or 3')
    except:
        print("Argument error, check input parameters")

    #print(prereqsLeft(CourseList, courseFocusedOn, transcript))
    #############################
    #Debug Area
    #############################
    #Print course has prereq for course
    #print("Does inputted class have a prereq?")
    #print(hasPrereq(CourseList,courseFocusedOn))


main(sys.argv[1], sys.argv[2], sys.argv)