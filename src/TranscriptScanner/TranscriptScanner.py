


# This function filters out courses from a transcript.txt file
# Used newocr.com formatting
# The output from newocr.com has some errors: if the document has
# multiple pages, classes listed at the page break likely will be broken.
def read_file(userFile):
        # Array for storing classes
        classes = []
        #Input file
        in_file = open(userFile, 'r')

        # Dump all text into array
        words = in_file.readlines()

        # Iterate over all text
        for i in range (len(words)):
            # Look at a word
            scan = words[i]
            
            # Check the first 3 chars
            first_three = scan[:2]
            
            # Check the next 3 chars
            next_three = scan[3:5]
            
            # Check for right format (3 uppercase followed by 3 nums)
            if ( (first_three.isupper() ) and (next_three.isdigit() ) ): 
                # Get rid of newline char, put into classes array
                line = words[i].rstrip()
                classes.insert(i, line)

        file_name = "FormattedTranscript.txt"
        file = open(file_name, 'w')
        for i in range (len(classes)):
            file.write(classes[i] + "\n")
        
        #return classes
def main():
    file = "Transcript.txt"
    read_file(file)
    
main()
