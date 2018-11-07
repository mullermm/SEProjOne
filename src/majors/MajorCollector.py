import csv
import os
import codecs

transcript = [] #Holds classes from transcript
majortxt = [] #Holds the name of the file for the major txts.
majorinprogress = []

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
print(majorinprogress)

for progress in majorinprogress:
        print(progress)

