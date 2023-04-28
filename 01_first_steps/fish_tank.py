length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume_tank = length * width * height
volume_tank_liters = volume_tank / 1000
volume_tank_liters_correction = volume_tank_liters * (1 - percentage/100)

print(volume_tank_liters_correction)