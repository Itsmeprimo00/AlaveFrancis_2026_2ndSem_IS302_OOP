class Student:
    def __init__(self, name, student_id, course):
        self.name_FGA = name
        self.student_id_FGA = student_id
        self.course_FGA = course

    def display_student(self):
        print("Name:", self.name_FGA)
        print("Student ID:", self.student_FGA)
        print("Course:", self.course_FGA)


student1 = Student("Maria", "2023-001", "BSIS")
student1.display_student()


