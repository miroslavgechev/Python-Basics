import math

movie_name = input()
movie_duration = int(input())
break_duration = int(input())

duration_lunch = break_duration / 8
duration_relax = break_duration / 4

total_time_needed = duration_relax + duration_lunch + movie_duration

diff = abs(break_duration - total_time_needed)
diff = math.ceil(diff)

if break_duration >= total_time_needed:
    print(f"You have enough time to watch {movie_name} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {diff} more minutes.")