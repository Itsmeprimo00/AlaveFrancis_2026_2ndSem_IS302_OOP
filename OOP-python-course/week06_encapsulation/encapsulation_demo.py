class Person_FGA:
    def __init__(self_FGA, name_FGA, age_FGA):
        self_FGA.__name_FGA = name_FGA
        self_FGA.__age_FGA = age_FGA

    def get_name_FGA(self_FGA):
        return self_FGA.__name_FGA

    def get_age_FGA(self_FGA):
        return self_FGA.__age_FGA

p1_FGA = Person_FGA("Maria", 20)
print("Name:", p1_FGA.get_name_FGA())
print("Age:", p1_FGA.get_age_FGA())

