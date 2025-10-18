from Shape_calculator import *
import os
from rich.console import Console

os.system("cls" if os.name == "nt" else "clear")

console = Console()

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def main():

    first = input("Enter The Shape that you would like to measure: (type \"list\" if you would like a list of avaliable shapes.)\n").lower().strip()
    clear_screen()

    if first == "list":
        console.print(f"[yellow italic]Avaliable Shapes to measure:[/yellow italic] \n[bold green]Square[/bold green], \n[bold blue]Circle[/bold blue], \n[bold green]Rectangle[/bold green], \n[bold blue]Triangle[/bold blue], \n[bold purple]Cube[/bold purple], \n[bold magenta]Sphere[/bold magenta], \n[bold purple]Rectangular prism[/bold purple], \n[bold magenta]Triangular prism[/bold magenta]. \n[yellow italic]Press \"Enter\" to restart the calculator.[/yellow italic] \n{"\u2024" * 100}")
        input()
        console.print("Program ended. Please wait while this program restarts the calculator. Wait how are you reading this?")
        clear_screen()
        main2()

    elif first == "square":
        squar = input("Enter The height: ").strip()
        
        if isfloat(squar):
            clear_screen()
            square = Square(float(squar))
            m = input("Would you like to display info, print the area, print the diagonal, or print the perimeter?: ").lower().strip()

            if m == "display info":
                clear_screen()
                console.print(square.display_info())

            elif m == "area":
                clear_screen()
                console.print(square.area())

            elif m == "perimeter":
                clear_screen()
                console.print(square.perimeter())
            
            elif m == "diagonal":
                clear_screen()
                console.print(square.diagonal)

            else:
                raise TypeError("You can only write \"Display Info\", \"Area\", \"Diagonal\", or \"Perimeter\".")
        else:
            raise TypeError("You can only write a number.")
        
    elif first == "circle":
        circl = input("Enter the radius: ")

        if isfloat(circl):
            circle = Circle(float(circl))
            clear_screen()
            n = input("Would you like to display info, print the area, or print the circumference?: ").lower().strip()

            if n == "display info":
                clear_screen()
                console.print(circle.display_info())

            elif n == "area":
                clear_screen()
                console.print(circle.area())
            
            elif n == "circumference":
                clear_screen()
                console.print(circle.circumference())
            
            else:
                raise TypeError("You can only write \"Display Info\", \"Area\", or \"Circumference\".")
            
        else:
            raise TypeError("You can only write a number.")
        
    elif first == "rectangle":
        rec = input("Enter the length: ")
        clear_screen()
        rec1 = input("Enter the width: ")

        if isfloat(rec) and isfloat(rec1):
            rectangle = Rectangle(float(rec), float(rec1))
            clear_screen()
            n = input("Would you like to display info, print the area, print the perimeter, or print the diagonal?: ").lower().strip()

            if n == "display info":
                clear_screen()
                console.print(rectangle.display_info())

            elif n == "area":
                clear_screen()
                console.print(rectangle.area())
            
            elif n == "perimeter":
                clear_screen()
                console.print(rectangle.perimeter())
            
            elif n == "diagonal":
                clear_screen()
                console.print(rectangle.diagonal())
            
            else:
                raise TypeError("You can only write \"Display Info\", \"Area\", or \"Perimeter\", \"Diagonal\".")
            
        else:
            raise TypeError("You can only write a number.")
        
    elif first == "triangle":
        tri = input("Enter The base: ")
        clear_screen()
        tri1 = input("Enter the height")
        
        if isfloat(tri) and isfloat(tri1):
            clear_screen()
            triangle = Triangle(float(tri), float(tri1))
            m = input("Would you like to display info, print the area, or print the perimeter?: ").lower().strip()

            if m == "display info":
                clear_screen()
                console.print(triangle.display_info())

            elif m == "area":
                clear_screen()
                console.print(triangle.area())

            elif m == "perimeter":
                one = int("Enter the first side of the triangle: ")
                clear_screen()
                two = int("Enter the second side of the triangle: ")
                clear_screen()
                three = int("Enter the third side of the triangle")
                clear_screen()
                console.print(triangle.perimeter(one, two, three))

            else:
                raise TypeError("You can only write \"Display Info\", \"Area\", or \"Perimeter\".")
        else:
            raise TypeError("You can only write a number.")
        
    elif first == "Cube":
        cub = input("Enter The length: ")
        
        if isfloat(cub):
            clear_screen()
            cube = Cube(float(cub))
            m = input("Would you like to display info, print the volume, print the surface area, print the diagonal, or print the perimeter?: ").lower().strip()

            if m == "display info":
                clear_screen()
                console.print(cube.display_info())

            elif m == "volume":
                clear_screen()
                console.print(cube.volume())

            elif m == "surface area":
                clear_screen()
                console.print(cube.surface_area())
            
            elif m == "perimeter":
                clear_screen()
                console.print(cube.perimeter())

            elif m == "diagonal":
                clear_screen()
                console.print(cube.diagonal())

            else:
                raise TypeError("You can only write \"Display Info\", \"Volume\", or \"Surface Area\", \"Perimeter\", or \"Diagonal\".")
        else:
            raise TypeError("You can only write a number.")
        
    elif first == "Sphere":
        spher = input("Enter The radius: ")
        
        if isfloat(spher):
            clear_screen()
            sphere = Sphere(float(spher))
            m = input("Would you like to display info, print the volume, or print the surface area?: ").lower().strip()

            if m == "display info":
                clear_screen()
                console.print(sphere.display_info())

            elif m == "volume":
                clear_screen()
                console.print(sphere.volume())

            elif m == "surface area":
                clear_screen()
                console.print(sphere.surface_area())
            
            else:
                raise TypeError("You can only write \"Display Info\", \"Volume\", or \"Surface Area\".")
        else:
            raise TypeError("You can only write a number.")
        
    elif first == "rectangular prism":
        rec = input("Enter the length: ")
        clear_screen()
        rec1 = input("Enter the width: ")
        clear_screen()
        rec2 = input("Enter the height: ")
        
        if isfloat(rec) and isfloat(rec1) and isfloat(rec2):
            clear_screen()
            rectangular_prism = Rectangular_prism(float(rec), float(rec1), float(rec2))
            m = input("Would you like to display info, print the volume, print the perimeter, print the space diagonal, or print the surface area?: ").lower().strip()

            if m == "display info":
                clear_screen()
                console.print(rectangular_prism.display_info())

            elif m == "volume":
                clear_screen()
                console.print(rectangular_prism.volume())

            elif m == "perimeter":
                clear_screen()
                console.print(rectangular_prism.perimeter())

            elif m == "surface area":
                clear_screen()
                console.print(rectangular_prism.surface_area())

            elif m == "space diagonal":
                clear_screen()
                console.print(rectangular_prism.space_diagonal())

            else:
                raise TypeError("You can only write \"Display Info\", \"Surface Area\", \"Volume\", \"Space Diagonal\", or \"Perimeter\".")
        else:
            raise TypeError("You can only write a number.")
    elif first == "triangular prism":
        one = input("Enter the first side of the triangular prism: ")
        two = input("Enter the second side of the triangular prism: ")
        three = input("Enter the third side of the triangular prism: ")
        height = input("Enter the height of the triangular prism: ")

        if isfloat(one) and isfloat(two) and isfloat(three) and isfloat(height):
            clear_screen()
            triangular_prism = Triangular_prism(float(one), float(two), float(three), float(height))
            m = input("Would you like to display info, print the volume, print the lateral surface area, print the surface area, print the perimeter, or print the base area?: ").lower().strip()

            if m == "display info":
                clear_screen()
                console.print(triangular_prism.display_info())

            elif m == "volume":
                clear_screen()
                console.print(triangular_prism.volume())

            elif m == "lateral surface area":
                clear_screen()
                console.print(triangular_prism.lateral_surface_area())
            
            elif m == "surface area":
                clear_screen()
                console.print(triangular_prism.surface_area())

            elif m == "base area":
                clear_screen()
                console.print(triangular_prism.base_area())

            elif m == "perimeter":
                clear_screen()
                console.print(triangular_prism.perimeter())

            else:
                raise TypeError("You can only write \"Display Info\", \"Volume\", \"Lateral Surface Area\", \"Surface Area\", \"Base Area\", or \"Perimeter\".")
        else:
            raise TypeError("You can only write a number.")

