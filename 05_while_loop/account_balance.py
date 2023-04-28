total_money = 0

command = input()

while command != "NoMoreMoney":
    increase = float(command)
    if increase < 0:
        print(f"Invalid operation!")
        break
    total_money += increase
    print(f"Increase: {increase:.2f}")
    command = input()

print(f"Total: {total_money:.2f}")