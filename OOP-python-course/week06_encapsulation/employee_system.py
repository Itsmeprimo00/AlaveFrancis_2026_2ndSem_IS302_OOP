class Employee_FGA:
    def __init__(self_FGA, name_FGA):
        self_FGA.__name_FGA = name_FGA
        self_FGA.__salary_FGA = 0

    def set_salary_FGA(self_FGA, salary_FGA):
        if salary_FGA > 0:
            self_FGA.__salary_FGA = salary_FGA

    def get_salary_FGA(self_FGA):
        return self_FGA.__salary_FGA

emp_FGA = Employee_FGA("Ana")
emp_FGA.set_salary_FGA(30000)
print("Salary:", emp_FGA.get_salary_FGA())

