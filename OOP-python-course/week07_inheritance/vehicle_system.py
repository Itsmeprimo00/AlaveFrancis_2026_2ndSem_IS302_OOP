class Vehicle_FGA:
    def __init__(self_FGA, brand_FGA, model_FGA):
        self_FGA.brand_FGA = brand_FGA
        self_FGA.model_FGA = model_FGA

class Car_FGA(Vehicle_FGA):
    def __init__(self_FGA, brand_FGA, model_FGA, year_FGA):
        super().__init__(brand_FGA, model_FGA)
        self_FGA.year_FGA = year_FGA

    def display_car_FGA(self_FGA):
        print(self_FGA.brand_FGA, self_FGA.model_FGA, self_FGA.year_FGA)

car1_FGA = Car_FGA("Toyota", "Corolla", 2022)
car1_FGA.display_car_FGA()

