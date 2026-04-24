import math

class Shape_FGA:
    def area_FGA(self_FGA):
        pass  # Placeholder for polymorphism

class Rectangle_FGA(Shape_FGA):
    def __init__(self_FGA, width_FGA, height_FGA):
        self_FGA.width_FGA = width_FGA
        self_FGA.height_FGA = height_FGA

    def area_FGA(self_FGA):
        return self_FGA.width_FGA * self_FGA.height_FGA

class Circle_FGA(Shape_FGA):
    def __init__(self_FGA, radius_FGA):
        self_FGA.radius_FGA = radius_FGA

    def area_FGA(self_FGA):
        return math.pi * self_FGA.radius_FGA ** 2

class Triangle_FGA(Shape_FGA):
    def __init__(self_FGA, base_FGA, height_FGA):
        self_FGA.base_FGA = base_FGA
        self_FGA.height_FGA = height_FGA

    def area_FGA(self_FGA):
        return 0.5 * self_FGA.base_FGA * self_FGA.height_FGA

# Example usage
rectangle_FGA = Rectangle_FGA(10, 5)
circle_FGA = Circle_FGA(5)
triangle_FGA = Triangle_FGA(8, 6)

print(f"Rectangle Area: {rectangle_FGA.area_FGA()}")
print(f"Circle Area: {circle_FGA.area_FGA():.1f}")
print(f"Triangle Area: {triangle_FGA.area_FGA()}")


