<<<<<<< HEAD
=======
def build_list(numberofcourses, courses):
    if numberofcourses == 0:
        return "|".join(courses)
    else:
        string = "|".join(courses)
        return str(numberofcourses) + "|" + string

>>>>>>> Nghia
class ConLib:    
    def __init__(self, transcript):
        self.transcript = transcript
        self.totalclasses = 0
        self.completeclasses = 0
<<<<<<< HEAD
=======
        self.todoclasses = []
        self.doneclasses = []
        self.schedual = []

    def build_list(self,numberofcourses, courses):
        if numberofcourses == 0:
            return "|".join(courses)
        else:
            string = "|".join(courses)
            return str(numberofcourses) + "|" + string


>>>>>>> Nghia
#This is for sections where all classes must be completed.
    def do_all(self, section):
        todo = [x for x in section if x not in self.transcript]
        done = [x for x in section if x in self.transcript]
        if len(todo) == 0:
            self.totalclasses = self.totalclasses + len(section)
            self.completeclasses = self.completeclasses + len(section)
<<<<<<< HEAD
        else:
            self.totalclasses = self.totalclasses + len(section)
            self.completeclasses = self.completeclasses + len(done)
=======
            self.doneclasses = self.doneclasses + done
        else:
            self.totalclasses = self.totalclasses + len(section)
            self.completeclasses = self.completeclasses + len(done)
            self.todoclasses = self.todoclasses + todo
            self.schedual.append(build_list(0,todo))
>>>>>>> Nghia
#This is for sections where a specific number of classes must be done.
    def do_some(self, numofclass, section):
        todo = [x for x in section if x not in self.transcript]
        done = [x for x in section if x in self.transcript]
        if numofclass <= (len(section) - len(todo)):
            self.totalclasses = self.totalclasses + numofclass
            self.completeclasses = self.completeclasses + numofclass
<<<<<<< HEAD
        else:
            self.totalclasses = self.totalclasses + numofclass
            self.completeclasses = self.completeclasses + len(done)
=======
            self.doneclasses = self.doneclasses + done
        else:
            self.totalclasses = self.totalclasses + numofclass
            self.completeclasses = self.completeclasses + len(done)
            self.todoclasses = self.todoclasses + todo
            self.schedual.append(build_list(numofclass,todo))
>>>>>>> Nghia
#Same as above but with a checker to make sure the courses taken are upper div
    def do_some_upper(self, numofclass, numofdiv, section):
        todo = [x for x in section if x not in self.transcript]
        done = [x for x in section if x in self.transcript]
        count = 0
        for course in done:
            if int(course[-3:]) >= 300:
                count = count + 1
        if numofclass <= (len(section) - len(todo)) and count >= numofdiv:
            self.totalclasses = self.totalclasses + numofclass
            self.completeclasses = self.completeclasses + numofclass
<<<<<<< HEAD
        else:
            self.totalclasses = self.totalclasses + numofclass
            self.completeclasses = self.completeclasses + len(done)
    
    def completion_percent(self):
        percent = self.completeclasses/self.totalclasses
        return (percent * 100)
=======
            self.doneclasses = self.doneclasses + done
        else:
            self.totalclasses = self.totalclasses + numofclass
            self.completeclasses = self.completeclasses + len(done)
            self.todoclasses = self.todoclasses + todo
            self.schedual.append(build_list(numofclass,todo))
    def completion_percent(self):
        percent = self.completeclasses/self.totalclasses
        return (percent * 100)
    
    def get_todo_classes(self):
        return self.todoclasses

    def get_done_classes(self):
        return self.doneclasses

    def build_course_list_csv(self):
        file = open("remainingcoursesneeded.txt","w")
        file.write(",".join(self.schedual)) 
        file.close
>>>>>>> Nghia
