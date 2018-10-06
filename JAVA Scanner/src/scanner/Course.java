package scanner;
/**
 * @author Maxwell Herron
 * This class embodies the course object, which will hold all the information of each course
 */
public class Course
{
    String name;
    String description;
    double creditHours;
    int courseLevel;
    String department;
    String prerequisites;

    /**
     * This is the constructor method for the Course object
     * @param inName
     * @param inCreditHours
     * @param inCourseLevel
     * @param inDepartment
     * @param inPrerequisites
     */
    public Course(String inName, double inCreditHours, String inDescription, int inCourseLevel, String inDepartment, String inPrerequisites)
    {
        this.name = inName;
        this.creditHours = inCreditHours;
        this.description = inDescription;
        this.courseLevel = inCourseLevel;
        this.department = inDepartment;
        this.prerequisites = inPrerequisites;
    }

    public Course() { }

/********************************* GETTERS AND SETTERS **************************************************/
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getCreditHours() {
        return creditHours;
    }

    public void setCreditHours(int creditHours) {
        this.creditHours = creditHours;
    }

    public String getDescription() { return description; }

    public void setDescription(String description) { this.description = description; }

    public int getCourseLevel() {
        return courseLevel;
    }

    public void setCourseLevel(int courseLevel) {
        this.courseLevel = courseLevel;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public String getPrerequisites() {
        return prerequisites;
    }

    public void setPrerequisites(String prerequisites) {
        this.prerequisites = prerequisites;
    }
/*******************************************************************************************************/

    @Override
    public String toString() {
        return "Course{" +
                "name='" + name + '\'' +
                ", description='" + description + '\'' +
                ", creditHours=" + creditHours +
                ", courseLevel=" + courseLevel +
                ", department='" + department + '\'' +
                ", prerequisites='" + prerequisites + '\'' +
                '}';
    }
}
