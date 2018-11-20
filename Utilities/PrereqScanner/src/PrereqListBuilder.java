import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class PrereqListBuilder {

    File inFile = new File("filteredCSV.txt");

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
                scan.useDelimiter("\\n|;");                     //delimeter sperating the name from prereqs
                input = scan.next();                            //Store the next token

                while(!lineDone){


                    /*If there is no prereqs*/
                    if(input == "NONE"){
                        br.write(input + "]");
                        break;
                    }
                    else if(isInteger(input)){

                    }

                }


            }

        }
        catch(IOException e){
            System.out.println("Could not make prereqList.txt");
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
