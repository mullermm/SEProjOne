import java.io.*;
import java.util.NoSuchElementException;
import java.util.Scanner;


/**
 * This class is for scanning the text document comprised of courses. This list was provided by
 * the customer. It contains methods that are helpful to scanning the Course list provided by the customer.
 */
public class CourseScanner {

    public static void main(String[] args){

        ScanCourseList();

    }

    /**
     * This method is used to scan CourseDescriptions.txt, remove page numbers, read in the text, create course
     * objects, and create a CourseList object. This CourseList object will contain every course offered at
     * Augsburg.*/
    public static void ScanCourseList(){

        /** This is the course list provided by the customer*/
        File fileIn = new File("CourseDescriptions.txt");

        /** This is the temp file we will use to modify the course list from the customer.
         * We need a temp because we will be reading lines from the customer text and then
         * create a temp using the text we want to keep. Eventually, this Temp.txt will
         * be written back to CourseDescriptions.txt*/
        File tempFile = new File("Temp.txt");

        /**Create the new file and verify we are not writing over an already existing Temp.txt*/
        try {
            tempFile.createNewFile();
        }
        catch(IOException e) {
            System.out.println("File already exists.");
        }

        /** Make sure the scanner actually finds the file and that*/
        try {


            /* The next three lines are used to manipulate the text file CourseDescriptions.txt. First, we remove
             * the page numbers from the file. Next, we remove any department name "headers" from the file. Last,
             * we take the CourseListDescriptions.txt file and create our list of courses inside our course list
             * object. */

            Scanner scanner = new Scanner(fileIn);      //Our scanner to read in the file from the customer
            RemovePageNumber(scanner, fileIn, tempFile);//Removes the page number from the text file

            scanner = new Scanner(fileIn);              //Our scanner to read in the file from the customer
            RemoveBlankLines(scanner, fileIn, tempFile);//Removes all empty lines from the text file

            scanner = new Scanner(fileIn);              //Our scanner to read in the file from the customer
            RemoveLeadingWhiteSpace(scanner, fileIn, tempFile); //Removes any white space at the front of a line

            scanner = new Scanner(fileIn);              //Our scanner to read in the file from the customer
            createCourseCSV(scanner, fileIn, tempFile); //Turns course list file into our database file

            scanner = new Scanner(fileIn);
            //cleanupFinalText(scanner, fileIn, tempFile);


        }
        catch (FileNotFoundException e){
            System.out.println("Input File Not Found! Expected to find CourseDescriptions.txt");
        }
        catch (IOException e){
            System.out.println("Error opening the temp file CourseListText/Temp.txt");
        }

    }

