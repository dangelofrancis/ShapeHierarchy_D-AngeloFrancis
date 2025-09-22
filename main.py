
#########################################################################################
# TITLE: Shape Hierarchy Project                                                        #
# FILE NAME: ShapeHierarchy_D'AngeloFrancis.py                                          #
# DATE: 9/21/2025                                                                       #
# PROGRAMMER: D'Angelo Francis                                                          #
# REQUIREMENTS: Write a Python program using classes, inheritance, and dynamic method   #
# resolution to model basic geometric shapes                                            #
#########################################################################################

from Circle import Circle
from Rectangle import Rectangle
from Square import Square

shapes = [
    Circle(10,10,4,"Circle_1"),
    Circle(20,30,9,"Circle_2"),
    Rectangle(10,20,"Rectangle_1"),
    Rectangle(20,30,"Rectangle_2"),
    Square(10,"Square")
    ]

print("--- Polymorphism check ---")
for shape in shapes:
    print(f"{shape.name} Area = {shape.are:.5f}")

print("--- Getter/setter check ---")

# Circle
circle = shapes[0]
print(f"{circle.name} Current: {circle.radius} {circle.area:.5f}")
circle.radius = circle.radius * 2
print(f"{circle.name} Doubled: {circle.radius} {circle.area:.5f}")

# Rectangle
rectangle = shapes[2]
print(f"{rectangle.name} Current: {rectangle.length} {rectangle.width} {rectangle.area:.5f}")
rectangle._length = rectangle.length * 2
rectangle._width = rectangle.width * 2
rectangle.calc_area()
print(f"{rectangle.name} Doubled: {rectangle.length} {rectangle.width} {rectangle.area:.5f}")

# Square
square = shapes[4]
print(f"{square.name} Current: {square.side} {square.area:.5f}")
square.side = square.side * 2
print(f"{square.name} Doubled: {square.side} {square.area:.5f}")