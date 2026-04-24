class Employee_FGA:
    def __init__(self_FGA, name_FGA, salary_FGA):
        self_FGA.name_FGA = name_FGA
        self_FGA.salary_FGA = salary_FGA

class Manager_FGA(Employee_FGA):
    def __init__(self_FGA, name_FGA, salary_FGA, department_FGA):
        super().__init__(name_FGA, salary_FGA)
        self_FGA.department_FGA = department_FGA

    def display_manager_FGA(self_FGA):
        print("Name:", self_FGA.name_FGA)
        print("Salary:", self_FGA.salary_FGA)
        print("Department:", self_FGA.department_FGA)

manager1_FGA = Manager_FGA("John", 50000, "IT")
manager1_FGA.display_manager_FGA()

