import csv
import os
import codecs

transcript = [] #Holds classes from transcript
majortxt = [] #Holds the name of the file for the major txts.
majorinprogress = [] #Holds the majors that are inprogress for the user.


#Load ups transcript
transciptfile = open("FakeTranscript.txt","r+")
for line in transciptfile.readlines():
        transcript.append(line.rstrip('\n'))

#Loads up all of the majors
for root, dirs, files in os.walk("./txt"): 
    for filename in files:
        if filename != "RTF.py":
                majortxt.append(filename)

for major in majortxt:
        filedr  = "./txt/" + major
        file = codecs.open(filedr,"r+",'utf-16')
        for line in file.readlines():
                if "                                 4" in line and any(substring in line for substring in transcript):
                        if major not in majorinprogress:
                                majorinprogress.append(major)
        file.close

data = "BIO Biopsychology 2018.txt"
courselist = []
print(data)
filedr  = "./txt/" + data
file = codecs.open(filedr,"r+",'utf-16')
for line in file.readlines():
        if "                                 4" in line:
                line = line.split(" ")
                line[:] = (value for value in line if value != "")
                line[:] = (value for value in line if value != "4")
                courselist.append(line[0])
print(courselist)
file.close

