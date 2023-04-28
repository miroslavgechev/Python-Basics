pens = int(input())
markers = int(input())
erasers = int(input())
discount = int(input())

price_pens = pens * 5.8
price_markers = markers * 7.2
price_erasers = erasers * 1.2

price = price_pens + price_erasers + price_markers
discount_price = price * discount/100
total_price = price - discount_price

print (total_price)