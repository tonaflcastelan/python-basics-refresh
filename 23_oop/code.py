# OOP
# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

# def average(sequence):
#     return sum(sequence) / len(sequence)

# print(average(student["grades"]))


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Ceci", (89, 90, 93, 66, 90))
student2 = Student("Tona", (89, 90, 93, 66, 34))
print(student.name)
# print(student.grades)
print(student.average())
print(student2.average())