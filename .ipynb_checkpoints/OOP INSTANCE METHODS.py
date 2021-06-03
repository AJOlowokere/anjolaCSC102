#Instance Method Example

# class Student:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def avg(self):
#         return (self.a + self.b)/2

# s1 = Student(10, 20)
# print(s1.avg())

#Class Method Implementation
class Student:
    name =  'Student'
    def __init__(self, a, b):
        self.a = a
        self.b = b

# @classmethod
# def into(cls):
#     return cls.name

# print(Student.info())

@staticmethod
def info():
    return "This is a static method"
print(Student.info())