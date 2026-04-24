class Employee_FGA:
    def work_FGA(self_FGA):
        print("Employee performs tasks")

class Programmer_FGA(Employee_FGA):
    def work_FGA(self_FGA):
        print("Programmer writes code")

class Designer_FGA(Employee_FGA):
    def work_FGA(self_FGA):
        print("Designer creates UI designs")

employees_FGA = [Programmer_FGA(), Designer_FGA()]
for emp_FGA in employees_FGA:
    emp_FGA.work_FGA()

