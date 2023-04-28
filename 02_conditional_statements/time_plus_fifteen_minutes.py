hour_input = int(input())
minutes_input = int(input())

hours_to_minutes = hour_input * 60

total_minutes = hours_to_minutes + minutes_input + 15

hours = total_minutes // 60
minutes = total_minutes % 60

if hours > 23:
    hours = 0

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")