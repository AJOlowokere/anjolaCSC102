class Student:
     studentLevel = 'first year computer science 2020/2021 session'
     studentCounter = 0
     registeredCourse = 'CSC102'
     def __init__(self, thename, thematricno, thesex, thehostelname, theage, thecsc102examscore):
         self.name = thename
         self.matricno = thematricno
         self.sex = thesex
         self.hostelname = thehostelname
         self.age = theage
         self.csc102examscore = thecsc102examscore
         Student.studentCounter = Student.studentCounter +1


     def getName(self):
         return  self.name

     def setName(self, thenewName):
         self.name = thenewName

     def agedeterminer(self):
         if self.age > 16:
            return "Student is above 16 "
         else: 
            return "Student is 16 or below"

     def ToCarryoverOrNot(self):
         if self.csc102examscore < 45:
             print("Lmao. Try again next year")


     @classmethod
     def course(cls):
         print(f'Registered course is {Student.registeredCourse}')

     @classmethod
     def counter(cls):
         print(Student.studentCounter)

     @staticmethod
     def PAUNanthem():
        print('Pau, here we come, Pau, here we come ')

     @staticmethod
     def evenOrOdd(num):
        if num % 2 == 0 :
            print("Number is Even")
        else:
            print("Number is Odd")

studendt1 = Student('James Kaka', '021074', 'M', 'Faith', )
print(studendt1.getName())
studendt1.setName('James Gaga')
print(studendt1.getName())

Student.PAUNanthem()