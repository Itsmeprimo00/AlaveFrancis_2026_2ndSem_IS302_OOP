class Student_FGA:
    def __init__(self_FGA, name_FGA, student_id_FGA, gpa_FGA):
        self_FGA.__name_FGA = name_FGA
        self_FGA.__student_id_FGA = student_id_FGA
        self_FGA.__gpa_FGA = gpa_FGA

    def get_student_info_FGA(self_FGA):
        print("Name:", self_FGA.__name_FGA)
        print("Student ID:", self_FGA.__student_id_FGA)
        print("GPA:", self_FGA.__gpa_FGA)

student1_FGA = Student_FGA("Juan", "2023-001", 1.75)
student1_FGA.get_student_info_FGA()

