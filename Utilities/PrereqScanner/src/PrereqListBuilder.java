import com.sun.xml.internal.ws.policy.privateutil.PolicyUtils;

import java.io.*;
import java.util.Scanner;

/**
 * This class is used to take the filteredCSV.txt file and convert it into a list of list that can be read
 * in by the python program used to manage the prereqs.
 */
public class PrereqListBuilder {

    /**
     * This method is used to make the prereqList.txt file that python can read in. It is the driver of
     * this class, but can be called from another class.
     */
    public static void makePrereqList(){

        try {
            File infile = new File("filteredCSV.txt");
            FileWriter fw = new FileWriter("prereqList.txt");
            BufferedWriter br = new BufferedWriter(fw);
            br.write("[");                              //First bracket for the list of list
            String input = "";
            boolean doneWithLine = false;
            Scanner scan = new Scanner(infile);

            /*This first loop runs for the length of the file. The name of
            each course is written before the prereq inner loop runs*/
            while (scan.hasNext()) {

                scan.useDelimiter("~");                         //delimeter sperating the name from prereqs
                br.write("");                             //"[" for the course and the " ' " for the course name string

                /*The line below add the name and the closing " ' ". The reason we have a .replace
                * is because the /n character at the end of each line in filterdCSV is not
                * dealt with by the scanner. This replace deals with it*/
                br.write(scan.next().replace("\n","") + ",");
                scan.useDelimiter("\n|;");                       //delimeter seperating the end of the prereqs or seperate prereqs
                input = scan.next();                             //Store the next token
                doneWithLine = false;

                while(!doneWithLine){
                    input = input.replace("~", "");  //Remove the delimiter between name and prereqs
                    /*If there is no prereqs CASE1 BREAK*/
                    if(input.equals("NONE%")){
                        br.write("NONE]");                      //append no prereqs
                        doneWithLine = true;
                        break;
                    }
                    /*If the prereqs are a number of a list ex. 1 MAT100, MAT110*/
                    if(input.contains("@")){
                        /*If the input is the last of the line, remove the % delim, add, and break loop*/
                        if(input.contains("%")) {
                            input = input.replace("%", "");       //remove the end of line flag
                            variablePrereq(br, input);                              //append the variable prereq
                            br.write("]");                                      //close the list
                            doneWithLine = true;
                            break;
                        }
                        else{                                                       //not the end of the line
                            variablePrereq(br, input);                              //append the variable prereq
                            br.write(",");
                            input = scan.next();                                    //get the next line
                        }
                    }
                    /*if the classes are all required prereqs*/
                    else{
                        input = input.replace("%", "");
                        String[] classes = input.split(",|\\*");            //split with the * too because classes being conccurrent
                        br.write("");
                        for(int i = 0; i < classes.length; i++){                  //for all the classes required
                            if(i + 1 != classes.length){                          //if its not the last class in the list
                                br.write(classes[i] + "|");                  //add the classes
                            }
                            else{                                                 //its the last class
                                br.write(classes[i] + "]");                 //write the class and close the list
                                doneWithLine = true;
                                break;
                            }
                        }
                    }
                }

                /*****THIS MIGHT NEED TO BE REMOVED BEFORE READING INTO PYTHON*******/
                br.write("\n");
            }

            br.write("]");     //close the list of lists
            br.close();

            File filered = new File("prereqList.txt");

            File prereqScannerFile = new File("../PreReq/prereqList.txt");
            CopyFile(filered, prereqScannerFile);

        }
        catch(IOException e){
            System.out.println(e.getStackTrace());
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

    /**
     * This method writes a list of classes to the prereqs list in a way where the first item in the list is how
     * many of the classes you have to take and the remainder of the list is the classes you can pick from.
     * @param br bufferedwritter that will be outputted to file
     * @param input string containing prereq number and classes to be made a list of
     */
    public static void variablePrereq(BufferedWriter br, String input){
        try {
            br.write("");
            String[] prereq = input.split("\\@");      //split the string into an array into the number and the classes
            br.write(prereq[0] + "|");                //Write the number of needed classes completed
            String[] classes = prereq[1].split(",");  //split the classes into an array

            for (int i = 0; i < classes.length; i++) {
                if (i + 1 != classes.length) {
                    br.write("" + classes[i] + "|");
                } else {
                    br.write("" + classes[i] + "");
                }
            }
        }
        catch(IOException e){
            System.out.println("Cant write to prereqList in method variablePrereq");
        }
    }

}
