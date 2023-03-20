class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = int(age)
        self.score = int(score)
 
    def getGrade(self):
        if self.score < 30:
            return 'F'
        elif self.score < 40:
            return 'E'
        elif self.score < 60:
            return 'C'
        elif self.score < 70:
            return 'B'
        else:
            return 'A'


f = open("name.txt", "r")
names = f.readlines()

from random import randrange
students =[]

for name in names:
    # print(name)
    students.append(Student(name.strip("\n"), randrange(16, 19), randrange(20, 100)))


for student in students:
    print(f"Student name = {student.name}, Age = {student.age}, Score = {student.score}, and Grade = {student.getGrade()}")
