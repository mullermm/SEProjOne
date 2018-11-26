import java.io.*;
import java.util.Scanner;

/**
 * This scanner will take a csv file of courses and create a filtered CSV file ready to be read in
 * the PrereqListBuilder class.
 */
public class PrereqSanner {

    /**
     * Diver for our scanner
     * @param args not used :)
     */
    public static void main(String[] args) {

        createCourseList();             //Create a list of all the courses. This might be helpful for the functionality of prereqs
        filterPrereq();                 //take the csv file and remove unneeded data (NEEDS TO BE FIRST SCANNER RUN!)
        removeExtras();                 //removes the string "Prerequisite(s): "
        removeTitles();                 //Get rid of title description of each class. We only need the course name
        concurrentFix();                //Fixes concurrent tag to just be a *
        concurrentFix2();               //Fixes case where the concurrent class ends with a ; but is still part of a list
        uppercaseNone();                //Change the word None to NONE
        removeOf();                     //Remove the word of. It is not needed
        removeSpaces();                 //Will make all whitespace characters excatly 1 in length

        PrereqListBuilder.makePrereqList();

    }

    /**
     * This method makes a list of all the courses offered at augsburg and saves it into a file called courseList.txt
     */
    public static void createCourseList(){

        try {
            File infile = new File("courses.csv");
            FileWriter fw = new FileWriter("courseList.txt");
            BufferedWriter br = new BufferedWriter(fw);

            Scanner scan = new Scanner(infile);
            scan.useDelimiter("\\n|~");

            while (scan.hasNext()) {
                br.write(scan.next() + "\n"); //Write the first delimited info of courses.csv to file
                /*Below eats the rest of the tokens for the couse
                that we don't want in our courseList.txt */
                for(int i = 0; i < 5; i++){
                    scan.next();
                }
            }
            br.close();             //flush the buffer into the file and close
        }
        catch(IOException e){
            System.out.println("Could not make temp.txt");
        }


    }

    /**
     * Removes the course titles after the actaul name for the course. For example,
     * BUS200(Exploring Business as a Vocation) becomes BUS200.
     */
    public static void concurrentFix(){

        try {
            File infile = new File("filteredCSV.txt");
            File temp = new File("temp.txt");
            FileWriter fw = new FileWriter(temp);
            BufferedWriter br = new BufferedWriter(fw);
            Scanner scan = new Scanner(infile);
            String lineIn = "";
            String regex = "[\\s]*[\\*].*[\\*]";

            while (scan.hasNext()) {
                lineIn = scan.nextLine();                                    //Get the line
                lineIn = lineIn.replaceAll(regex, "*");          //Remove any course descriptions
                /*This is so there is no new line at the end of the file*/
                if(scan.hasNext()) {
                    br.write(lineIn + "\n");                            //Write with a new line
                }
                else{
                    br.write(lineIn);                                        //Write without a new line
                }
            }

            br.close();
            CopyFile(temp, infile);
            //temp.delete();

        }
        catch(IOException e){
            System.out.println("Could not make temp.txt");
        }

    }

    /**
     * Removes the course titles after the actaul name for the course. For example,
     * BUS200(Exploring Business as a Vocation) becomes BUS200.
     */
    public static void concurrentFix2(){

        try {
            File infile = new File("filteredCSV.txt");
            File temp = new File("temp.txt");
            FileWriter fw = new FileWriter(temp);
            BufferedWriter br = new BufferedWriter(fw);
            Scanner scan = new Scanner(infile);
            String lineIn = "";
            String regex = "[\\*][;]";

            while (scan.hasNext()) {
                lineIn = scan.nextLine();                                    //Get the line
                lineIn = lineIn.replaceAll(regex, "*");          //Remove any course descriptions
                /*This is so there is no new line at the end of the file*/
                if(scan.hasNext()) {
                    br.write(lineIn + "\n");                            //Write with a new line
                }
                else{
                    br.write(lineIn);                                        //Write without a new line
                }
            }

            br.close();
            CopyFile(temp, infile);
            //temp.delete();

        }
        catch(IOException e){
            System.out.println("Could not make temp.txt");
        }

    }

    /**
     * This method will make the final file format the list in a way where it goes item, item
     */
    public static void removeSpaces(){

        try {
            File infile = new File("filteredCSV.txt");
            File temp = new File("temp.txt");
            FileWriter fw = new FileWriter(temp);
            BufferedWriter br = new BufferedWriter(fw);
            Scanner scan = new Scanner(infile);
            String lineIn = "";
            String regex = "[\\s]+";


            while (scan.hasNext()) {
                lineIn = scan.nextLine();                                    //Get the line
                lineIn = lineIn.replaceAll(regex, "");          //Remove any course descriptions
                /*This is so there is no new line at the end of the file*/
                if(scan.hasNext()) {
                    br.write(lineIn + "\n");                            //Write with a new line
                }
                else{
                    br.write(lineIn);                                        //Write without a new line
                }
            }

            br.close();
            CopyFile(temp, infile);
            temp.delete();

        }
        catch(IOException e){
            System.out.println("Could not make temp.txt");
        }

    }

