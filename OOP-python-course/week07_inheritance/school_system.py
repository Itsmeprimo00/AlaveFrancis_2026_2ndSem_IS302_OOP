class Person_FGA:
    def __init__(self_FGA, name_FGA, age_FGA):
        self_FGA.name_FGA = name_FGA
        self_FGA.age_FGA = age_FGA

    def display_info_FGA(self_FGA):
        print("Name:", self_FGA.name_FGA)
        print("Age:", self_FGA.age_FGA)

class Student_FGA(Person_FGA):
    def __init__(self_FGA, name_FGA, age_FGA, course_FGA):
        super().__init__(name_FGA, age_FGA)
        self_FGA.course_FGA = course_FGA

    def display_info_FGA(self_FGA):
        super().display_info_FGA()
        print("Course:", self_FGA.course_FGA)

class Teacher_FGA(Person_FGA):
    def __init__(self_FGA, name_FGA, age_FGA, subject_FGA):
        super().__init__(name_FGA, age_FGA)
        self_FGA.subject_FGA = subject_FGA

    def display_info_FGA(self_FGA):
        super().display_info_FGA()
        print("Subject:", self_FGA.subject_FGA)

# Example usage
student_FGA = Student_FGA("Maria", 20, "BSIS")
teacher_FGA = Teacher_FGA("Mr. Smith", 45, "Mathematics")

print("Student Info:")
student_FGA.display_info_FGA()
print("\nTeacher Info:")
teacher_FGA.display_info_FGA()

