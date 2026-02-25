class School:
    students = []
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def add_student(self, student):
        self.students.append(student)
    def remove_student(students, i):
        removed = students.pop(i)
    def show_students(self):
        for student in self.students:
            print(student)


class Student:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
    def get_info(self):
        return f"name: {self.name}\nlast name: {self.last_name}"

school = School("Skola #1", "Qucha1 nomeri2")
student1 = Student("Ani","Beridze", 14)
student2 = Student("Gio", "Begashvili", 16)
student3 = Student("Nia", "Kapanadze", 13)
school.add_student(student1)
school.add_student(student2)
school.add_student(student3)
print(School)