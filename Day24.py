class Person:
    university_name = "CODEGNAN"
    def __init__(self, name, age, education_background, gender, department):
        self.name = name
        self.age = age
        self.education_background = education_background
        self.gender = gender
        self.department = department
    def display(self):
        print(f"University Name      : {Person.university_name}")
        print(f"Name                 : {self.name}")
        print(f"Age                  : {self.age}")
        print(f"Education Background : {self.education_background}")
        print(f"Gender               : {self.gender}")
        print(f"Department           : {self.department}")


class Student(Person):
    student_count = 0
    def __init__(self, name, age, education_background, gender,department, student_id, course, year):
        super().__init__(name, age, education_background, gender, department)
        self.student_id = student_id
        self.course = course
        self.year = year
        Student.student_count += 1
    def display_info(self):
        print("\n Student Details")
        self.display()
        print(f"Student ID  : {self.student_id}")
        print(f"Course  : {self.course}")
        print(f"Year    : {self.year}")


class Faculty(Person):
    faculty_count = 0
    def __init__(self, name, age, education_background, gender,department, faculty_id, designation):
        super().__init__(name, age, education_background, gender, department)
        self.faculty_id = faculty_id
        self.designation = designation
        Faculty.faculty_count += 1
    def display_info(self):
        print("\n Faculty Details ")
        self.display()
        print(f"Faculty ID  : {self.faculty_id}")
        print(f"Designation  : {self.designation}")

s1 = Student("Badrinadh Nandigam", 22, "Intermediate MPC", "Male","CSE", "101", "Python Full Stack", "4th Year")
f1 = Faculty("Bhanu Teja Garikapati", 30, "M.Tech", "Male","CSE", "F001", "Trainer")
f2 = Faculty("Naveen Kumar", 31, "M.Tech", "Male", "CSE", "F002", "Trainer")

s1.display_info()
f1.display_info()
f2.display_info()
print(f"\nTotal Students  : {Student.student_count}")
print(f"Total Faculties : {Faculty.faculty_count}")
