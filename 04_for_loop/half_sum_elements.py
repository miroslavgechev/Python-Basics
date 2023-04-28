import sys

number_of_numbers = int(input())

max_num = -sys.maxsize
sum = 0

for numbers in range (number_of_numbers):
    current_number = int(input())
    if max_num < current_number:
        max_num = current_number
    sum += current_number

if max_num == (sum - max_num):
    print("Yes")
    print(f"Sum = {sum - max_num}")
else:
    print("No")
    print(f"Diff = {abs(2 * max_num - sum)}")