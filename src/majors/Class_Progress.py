import sys
import ConLib
import csv
from Major import *

def main():
    major_number = int(sys.argv[1])
    print(functions[major_number](transcript, 1))
    print(functions[major_number](transcript, 2))

if __name__ == "__main__":
    main()

