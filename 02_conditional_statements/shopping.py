budget = float(input())
video_pcs = int(input())
cpu_pcs = int(input())
ram_pcs = int(input())

cost_video_per_pcs = 250
cost_cpu_per_pcs = (cost_video_per_pcs * video_pcs) * 0.35
cost_ram_per_pcs = (cost_video_per_pcs * video_pcs) * 0.10

total_cost = cost_video_per_pcs * video_pcs + cost_cpu_per_pcs * cpu_pcs + cost_ram_per_pcs * ram_pcs

if video_pcs > cpu_pcs:
    total_cost = total_cost * 0.85

diff = abs(total_cost - budget)

if budget >= total_cost:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
