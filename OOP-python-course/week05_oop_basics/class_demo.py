class Person:
    def __init__(self, name, age):
        self.name_FGA = name
        self.age_FGA = age

    def display_info(self):
        print("Name:", self.name_FGA)
        print("Age:", self.age_FGA)


p1 = Person("Juan", 20)
p1.display_info()