    /**
     * This method takes a course list object and populates the listOfCourses.
     *
     * @param scanner scanner containing file of course descriptions
     * @return CourseList that has had listOfCourses populated
     */
    public static void createCourseCSV(Scanner scanner, File fileIn, File tempFile){

        /*
        These regular expressions are used inside the scanner to verify certain input being read in from
        CourseDescriptions.txt.
         */
        final String headerRegex = "([A-Z]{2})(\\s)(–|-).*|([A-Z]{3})(\\s)(–|-).*|([A-Z]{5})(\\s)(–|-).*";
        final String prereqRegex = "[A-Z]{3}[0-9]{3}$|[A-Z]{2}[0-9]{3}$|[A-Z]{3}[0-9]{3}[A-Z]{2}$|[A-Z]{3}[0-9]{4}[A-Z]{2}$|[A-Z]{3}[0-9]{3}[L]{1}$|[A-Z]{3}[0-9]{3}[P]{1}$|[A-Z]{5}[0-9]{1}$]";

        int lineCount = 0;

        scanner.nextLine();                                 //Eats the first line of the file. We don't need it
        lineCount++;
        String temp = "";                                   //This will hold the current line being read in by scanner
        String delimiter = "~";                             //Delimiter used between items in the course list database
        temp = scanner.nextLine();                          //read in the first line. line at the end of while loop will read this line for second course
        lineCount++;



        try {

            FileWriter fw = new FileWriter(tempFile);           //Make a file writter of out tempfile
            BufferedWriter br = new BufferedWriter(fw);         //This will be used to write the text to a temp
            fw.flush();                                         //Makes sure tempFile is flushed

            while (scanner.hasNext()) {                          //While the EoF of fileIn has not been reached

                if (temp.matches(headerRegex)) {  //If the next line is a department header
                    temp = scanner.nextLine();                                //read in the next line
                    lineCount++;
                }

                br.write(temp + delimiter);                 //write the course number
                temp = scanner.nextLine();                      //Gets the course name
                lineCount++;
                br.write(temp + delimiter);                 //write the course name
                temp = scanner.nextLine();                      //gets the course credits
                lineCount++;
                br.write(Integer.parseInt(temp.substring(0, 1)) + delimiter);  //Write the credit amount
                temp = scanner.nextLine();                      //Gets the begining of the course description
                lineCount++;

                int repeatedLineCounter = 0;
                //This will run until we find the word "Core" because the course description can be multiple lines
                while (temp.startsWith("Core") == false) {
                    if(repeatedLineCounter == 0) {
                        br.write(temp);                        //write line with course description
                    }
                    else{
                        br.write(" " + temp);             //write line with course description with a leading space
                    }
                    temp = scanner.nextLine();                //get the next line
                    lineCount++;
                    repeatedLineCounter++;
                }
                br.write(delimiter);                            //add the delimeter

                br.write(temp + delimiter);                 //Write the core curriculum. This is always one line
                temp = scanner.nextLine();                      //Get the next line
                lineCount++;

                //This try catch is simply used for catching the end of the file exception
                try {
                    repeatedLineCounter = 0;
                    while (!temp.matches(prereqRegex) && !temp.matches(headerRegex)) {
                        if(repeatedLineCounter == 0) {
                            br.write(temp);                     //Write the prereq
                        }
                        else{
                            br.write(" " + temp);          //write prereq with a leading space
                        }
                        temp = scanner.nextLine();
                        lineCount++;
                    }
                } catch (NoSuchElementException e) {
                    //End of the file has been reached. THIS IS THE CLEANUP WORK!
                    br.close();                                         //Close the writer so the buffer clears to temp.txt
                    File outfile = new File("courses.csv");
                    CopyFile(tempFile, outfile);                        //Copies contents of temp.txt back into original file
                    tempFile.delete();                                  //Deletes the temp file
                }
                br.write("\n");
                System.out.println("Line number: " + lineCount);
                //ECS585CE
            }
        }
        catch(IOException e){
            //Do nothing because we are at the end of the file :D
        }
    }


    /**
     * This method is used to remove page numbers from CourseDescriptions.txt
     * @param scanner       Scanner built from CourseDescriptions.txt
     * @param fileIn        File object containing the path to CourseDesctiptions.txt
     * @param tempFile      File object containing the path to Temp.txt
     * @throws IOException  Is thrown if scanner and files have errors finding files. Caught in method that calls this.
     */
    public static void RemovePageNumber(Scanner scanner, File fileIn, File tempFile) throws IOException{

        FileWriter fw = new FileWriter(tempFile);
        BufferedWriter br = new BufferedWriter(fw);         //This will be used to write the text to a temp
        String temp;                                        //This will hold the current line being read in by scanner
        fw.flush();                                         //Makes sure tempFile is flushed

        while(scanner.hasNext()) {                          //While the EoF of fileIn has not been reached
            temp = scanner.nextLine();                      //Store next line into temp
            if (isInteger(temp)) {                          //If the line is an integer do nothing and dont copy it
                //Don't copy line to temp file
            } else {                                        //Write the line to temp.txt and append a new line
                br.write(temp);
                br.write("\n");
            }
        }

        br.close();                                         //Close the writer so the buffer clears to temp.txt
        CopyFile(tempFile, fileIn);                         //Copies contents of temp.txt back into original file
        tempFile.delete();                                  //Deletes the temp file
    }

