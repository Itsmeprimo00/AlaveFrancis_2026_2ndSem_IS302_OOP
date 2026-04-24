class Dog_FGA:
    def speak_FGA(self_FGA):
        print("Dog barks")

class Cat_FGA:
    def speak_FGA(self_FGA):
        print("Cat meows")

animals_FGA = [Dog_FGA(), Cat_FGA()]
for animal_FGA in animals_FGA:
    animal_FGA.speak_FGA()

