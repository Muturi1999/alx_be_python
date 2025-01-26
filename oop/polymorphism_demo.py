#!/usr/bin/env python3
# polymorphism_demo.py

import math

class Shape:
    """Base class for shapes."""
    def area(self):
        raise NotImplementedError("Derived classes must override the area method")


class Rectangle(Shape):
    """Derived class for a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    """Derived class for a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

