#Author: Nawal Ahmed
#Concepts of Programming Languages
#Assignment 3

#initialize a class called Student
class Student:
    #defining a constructor
    def __init__(self, name, studentNumber, numberOfcourses):
        #the keyword self is similar to the keyboard this in Java
        #refers to an object the function is running on
        self.name = name
        self.studentNumber = studentNumber
        self.numberOfcourses = numberOfcourses

    #using setter like in Java
    def setName(self, name):
        self.name = name
    def setNumber(self, studentNumber):
        self.studentNumber = studentNumber
    def setCourses(self, numberOfcourses):
        self.numberOfcourses = numberOfcourses

    #using getter like in Java
    def getName(self):
        return self.name
    def getNumber(self):
        return self.studentNumber
    def getcourses(self):
        return self.numberOfcourses


#defining the main function
def main():
    #request the corresponding data from input
    name = input("Name: ")
    studentNumber = int(input("Student Number: "))
    numberOfcourses = int(input("Number of Courses: "))

    #object called student
    student = Student(name, studentNumber, numberOfcourses)

    #method that overrides the value of the attribute
    student.setName("John Smith (Override)") #name changes to John Smith

    #display attribute values
    print()
    print("Name:",student.getName())
    print("Student Number:",student.getNumber())
    print("Number of Courses:",student.getcourses())


#typical main function in python
if __name__ == '__main__':
    main()
