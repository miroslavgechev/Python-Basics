import math

price_video_card_per_piece = int(input())
price_connector_per_piece = int(input())
electricity_price_per_day = float(input())
profit_per_card_per_day = float(input())

price_video_cards = 13 * price_video_card_per_piece
price_connectors = 13 * price_connector_per_piece
total_investment = price_connectors + price_video_cards + 1000

profit_per_day = (profit_per_card_per_day - electricity_price_per_day) * 13

return_of_investment = math.ceil(total_investment / profit_per_day)

print(total_investment)
print(return_of_investment)