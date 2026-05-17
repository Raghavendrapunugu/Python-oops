"""
A class for representing a circle
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius 
    
    def display_circumference(self):
        return f"Circumference: {2 * 3.14 * self.radius} units"
    
    def display_area(self):
        return f"Area: {3.14 * self.radius ** 2} units"

circle1 = Circle(2)
print(circle1.display_circumference())
print(circle1.display_area())