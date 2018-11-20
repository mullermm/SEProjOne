import com.sun.xml.internal.ws.policy.privateutil.PolicyUtils;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class PrereqListBuilder {

    public void makePrereqList(){

        try {
            File infile = new File("filteredCSV.csv");
            FileWriter fw = new FileWriter("prereqList.txt");
            BufferedWriter br = new BufferedWriter(fw);
            br.write("[");                              //First bracket for the list of list
            String input = "";

            Scanner scan = new Scanner(infile);
            boolean lineDone = false;

            /*This first loop runs for the length of the file. The name of
            each course is written before the prereq inner loop runs*/
            while (scan.hasNext()) {

                scan.useDelimiter("~");                         //delimeter sperating the name from prereqs
                br.write("['");                             //"[" for the course and the " ' " for the course name string
                br.write(scan.next() + "', ");              //add the name and the closing " ' "
                scan.useDelimiter("\\n|;");                     //delimeter sperating the end of the prereqs or seperate prereqs
                input = scan.next();                            //Store the next token

                while(!lineDone){

                    /*If there is no prereqs CASE1 BREAK*/
                    if(input == "NONE"){
                        br.write(input + "]");
                        break;
                    }
                    /*If the prereqs are a number of a list ex. 1 MAT100, MAT110*/
                    if(input.contains("^")){
                        variablePrereq(br, input);
                    }
                    /*if the classes are all required prereqs*/
                    
                }


            }

        }
        catch(IOException e){
            System.out.println("Could not make prereqList.txt");
        }




    }

    public void variablePrereq(BufferedWriter br, String input){
        try {
            br.write("[");
            String[] prereq = input.split("^");      //split the string into an array into the number and the classes
            br.write(prereq[0] + ", ");                //Write the number of needed classes completed
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
