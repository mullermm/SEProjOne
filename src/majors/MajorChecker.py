import csv
import os
import codecs

transcript = [] #Holds classes from transcript

#Load ups transcript
transciptfile = open("FakeTranscript.txt","r+")
for line in transciptfile.readlines():
        transcript.append(line.rstrip('\n'))

