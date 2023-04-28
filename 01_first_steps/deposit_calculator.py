deposited_sum = float(input())
deposit_time = int(input())
annual_rate = float (input())

sum = deposited_sum + deposit_time * ((deposited_sum * annual_rate/100)/12)

print(sum)