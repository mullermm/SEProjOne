### How This Scanner Works

This file takes the Course List provided by the customer and creates the document courses.csv. There are a few things
you should know about this scanner.

* The file inputted to the scanner must be stored as or in CourseDescriptions.txt
* The file provided by the customer has an error on line 2410. The line needs to be split into two lines.

        AP Courses APPROVED BY GAAC cont ed 1 Semester Credits

   should become

        AP Courses APPROVED BY GAAC cont ed
        1 Semester Credits

* As the scanner runs, Line number: is printed to the console. This can be used in debugging if needed.
* The scanner uses a temp file called temp.txt. This will be deleted once the scanner is completed
* This project can edited and configured easily if imported in intellij. All the config files have been added to the repo.

### Ready to Go!
The courses.csv file that the scanner created is ready to be incorporated as the database for the PHP course project.

