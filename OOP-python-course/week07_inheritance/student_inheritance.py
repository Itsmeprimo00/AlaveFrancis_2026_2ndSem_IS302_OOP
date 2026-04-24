class Person_FGA:
    def __init__(self_FGA, name_FGA, age_FGA):
        self_FGA.name_FGA = name_FGA
        self_FGA.age_FGA = age_FGA

class Student_FGA(Person_FGA):
    def __init__(self_FGA, name_FGA, age_FGA, course_FGA):
        super().__init__(name_FGA, age_FGA)
        self_FGA.course_FGA = course_FGA

    def display_student_FGA(self_FGA):
        print("Name:", self_FGA.name_FGA)
        print("Age:", self_FGA.age_FGA)
        print("Course:", self_FGA.course_FGA)

student1_FGA = Student_FGA("Maria", 20, "BSIS")
student1_FGA.display_student_FGA()

