class ConLib:    
    def __init__(self, transcript):
        self.transcript = transcript
        self.totalclasses = 0
        self.completeclasses = 0
#This is for sections where all classes must be completed.
    def do_all(self, section):
        todo = [x for x in section if x not in self.transcript]
        done = [x for x in section if x in self.transcript]
        if len(todo) == 0:
            self.totalclasses = self.totalclasses + len(section)
            self.completeclasses = self.completeclasses + len(section)
        else:
            self.totalclasses = self.totalclasses + len(section)
            self.completeclasses = self.completeclasses + len(done)
#This is for sections where a specific number of classes must be done.
    def do_some(self, numofclass, section):
        todo = [x for x in section if x not in self.transcript]
        done = [x for x in section if x in self.transcript]
        if numofclass <= (len(section) - len(todo)):
            self.totalclasses = self.totalclasses + numofclass
            self.completeclasses = self.completeclasses + numofclass
        else:
            self.totalclasses = self.totalclasses + numofclass
            self.completeclasses = self.completeclasses + len(done)
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
        else:
            self.totalclasses = self.totalclasses + numofclass
            self.completeclasses = self.completeclasses + len(done)
    
    def completion_percent(self):
        percent = self.completeclasses/self.totalclasses
        return (percent * 100)