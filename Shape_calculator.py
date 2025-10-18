import math
from rich.console import Console
import os
import time

def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")
clear_screen()

console = Console()

clear_screen()

class Shape:
  def display_info(self):
    return f"This is a shape. \n{"\u2024" * 100}"
  
  def area(self):
    return 0
  
class Three_dim_shape:
  def display_info(self):
    return f"This is a 3D Shape. \n{"\u2024" * 100}"
  
  def area(self):
    return 0
  
class Square(Shape):
  def __init__(self, length):
    self.length = length

  def display_info(self):
    return f"Square with: \nLength: {self.length}, \nWidth: {self.length}. \n{"\u2024" * 100}"
  
  def area(self):
    return f"The area is: \n{self.length ** 2}. \n{"\u2024" * 100}"
  
  def perimeter(self):
    return f"The perimeter of the square is: \n{self.length * 4}. \n{"\u2024" * 100}"
  
  def diagonal(self):
    return f"The length of one side is: \n{math.sqrt(2) * self.length}."

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
    if self.radius <= 0:
      raise ValueError("Measurment given must be greater than 0.")
  def display_info(self):
    return f"Circle with: \nRadius: {self.radius}, \n Diameter: {self.radius * 2}. \n{"\u2024" * 100}"
  def area(self):
    return f"The area of the circle is: \n{math.pi * self.radius ** 2}. \n{"\u2024" * 100}"
  def circumference(self):
    return f"The circumference of the circle is: \n{2 * (math.pi * self.radius)}. \n{"\u2024" * 100}"
