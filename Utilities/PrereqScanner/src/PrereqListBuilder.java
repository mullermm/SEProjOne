import com.sun.xml.internal.ws.policy.privateutil.PolicyUtils;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class PrereqListBuilder {

    public static void makePrereqList(){

        try {
            File infile = new File("filteredCSV.txt");
            FileWriter fw = new FileWriter("prereqList.txt");
            BufferedWriter br = new BufferedWriter(fw);
            br.write("[");                              //First bracket for the list of list
            String input = "";
            boolean doneWithLine = false;
            Scanner scan = new Scanner(infile);
            int count = 1;

            /*This first loop runs for the length of the file. The name of
            each course is written before the prereq inner loop runs*/
            while (scan.hasNext()) {

                scan.useDelimiter("~");                         //delimeter sperating the name from prereqs
                br.write("['");                             //"[" for the course and the " ' " for the course name string

                /*The line below add the name and the closing " ' ". The reason we have a .replace
                * is because the /n character at the end of each line in filterdCSV is not
                * dealt with by the scanner. This replace deals with it*/
                br.write(scan.next().replace("\n","y") + "', ");
                scan.useDelimiter("\n|;");                       //delimeter seperating the end of the prereqs or seperate prereqs
                input = scan.next();                             //Store the next token
                doneWithLine = false;


                System.out.println("---------");
                System.out.print("debug " + count + ": ");
                while(!doneWithLine){
                    input = input.replace("~", "");
                    System.out.println("The input: " + input);
                    /*If there is no prereqs CASE1 BREAK*/
                    if(input.equals("NONE%")){
                        br.write("['NONE']]");
                        doneWithLine = true;
                        break;
                    }
                    /*If the prereqs are a number of a list ex. 1 MAT100, MAT110*/
                    if(input.contains("^")){
                        /*If the input is the last of the line, remove the % delim, add, and break loop*/
                        if(input.contains("%")) {
                            input = input.replace("%", "");
                            System.out.print(" var ");
                            variablePrereq(br, input);
                            doneWithLine = true;
                            break;
                        }
                        else{
                            variablePrereq(br, input);
                        }
                    }
                    /*if the classes are all required prereqs*/
                    else{
                        input = input.replace("%", "");
                        String[] classes = input.split(",");
                        br.write("['");
                        for(int i = 0; i < classes.length; i++){
                            if(i + 1 != classes.length){
                                br.write(classes[i] + "', ");
                            }
                            else{
                                br.write(classes[i] + "']]");
                                doneWithLine = true;
                                break;
                            }
                        }
                    }
                }

                br.write("\n");
                count++;
            }

            br.write("]");     //close the list of lists
            br.close();

        }
        catch(IOException e){
            System.out.println(e.getStackTrace());
        }




    }

    public static void variablePrereq(BufferedWriter br, String input){
        try {
            br.write("[");
            String[] prereq = input.split("@");      //split the string into an array into the number and the classes
            br.write(prereq[0] + ", ");                //Write the number of needed classes completed
            System.out.print("rereq 0 is " + prereq[0]);
            String[] classes = prereq[1].split(",");  //split the classes into an array

            for (int i = 0; i < classes.length; i++) {
                if (i + 1 != classes.length) {
                    br.write("'" + classes[i] + "',");
                } else {
                    br.write("'" + classes[i] + "']");
                }
            }
        }
        catch(IOException e){
            System.out.println("Cant write to prereqList in method variablePrereq");
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
