package scanner;
/**
 * This class will create the TextScanner object, which is responsible for parsing through courses.txt
 * and then creating a course object out of each course. It then pushes those into an arraylist and writes
 * them into the courses.csv file
 */
import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class TextScanner
{
    /**
     * This is the generic constructor for the TextScanner object
     */
    public TextScanner() { }

    /**
     * This method will parse through courses.txt and create a course object out of each course
     * and then push each course object into the arraylist courseList
     * @param inFile the file being read from
     * @return courseList, the arraylist holding all the course objects
     */
    public ArrayList<Course> scan(File inFile)
    {
        // This ArrayList will hold all of the course objects to later be printed out line by line in courses.csv
        ArrayList courseList = new ArrayList();

        // Creates the file reader and writer and handles any exceptions that this may cause
        try{
            Scanner reader = new Scanner(inFile);

            while(reader.hasNextLine())
            {
                Course course = new Course();

                courseList.add(course);
            }
        }
        catch (FileNotFoundException e){
            System.out.println(e.getMessage());
        }

        return courseList;
    }

    /**
     * This method will iterate through each course object in inList and write their toString() call into
     * courses.csv
     * @param inFile the file being written to
     * @param inList the arraylist being iterated through
     */
    public void writeToFile(File inFile, ArrayList inList)
    {
        ArrayList<Course> courseList = new ArrayList();
        courseList = inList;
    }
}
