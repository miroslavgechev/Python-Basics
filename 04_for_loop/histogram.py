number_of_numbers = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for numbers in range (number_of_numbers):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif 200 <= current_number <= 399:
        p2 += 1
    elif 400 <= current_number <= 599:
        p3 += 1
    elif 600 <= current_number <= 799:
        p4 += 1
    elif current_number >= 800:
        p5 += 1

print(f"{(p1*100/number_of_numbers):.2f}%")
print(f"{(p2*100/number_of_numbers):.2f}%")
print(f"{(p3*100/number_of_numbers):.2f}%")
print(f"{(p4*100/number_of_numbers):.2f}%")
print(f"{(p5*100/number_of_numbers):.2f}%")
