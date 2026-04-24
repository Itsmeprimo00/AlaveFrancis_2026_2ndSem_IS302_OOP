class Car:
    def __init__(self, brand, model, year):
        self.brand_FGA = brand
        self.model_FGA = model
        self.year_FGA = year

    def display_car(self):
        print(self.brand_FGA, self.model_FGA, self.year_FGA)


car1 = Car("Toyota", "Corolla", 2020)
car1.display_car()