    /**
     * Remove the word of from our file. We do not need it in our list.
     */
    public static void removeOf(){

        try {
            File infile = new File("filteredCSV.txt");
            File temp = new File("temp.txt");
            FileWriter fw = new FileWriter(temp);
            BufferedWriter br = new BufferedWriter(fw);
            Scanner scan = new Scanner(infile);
            String lineIn = "";
            while (scan.hasNext()) {
                lineIn = scan.nextLine();
                lineIn = lineIn.replace("of", "@");
                br.write(lineIn + "\n");
            }

            br.close();
            CopyFile(temp, infile);
            temp.delete();

        }
        catch(IOException e){
            System.out.println("Could not make temp.txt");
        }

    }

    /**
     * This method changes the string "None" to "NONE" to match the uppercase theme of the course names
     */
    public static void uppercaseNone(){

        try {
            File infile = new File("filteredCSV.txt");
            File temp = new File("temp.txt");
            FileWriter fw = new FileWriter(temp);
            BufferedWriter br = new BufferedWriter(fw);
            Scanner scan = new Scanner(infile);
            String lineIn = "";
            while (scan.hasNext()) {
                lineIn = scan.nextLine();
                lineIn = lineIn.replace("None", "NONE");
                br.write(lineIn + "\n");
            }

            br.close();
            CopyFile(temp, infile);
            temp.delete();

        }
        catch(IOException e){
            System.out.println("Could not make temp.txt");
        }

    }

    /**
     * Removes the course titles after the actaul name for the course. For example,
     * BUS200(Exploring Business as a Vocation) becomes BUS200.
     */
    public static void removeTitles(){

        try {
            File infile = new File("filteredCSV.txt");
            File temp = new File("temp.txt");
            FileWriter fw = new FileWriter(temp);
            BufferedWriter br = new BufferedWriter(fw);
            Scanner scan = new Scanner(infile);
            String lineIn = "";
            String regex = "[\\(]{1}[a-zA-Z | \\s | : | , | \\-| ' | \\/ | & | [0-9] | + | .]*[\\)]{1}";

            while (scan.hasNext()) {
                lineIn = scan.nextLine();                                    //Get the line
                lineIn = lineIn.replaceAll(regex, " ");          //Remove any course descriptions
                /*This is so there is no new line at the end of the file*/
                if(scan.hasNext()) {
                    br.write(lineIn + "\n");                            //Write with a new line
                }
                else{
                    br.write(lineIn);                                        //Write without a new line
                }
            }

            br.close();
            CopyFile(temp, infile);
            //temp.delete();

        }
        catch(IOException e){
            System.out.println("Could not make temp.txt");
        }

    }

    /**
     * This method removes the string "Prerequisite(s): " from the filteredCSV.txt file and replaces it with a " ".
     */
    public static void removeExtras(){

        try {
            File infile = new File("filteredCSV.txt");
            File temp = new File("temp.txt");
            FileWriter fw = new FileWriter(temp);
            BufferedWriter br = new BufferedWriter(fw);
            Scanner scan = new Scanner(infile);
            String lineIn = "";
            while (scan.hasNext()) {
                lineIn = scan.nextLine();
                lineIn = lineIn.replace("Prerequisite(s): ", " ");
                br.write(lineIn + "\n");
            }

            br.close();
            CopyFile(temp, infile);
            temp.delete();

        }
        catch(IOException e){
            System.out.println("Could not make temp.txt");
        }
    }

    /**
     * This method takes the courses.csv file and pulls out the first and the last value of the csv. It then
     * stores these into a file named "filteredCSV."
     */
    public static void filterPrereq(){

        int debugLine = 0;

        try {
            File infile = new File("courses.csv");
            FileWriter fw = new FileWriter("filteredCSV.txt");
            BufferedWriter br = new BufferedWriter(fw);

            Scanner scan = new Scanner(infile);
            scan.useDelimiter("\\n|~");

            while (scan.hasNext()) {
                br.write(scan.next());                          //Write the Course Name
                debugLine++;
                br.write("~");                              //Use this delimeter to sperate the course name

                /*Below eats the next four attributes of a course in
                course.scv. We only want the course name and prereq,
                so these four items are unneeded.*/
                for(int i = 0; i < 4; i++){
                    scan.next();
                    debugLine++;
                }

                br.write(scan.next() + "%\n");               //Write the prereq and the newline
                debugLine++;
               // System.out.println("inline: " + debugLine);     //prints the line for debugging.
            }

            br.close();                                         //flush the buffer and write the rest to the file
            System.out.println("Done");
        }
        catch(IOException e){
            System.out.println("Could not make temp.txt");
        }


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

}
