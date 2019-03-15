class Student:
    def __init__(self, name, studentNumber, numberOfcourses):
        self.name = name
        self.studentNumber = studentNumber
        self.numberOfcourses = numberOfcourses

    def setName(self, name):
        self.name = name

    def setNumber(self, studentNumber):
        self.studentNumber = studentNumber

    def setCourses(self, numberOfcourses):
        self.numberOfcourses = numberOfcourses

    def getName(self):
        return self.name

    def getNumber(self):
        return self.studentNumber

    def getcourses(self):
        return self.numberOfcourses


#tesing Student class
def main():
    #request the corresponding data from input
    name = input("Enter name: ")
    studentNumber = input("Enter studentNumber: ")
    numberOfcourses = int(input("Enter studentNumber of numberOfcourses in this semester: "))

    #create a Student object.
    student = Student(name, studentNumber, numberOfcourses)

    # invoke a method to change the value of one of its attributes of the object
    # Changing the studentNumber of numberOfcourses by 10
    #Changing name to jerry
    student.setCourses(10)
    student.setName("Jerry")

    #invoke a method to that displays the value of each attribute
    print("Name:",student.getName())
    print("studentNumber:",student.getNumber())
    print("studentNumber of numberOfcourses:",student.getcourses())


if __name__ == '__main__':
main()
