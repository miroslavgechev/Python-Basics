coin_counter = 0
total_coin_counter = 0

resto = float (input())
resto = resto * 100
resto = round(resto, 2)

while resto > 0:
        if resto // 200 != 0:
                coin_counter = resto // 200
                resto -= coin_counter * 200
                total_coin_counter += coin_counter
        if resto // 100 != 0:
                coin_counter = resto // 100
                resto -= coin_counter * 100
                total_coin_counter += coin_counter
        elif resto // 50 != 0:
                coin_counter = resto // 50
                resto -= coin_counter * 50
                total_coin_counter += coin_counter
        elif resto // 20 != 0:
                coin_counter = resto // 20
                resto -= coin_counter * 20
                total_coin_counter += coin_counter
        elif resto // 10 != 0:
                coin_counter = resto // 10
                resto -= coin_counter * 10
                total_coin_counter += coin_counter
        elif resto // 5 != 0:
                coin_counter = resto // 5
                resto -= coin_counter * 5
                total_coin_counter += coin_counter
        elif resto // 2 != 0:
                coin_counter = resto // 2
                resto -= coin_counter * 2
                total_coin_counter += coin_counter
        elif resto // 1 != 0:
                coin_counter = resto // 1
                resto -= coin_counter * 1
                total_coin_counter += coin_counter

print(f"{total_coin_counter:.0f}")