cake_width = int(input())
cake_lenght = int(input())

cake_size = cake_lenght * cake_width
slice_count = cake_size

party_has_ended = False

while slice_count > 0:
    cakes_taken = input()
    if cakes_taken == "STOP":
        party_has_ended = True
        break

    slice_count -= int(cakes_taken)

if party_has_ended and slice_count > 0:
    print(f"{slice_count} pieces are left.")
else:
    print(f"No more cake left! You need {abs(slice_count)} pieces more.")