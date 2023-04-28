price_yearly_tax = int(input())

price_shoes = price_yearly_tax * 0.6
price_jersey = price_shoes * 0.8
price_ball  = price_jersey / 4
price_accessories = price_ball / 5

total_investment = price_accessories + price_ball + price_shoes + price_jersey + price_yearly_tax

print (total_investment)

i = 0
while i <= 6:
    i += 1
    if i % 2 == 0:
        print(i, end="")
