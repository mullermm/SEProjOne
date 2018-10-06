package scanner;
import java.io.File;

/**
 * @author Maxwell Herron
 * This will read the .txt file of all the classes, organize them into Course objects,
 * and feed them into into a javascript file
 */


public class Driver
{
    public static void main(String[] args)
    {
        TextScanner scanner = new TextScanner();
        File fileOne = new File("courses.txt");
        File fileTwo = new File("courses.csv");
        scanner.scan(fileOne);

    }

}
