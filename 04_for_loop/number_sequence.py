import sys

number_of_numbers = int (input())

max_num = - sys.maxsize
min_num = sys.maxsize

for numbers in range (number_of_numbers):
    number = int (input())
    if max_num < number:
        max_num = number
    if min_num > number:
        min_num = number

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")