class Animal_FGA:
    def __init__(self_FGA, name_FGA):
        self_FGA.name_FGA = name_FGA

    def speak(self_FGA):
        print(self_FGA.name_FGA, "makes a sound")

class Dog_FGA(Animal_FGA):
    def bark(self_FGA):
        print(self_FGA.name_FGA, "barks")

dog1_FGA = Dog_FGA("Buddy")
dog1_FGA.speak()
dog1_FGA.bark()

