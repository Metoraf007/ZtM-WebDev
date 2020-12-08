
class Classroom:
    def __init__(self ,classNum, capacity ,isUseable):
        self.classNum = classNum
        self.capacity = capacity
        self.isUseable = isUseable

    def toString(self):
        if self.isUseable == True:
            self.isUseable = "useable"
        else :
            self.isUseable = "anuseable"
        return "class Number :" + str(self.classNum) + " can contain " + str(self.capacity) + " people max, class is " + str(self.isUseable)

class Course:
    def __init__(self , courseName, dayOfWeek, startHour, numOfStudents, classNum, capacity, isUseable):
        self.courseName = courseName
        if dayOfWeek >6 or dayOfWeek < 1 :
            self.dayOfWeek = -1
        else:
            self.dayOfWeek = dayOfWeek
        if (startHour > 18) or (startHour < 8) :
            self.startHour = -1
        else:
            self.startHour = startHour

        if numOfStudents <= 5:
            self.numOfStudents = -1
        else:
            self.numOfStudents = numOfStudents
        self.courseClassRoom = Classroom(classNum ,capacity ,isUseable)

 ####ג##
    def setClassRoom(self,courseClassRoom):
        self.courseClassRoom = courseClassRoom
        if self.courseClassRoom.isUseable == False :
            self.courseClassRoom ="None"
        if self.courseClassRoom.capacity < self.numOfStudents :
            self.courseClassRoom = "None"

class College(Classroom):
    def __init__(self, courses):
       self.courses = courses

    # def setClassForCourse(self , courseName, room):

####ה##
    def earliestCourse(self, day):
        theErliestCourse = self.courses[0]
        ##הגדרת הקורס הראשון ברשימה לקורס המוקדם ביותר כהתחלה
        for i in range(len(self.courses):
            if self.courses[i].dayOfWeek == day:
                if self.courses[i].startHour < theErliestCourse.startHour:
                    theErliestCourse = self.courses[i]
        #מעבר על רשימת הקורסים ובדיקה האם מתקיימים ביום שהפונקתיה קיבלה כפרמטר###
        if theErliestCourse == self.courses[0]:
        ##אם הקורס הראשון במערך נשאר כקורס המוקדם ביותר- בדיקה האם בכלל מתקיים ביום שהתקבל כפרמטר
            if self.courses[0].dayOfWeek != day:
                return ""
        return theErliestCourse.courseName
####ו##
    def howManyAfter12(self, inputList):
        after12Courses = []
        numOfCourses = len(self.courses)
        i = 0

        if len(inputList) == 0 or numOfCourses == 0:
            return after12Courses
        else:
            if self.courses[i].startHour => 12:
                after12Courses = self.courses[i]
                shortList = self.courses[1:]
                i = i + 1
                
                howManyAfter12(shortList)
                
                

####ז##
    def nextCourse(self):
        continue
