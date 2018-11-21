import os
import re



#############################################################
#Used to check to see if the class has no prereqs. It looks
#through all of the classes and checks to see if its prereq
#is labeled as 'NONE'. If so, it returns false, otherwise
#it returns true.
#############################################################
def hasPrereq(lines):
    for i in lines:
        print()

def countBracks():

    outFile = open("temp.txt", "w")                 #This will be used to hold our file that we are building
    outFile.write("[\n")                            #Write the first Left Bracket For the whole list

    for line in open("prereqList.txt"):             #For every line in the file
        currentBrak = line.count("[")               #Count how many left brackets there are
        if(currentBrak < 5):                        #If there is less than 5 left brackets
            maxBrak = currentBrak
            outFile.write(line[:len(line) - 2])     #Remove the last bracket from the line
            if(currentBrak == 4):                   #If we need to add one padded x
                outFile.write(",['X']]\n")
            if(currentBrak == 3):                   #If we need to add two padded x
                outFile.write(",['X'],['X']]\n")
            if(currentBrak == 2):                   #If we need to add three padded x
                outFile.write(",['X'],['X'],['X']]\n")
        else:
            outFile.write(line)                     #Writes the line because it already has 5 sub list

    outFile.write("]")                              #Close the file with a left bracket for the whole list
    os.remove("prereqList.txt")                     #Removes the temp file we used to append the blanks to our list
    os.rename('temp.txt', "prereqList.txt")


#def junk():
    # file = open("prereqList.txt", "r")
    # lines = file.read().split(']').split('').split('[')
    # lines = [line.strip() for line in file]
    # print(lines[0])
    # sub = [[]]
    #
    # with open('input.txt', 'r') as f:
    #     # gets lines as list of strings [['1, 2, 3,', ...]]
    #     nodes_list = [n.split() for n in f.readlines()]
    #     # convert strings inside the lists to int's [[1, 2, 3], ...]
    #     nodes_list = [[int(y[0]), int(y[1]), int(y[2])] for y in nodes_list]
    #
    # for line in lines:
    #     lineHelper = []
    #     linehelper = list(line)
    #     sub.append(linehelper)
    # print(sub[1][1])


def main():
    countBracks()                                   #This will pad the list file so python can read it in as a list of list


    lines = []
    with open("prereqList.txt") as file:
        for line in file:
            line = line.replace(",","").replace("[","").replace("]","").strip() .split("'")  # or some other preprocessing
            lines.append(line)  # storing everything in memory!
    print(lines)
    print(lines[140][2])

    lines2 = []
    lineBuidler = ""
    i = 1;
    j = 1;

    for classes in lines:
        lineBuidler = lineBuidler + "'" + lines[i][j] + "'"
        if(j < 9):
            lineBuidler = lineBuidler + ","
            j = j + 2
        else:
            j = 1
            i = i + 1
            lines2.append(lineBuidler.split(","))
            lineBuidler = ""

    print(lines2[140])

    #['', 'ACC221', ',[', 'NONE', '],[', 'X', '],[', 'X', '],[', 'X', ']]\n']



main()