    /**
     * This method removes any leading white space from a text file. It uses a temp file to complete this task.
     *
     * @param scanner   scanner of input file to read from
     * @param fileIn    file to have lines removed from
     * @param tempFile  temp file to store lines as you process the fileIn
     * @throws IOException  exception saying files could not be found.
     */
    public static void RemoveLeadingWhiteSpace(Scanner scanner, File fileIn, File tempFile) throws IOException{
        FileWriter fw = new FileWriter(tempFile);
        BufferedWriter br = new BufferedWriter(fw);         //This will be used to write the text to a temp
        String temp;                                        //This will hold the current line being read in by scanner
        fw.flush();                                         //Makes sure tempFile is flushed

        while(scanner.hasNext()) {                          //While the EoF of fileIn has not been reached
            temp = scanner.nextLine();                      //Store next line into temp
            if (temp.startsWith("\\s") || temp.startsWith("\f")) {                   //If the line has leading white space
                br.write(temp.substring(1,temp.length()));  //Print the substring without the leading whitespace
                br.write("\n");
            }
            else{                                           //Whole line is ok to write
                br.write(temp);                             //Write the whole line
                br.write("\n");
            }
        }

        br.close();                                         //Close the writer so the buffer clears to temp.txt
        CopyFile(tempFile, fileIn);                         //Copies contents of temp.txt back into original file
        tempFile.delete();                                  //Deletes the temp file
    }

    /**
     * This method removes any blank lines from a text file. It uses a temp file to complete this task.
     *
     * @param scanner   scanner of input file to read from
     * @param fileIn    file to have lines removed from
     * @param tempFile  temp file to store lines as you process the fileIn
     * @throws IOException  exception saying files could not be found.
     */
    public static void RemoveBlankLines(Scanner scanner, File fileIn, File tempFile) throws IOException{
        FileWriter fw = new FileWriter(tempFile);
        BufferedWriter br = new BufferedWriter(fw);         //This will be used to write the text to a temp
        String temp;                                        //This will hold the current line being read in by scanner
        fw.flush();                                         //Makes sure tempFile is flushed

        while(scanner.hasNext()) {                          //While the EoF of fileIn has not been reached
            temp = scanner.nextLine();                      //Store next line into temp
            if (temp.isEmpty()) {                           //If the line is an blank line
                //Don't copy line to temp file
            } else {                                        //Write the line to temp.txt and append a new line
                br.write(temp);
                br.write("\n");
            }
        }

        br.close();                                         //Close the writer so the buffer clears to temp.txt
        CopyFile(tempFile, fileIn);                         //Copies contents of temp.txt back into original file
        tempFile.delete();                                  //Deletes the temp file
    }

    /**
     *This method takes two files and copies ton contents of the inFile to the outFile.
     *
     * @author https://www.tutorialspoint.com/javaexamples/file_copy.htm
     * */
    public static void CopyFile(File inFile, File outFile) {
        FileInputStream ins = null;
        FileOutputStream outs = null;
        try {
            ins = new FileInputStream(inFile);
            outs = new FileOutputStream(outFile);
            byte[] buffer = new byte[1024];
            int length;

            while ((length = ins.read(buffer)) > 0) {
                outs.write(buffer, 0, length);
            }
            ins.close();
            outs.close();
        } catch(IOException ioe) {
            ioe.printStackTrace();
        }
    }

    /**
     * This method will check to see if a string is an integer. If so, it returns true, else it returns false
     *
     * @author Oscar Lopez - https://stackoverflow.com/questions/8336607/how-to-check-if-the-value-is-integer-in-java
     */
    public static boolean isInteger(String s) {
        boolean isValidInteger = false;
        try {
            Integer.parseInt(s);
            isValidInteger = true;
        }
        catch (NumberFormatException ex)
        {
            //Is not an integer
        }
        return isValidInteger;
    }

}