class Rectangle(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width
    if self.length <= 0 or self.width <= 0:
      raise ValueError("Measurments given must be greater than 0.")
  def display_info(self):
    return f"Rectangle with: \nLength: {self.length}, \nWidth: {self.width}. \n{"\u2024" * 100}"
  def area(self):
    return f"The area is: \n{self.length * self.width}. \n{"\u2024" * 100}"
  def perimeter(self):
    return f"The perimeter of the rectangle is: \n{2 * (self.length + self.width)}. \n{"\u2024" * 100}"
  def diagonal(self):
    return f"The diagonal of the rectangle is: \n{math.sqrt(self.width ** 2 * self.length ** 2)}."
class Triangle(Shape):
  def __init__(self, base, height):
    self.base = base
    self.height = height
    if self.base <= 0 or self.height <= 0:
      raise ValueError("Measurments given must be greater than 0.")
  def display_info(self):
    return f"Triangle with: \nBase: {self.base}, \nHeight: {self.height}. \n{"\u2024" * 100}"
  def area(self):
    return f"The area of the triangle is: \n{self.base * self.height / 2}. \n{"\u2024" * 100}"
  def perimeter(self, a: float, b: float, c: float):
    if a + b <= c or a + c <= b or b + c <= a:
      raise ValueError(f"The sides provided does not create a valid triangle. \n{"\u2024" * 100}")
    return f"The perimeter of the triangle is: \n{a + b + c}. \n{"\u2024" * 100}"
class Cube(Three_dim_shape):
  def __init__(self, length):
    self.length = length
    if self.length <= 0:
      raise ValueError("Measurment given must be greater than 0.")
  def display_info(self):
    return f"Cube with: \nLength: {self.length}, \nWidth: {self.length}, \nHeight: {self.length}. \n{"\u2024" * 100}"
  def volume(self):
    return f"The volume of the cube is: \n{self.length ** 3}. \n{"\u2024" * 100}"
  def surface_area(self):
    return f"The surface area of the cube is: \n{6 * (self.length ** 2)}. \n{"\u2024" * 100}"
  def perimeter(self):
    return f"The perimeter of the cube is: \n{self.length * 12}. \n{"\u2024" * 100}"
  def diagonal(self):
    return f"The diagonal of the cube is: \n{math.sqrt(3) * self.length}. \n{"\u2024" * 100}"
class Sphere(Three_dim_shape):
  def __init__(self, radius):
    self.radius = radius
    if self.radius <= 0:
      raise ValueError("Measurment given must me greater than 0.")
  def display_info(self):
    return f"Sphere with: \nRadius: {self.radius}, \nDiameter: {self.radius * 2}. \n{"\u2024" * 100}"
  def volume(self):
    return f"The volume of the sphere is: \n{4 / 3 * math.pi * self.radius ** 3}. \n{"\u2024" * 100}"
  def surface_area(self):
    return f"The surface area of the sphere is: \n{4 * math.pi * (self.radius ** 2)}. \n{"\u2024" * 100}"
class Rectangular_prism(Three_dim_shape):
  def __init__(self, length, width, height):
    self.length = length
    self.width = width
    self.height = height
    if self.length <= 0 or self.width <= 0 or self.height <= 0:
      raise ValueError("Measurments given must be greater than 0.")
  def display_info(self):
    return f"Rectangular prism with: \nLength: {self.length}, \nWidth: {self.width}, \nHeight: {self.height}. \n{"\u2024" * 100}"
  def volume(self):
    return f"The volume of the rectangular prism is: \n{self.length * self.width * self.height}. \n{"\u2024" * 100}"
  def surface_area(self):
    return f"The surface area of the rectangular prism is: \n{2 * (self.width * self.length + self.height * self.length + self.height * self.width)}. \n{"\u2024" * 100}"
  def space_diagonal(self):
    return f"The space diagonal of the rectangular prism is: \n{math.sqrt(self.length ** 2 + self.width ** 2 or self.height ** 2)}. \n{"\u2024" * 100}"
  def perimeter(self):
    return f"The perimeter of the rectangular prism is: \n{(self.length * 4) + (self.width * 4) + (self.height * 4)}. \n{"\u2024" * 100}"
class Triangular_prism(Three_dim_shape):
  def __init__(self, a, b, c, h):
    self.a = a
    self.b = b
    self.c = c
    self.h = h
    
    if self.a <= 0 or self.b <= 0 or self.c <= 0 or self.h <= 0:
      raise ValueError(f"All parameters must be greater than 0. \n{"\u2024" * 100}")
    
    elif self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
      raise ValueError(f"The measurements given cannot create a triangular prism. \n{"\u2024" * 100}")
  
  def display_info(self):
    return f"Triangular prism with: \nFirst base height: {self.a}, \nSecond base height: {self.b}, \nThird base height: {self.c}, \nHeight: {self.h}. \n{"\u2024" * 100}"
  
  def volume(self):
    return f"The volume of the Triangular prism is: \n{0.50 * self.h * math.sqrt(-(self.a) ** 4 + 2 * (self.a * self.b) ** 2 + 2 * (self.a * self.c) ** 2 - self.b ** 4 + 2 * (self.b * self.c) ** 2 - self.c ** 4)}. \n{"\u2024" * 100}"
  
  def lateral_surface_area(self):
    return f"The lateral surface area of the Triangular prism is {(self.a + self.b + self.c) * self.h}. \n{"-" * 100}"
  
  def surface_area(self):
    d = (self.a + self.b + self.c) / 2
    lateral = (self.a + self.b + self.c) * self.h
    return f"The surface area of the Triangular prism is: \n{lateral + (2 * math.sqrt((d) * (d - self.a) * (d - self.b) * (d - self.c)))}. \n{"-" * 100}"
  
  def base_area(self):
    return f"The base area of the Triangular prism is {1/4 * math.sqrt(-self.a ** 4 + 2 * (self.a + self.b) ** 2 + 2 * (self.a + self.c) ** 2 - self.b ** 4 + 2 * (self.b + self.c) ** 2 - self.c ** 4)}. \n{"\u2024" * 100}"

  def perimeter(self):
    return f"The perimeter of the Triangular prism is {(self.a * 2) + (self.b * 2) + (self.c * 2) + (self.h * 3)}. \n{"\u2024" * 100}"
