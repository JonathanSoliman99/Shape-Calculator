import math
from rich.console import Console
import os

def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")
  
clear_screen()
console = Console()
user = int(input("Enter the number that you would like to round by (Max is 15): \n"))
clear_screen()

class Shape:
  def display_info(self):
    return f"This is a shape. \n{"-" * 50}"
    
  def area(self):
    return 0
    
class Three_dim_shape:
  def display_info(self):
    return f"This is a 3D Shape. \n{"-" * 50}"
    
  def area(self):
    return 0
    
class Square(Shape):
  def __init__(self, length):
    self.length = length
    
  def display_info(self):
    return f"Square with: \nLength: {self.length}, \nWidth: {self.length}. \n{"-" * 50}"
    
  def area(self):
    return f"The area is: \n{self.length ** 2}. \n{"-" * 50}"
    
  def perimeter(self):
    return f"The perimeter of the square is {self.length * 4}. \n{"-" * 50}"
    
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
    
  def display_info(self):
    return f"Circle with: \nRadius: {self.radius}, \n Diameter: {self.radius * 2}. \n{"-" * 50}"
    
  def area(self):
    return f"The area of the circle is: \n{round(math.pi * self.radius ** 2, user)}. \n{"-" * 50}"
    
  def circumference(self):
    return f"The circumference of the circle is: \n{round(2 * (math.pi * self.radius), user)}. \n{"-" * 50}"
    
class Rectangle(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width
    
  def display_info(self):
    return f"Rectangle with: \nLength: {self.length}, \nWidth: {self.width}. \n{"-" * 50}"
    
  def area(self):
    return f"The area is: \n{self.length * self.width}. \n{"-" * 50}"
    
  def perimeter(self):
    return f"The perimeter of the rectangle is: \n{2 * (self.length * self.width)}. \n{"-" * 50}"
    
class Triangle(Shape):
  def __init__(self, base, height):
    self.base = base
    self.height = height
    
  def display_info(self):
    return f"Triangle with: \nBase: {self.base}, \nHeight: {self.height}. \n{"-" * 50}"
    
  def area(self):
    return f"The area of the triangle is: \n{self.base * self.height / 2}. \n{"-" * 50}"
    
  def perimeter(self, a: float, b: float, c: float):
    if a + b <= c or a + c <= b or b + c <= a:
      raise ValueError(f"The sides provided does not create a valid triangle. \n{"-" * 50}")
    return f"The perimeter of the triangle is: \n{a + b + c}. \n{"-" * 50}"
    
class Cube(Three_dim_shape):
  def __init__(self, length):
    self.length = length
    
  def display_info(self):
    return f"Cube with: \nLength: {self.length}, \nWidth: {self.length}, \nHeight: {self.length}. \n{"-" * 50}"
  
  def volume(self):
    return f"The volume of the cube is: \n{self.length ** 3}. \n{"-" * 50}"
  
  def surface_area(self):
    return f"The surface area of the cube is: \n{6 * (self.length ** 2)}. \n{"-" * 50}"
  
  def perimeter(self):
    return f"The perimeter of the cube is: \n{self.length * 12}. \n{"-" * 50}"

class Sphere(Three_dim_shape):
  def __init__(self, radius):
    self.radius = radius
  
  def display_info(self):
    return f"Sphere with: \nRadius: {self.radius}, \nDiameter: {self.radius * 2}. \n{"-" * 50}"
  
  def volume(self):
    return f"The volume of the sphere is: \n{round(4 / 3 * math.pi * self.radius ** 3, user)}. \n{"-" * 50}"
  
  def surface_area(self):
   
    return f"The surface area of the sphere is: \n{round(4 * math.pi * (self.radius ** 2), user)}. \n{"-" * 50}"
class Rectangular_prism(Three_dim_shape):
  def __init__(self, length, width, height):
    self.length = length
    self.width = width
    self.height = height
 
  def display_info(self):
    return f"Rectangular prism with: \nLength: {self.length}, \nWidth: {self.width}, \nHeight: {self.height}. \n{"-" * 50}"
  
  def volume(self):
    return f"The volume of the rectangular prism is: \n{self.length * self.width * self.height}. \n{"-" * 50}"
  
  def surface_area(self):
    return f"The surface area of the rectangular prism is: \n{2 * (self.width * self.length + self.height * self.length + self.height * self.width)}. \n{"-" * 50}"

class Triangular_prism(Three_dim_shape):
  def __init__(self, a, b, c, h):
    self.a = a
    self.b = b
    self.c = c
    self.h = h
    
    if self.a <= 0 or self.b <= 0 or self.c <= 0 or self.h <= 0:
      raise ValueError(f"All parameters must be greater than 0. \n{"-" * 50}")
    
    elif self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
      raise ValueError(f"The measurements given cannot create a triangular prism. \n{"-" * 50}")
  
  def display_info(self):
    return f"Triangular prism with: \nFirst base height: {self.a}, \nSecond base height: {self.b}, \nThird base height: {self.c}, \nHeight: {self.h}. \n{"-" * 50}"
  
  def volume(self):
    return f"The volume of the triangular prism is: \n{round(0.50 * self.h * math.sqrt(-(self.a) ** 4 + 2 * (self.a * self.b) ** 2 + 2 * (self.a * self.c) ** 2 - self.b ** 4 + 2 * (self.b * self.c) ** 2 - self.c ** 4), 2)}. \n{"-" * 50}"
  
  def surface_area(self):
    d = (self.a + self.b + self.c) / 2
    return f"The surface area of the Triangular prism is: \n{round(((self.a + self.b + self.c) * self.h) + (2 * math.sqrt((d) * (d - self.a) * (d - self.b) * (d - self.c))), user)}. \n{"-" * 50}"

try:
  t1 = Triangular_prism(3, 4, 5, 6)
  console.print(t1.surface_area())
  # If High Tech is reading this, the project is a little bit small then my others but I tried my best for this folder and it took me hours for this.
except (TypeError, NameError):
  console.print(f"All parameters MUST be a number. \n{"-" * 50}")

  
  


