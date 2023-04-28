age = int(input())
price_washing_machine = float(input())
price_toy = int(input())

even_birthday_sum = 0
odd_birthday_sum = 0
total_sum = 0

number_of_toys = 0

for birthdays in range (1, age + 1):
    if birthdays % 2 == 0:
        even_birthday_sum += 10 * (birthdays/2)
        even_birthday_sum -= 1
    else:
        number_of_toys += 1

total_sum = even_birthday_sum + number_of_toys * price_toy

if total_sum >= price_washing_machine:
    print(f"Yes! {(total_sum - price_washing_machine):.2f}")
else:
    print(f"No! {abs((price_washing_machine - total_sum)):.2f}")