def main2():

    first = input("Enter The Shape that you would like to measure: (type \"list\" if you would like a list of avaliable shapes.)\n").lower().strip()
    clear_screen()

    if first == "list":
        console.print(f"[yellow italic]Avaliable Shapes to measure:[/yellow italic] \n[bold green]Square[/bold green], \n[bold blue]Circle[/bold blue], \n[bold green]Rectangle[/bold green], \n[bold blue]Triangle[/bold blue], \n[bold purple]Cube[/bold purple], \n[bold magenta]Sphere[/bold magenta], \n[bold purple]Rectangular prism[/bold purple], \n[bold magenta]Triangular prism[/bold magenta]. \n[yellow italic]Press \"Enter\" to restart the calculator.[/yellow italic] \n{"\u2024" * 100}")
        input()
        console.print("Program ended. Please wait while this program restarts the calculator. Wait how are you reading this?")
        clear_screen()
        main2()

    elif first == "square":
        squar = input("Enter The height: ").strip()
        
        if isfloat(squar):
            clear_screen()
            square = Square(float(squar))
            m = input("Would you like to display info, print the area, print the diagonal, or print the perimeter?: ").lower().strip()

            if m == "display info":
                clear_screen()
                console.print(square.display_info())

            elif m == "area":
                clear_screen()
                console.print(square.area())

            elif m == "perimeter":
                clear_screen()
                console.print(square.perimeter())
            
            elif m == "diagonal":
                clear_screen()
                console.print(square.diagonal)

            else:
                raise TypeError("You can only write \"Display Info\", \"Area\", \"Diagonal\", or \"Perimeter\".")
        else:
            raise TypeError("You can only write a number.")
        
    elif first == "circle":
        circl = input("Enter the radius: ")

        if isfloat(circl):
            circle = Circle(float(circl))
            clear_screen()
            n = input("Would you like to display info, print the area, or print the circumference?: ").lower().strip()

            if n == "display info":
                clear_screen()
                console.print(circle.display_info())

            elif n == "area":
                clear_screen()
                console.print(circle.area())
            
            elif n == "circumference":
                clear_screen()
                console.print(circle.circumference())
            
            else:
                raise TypeError("You can only write \"Display Info\", \"Area\", or \"Circumference\".")
            
        else:
            raise TypeError("You can only write a number.")
        
    elif first == "rectangle":
        rec = input("Enter the length: ")
        clear_screen()
        rec1 = input("Enter the width: ")

        if isfloat(rec) and isfloat(rec1):
            rectangle = Rectangle(float(rec), float(rec1))
            clear_screen()
            n = input("Would you like to display info, print the area, print the perimeter, or print the diagonal?: ").lower().strip()

            if n == "display info":
                clear_screen()
                console.print(rectangle.display_info())

            elif n == "area":
                clear_screen()
                console.print(rectangle.area())
            
            elif n == "perimeter":
                clear_screen()
                console.print(rectangle.perimeter())
            
            elif n == "diagonal":
                clear_screen()
                console.print(rectangle.diagonal())
            
            else:
                raise TypeError("You can only write \"Display Info\", \"Area\", or \"Perimeter\", \"Diagonal\".")
            
        else:
            raise TypeError("You can only write a number.")
        
    elif first == "triangle":
        tri = input("Enter The base: ")
        clear_screen()
        tri1 = input("Enter the height")
        
        if isfloat(tri) and isfloat(tri1):
            clear_screen()
            triangle = Triangle(float(tri), float(tri1))
            m = input("Would you like to display info, print the area, or print the perimeter?: ").lower().strip()

            if m == "display info":
                clear_screen()
                console.print(triangle.display_info())

            elif m == "area":
                clear_screen()
                console.print(triangle.area())

            elif m == "perimeter":
                one = int("Enter the first side of the triangle: ")
                clear_screen()
                two = int("Enter the second side of the triangle: ")
                clear_screen()
                three = int("Enter the third side of the triangle")
                clear_screen()
                console.print(triangle.perimeter(one, two, three))

            else:
                raise TypeError("You can only write \"Display Info\", \"Area\", or \"Perimeter\".")
        else:
            raise TypeError("You can only write a number.")
        
    elif first == "Cube":
        cub = input("Enter The length: ")
        
        if isfloat(cub):
            clear_screen()
            cube = Cube(float(cub))
            m = input("Would you like to display info, print the volume, print the surface area, print the diagonal, or print the perimeter?: ").lower().strip()

            if m == "display info":
                clear_screen()
                console.print(cube.display_info())

            elif m == "volume":
                clear_screen()
                console.print(cube.volume())

            elif m == "surface area":
                clear_screen()
                console.print(cube.surface_area())
            
            elif m == "perimeter":
                clear_screen()
                console.print(cube.perimeter())

            elif m == "diagonal":
                clear_screen()
                console.print(cube.diagonal())

            else:
                raise TypeError("You can only write \"Display Info\", \"Volume\", or \"Surface Area\", \"Perimeter\", or \"Diagonal\".")
        else:
            raise TypeError("You can only write a number.")
        
    elif first == "Sphere":
        spher = input("Enter The radius: ")
        
        if isfloat(spher):
            clear_screen()
            sphere = Sphere(float(spher))
            m = input("Would you like to display info, print the volume, or print the surface area?: ").lower().strip()

            if m == "display info":
                clear_screen()
                console.print(sphere.display_info())

            elif m == "volume":
                clear_screen()
                console.print(sphere.volume())

            elif m == "surface area":
                clear_screen()
                console.print(sphere.surface_area())
            
            else:
                raise TypeError("You can only write \"Display Info\", \"Volume\", or \"Surface Area\".")
        else:
            raise TypeError("You can only write a number.")
        
    elif first == "rectangular prism":
        rec = input("Enter the length: ")
        clear_screen()
        rec1 = input("Enter the width: ")
        clear_screen()
        rec2 = input("Enter the height: ")
        
        if isfloat(rec) and isfloat(rec1) and isfloat(rec2):
            clear_screen()
            rectangular_prism = Rectangular_prism(float(rec), float(rec1), float(rec2))
            m = input("Would you like to display info, print the volume, print the perimeter, print the space diagonal, or print the surface area?: ").lower().strip()

            if m == "display info":
                clear_screen()
                console.print(rectangular_prism.display_info())

            elif m == "volume":
                clear_screen()
                console.print(rectangular_prism.volume())

            elif m == "perimeter":
                clear_screen()
                console.print(rectangular_prism.perimeter())

            elif m == "surface area":
                clear_screen()
                console.print(rectangular_prism.surface_area())

            elif m == "space diagonal":
                clear_screen()
                console.print(rectangular_prism.space_diagonal())

            else:
                raise TypeError("You can only write \"Display Info\", \"Surface Area\", \"Volume\", \"Space Diagonal\", or \"Perimeter\".")
        else:
            raise TypeError("You can only write a number.")
    elif first == "triangular prism":
        one = input("Enter the first side of the triangular prism: ")
        two = input("Enter the second side of the triangular prism: ")
        three = input("Enter the third side of the triangular prism: ")
        height = input("Enter the height of the triangular prism: ")

        if isfloat(one) and isfloat(two) and isfloat(three) and isfloat(height):
            clear_screen()
            triangular_prism = Triangular_prism(float(one), float(two), float(three), float(height))
            m = input("Would you like to display info, print the volume, print the lateral surface area, print the surface area, print the perimeter, or print the base area?: ").lower().strip()

            if m == "display info":
                clear_screen()
                console.print(triangular_prism.display_info())

            elif m == "volume":
                clear_screen()
                console.print(triangular_prism.volume())

            elif m == "lateral surface area":
                clear_screen()
                console.print(triangular_prism.lateral_surface_area())
            
            elif m == "surface area":
                clear_screen()
                console.print(triangular_prism.surface_area())

            elif m == "base area":
                clear_screen()
                console.print(triangular_prism.base_area())

            elif m == "perimeter":
                clear_screen()
                console.print(triangular_prism.perimeter())

            else:
                raise TypeError("You can only write \"Display Info\", \"Volume\", \"Lateral Surface Area\", \"Surface Area\", \"Base Area\", or \"Perimeter\".")
        else:
            raise TypeError("You can only write a number.")

main()