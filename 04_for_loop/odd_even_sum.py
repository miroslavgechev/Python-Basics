number_of_numbers = int(input())

even_nums = 0
odd_nums = 0

for number in range (0, number_of_numbers):
    current_number = int(input())

    if number % 2 == 0:
        even_nums += current_number
    else:
        odd_nums += current_number

if even_nums == odd_nums:
    print(f"Yes")
    print(f"Sum = {even_nums}")
else:
    print("No")
    print(f"Diff = {abs(even_nums - odd_nums)}")

