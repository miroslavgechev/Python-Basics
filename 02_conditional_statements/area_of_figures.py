from math import pi

figure = input()
result = 0

if figure == "square":
    side1 = float(input())
    result = side1 * side1
elif figure == "rectangle":
    side1 = float (input())
    side2 = float(input())
    result = side1 * side2
elif figure == "circle":
    radius = float(input())
    result = pi * (radius ** 2)
elif figure == "triangle":
    size = float(input())
    height = float(input())
    result = size * height / 2

print(f"{result: .3f}")