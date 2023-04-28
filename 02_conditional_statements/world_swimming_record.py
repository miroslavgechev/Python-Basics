import math

record_time_in_seconds = float(input())
distance_in_meters = float(input())
time_to_swim_one_meter = float(input())

total_time = distance_in_meters * time_to_swim_one_meter

delay =  math.floor(distance_in_meters / 15) * 12.5

total_time = total_time + delay

diff = abs(record_time_in_seconds - total_time)

if total_time < record_time_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")