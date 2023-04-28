exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

exam_in_minutes = exam_hours * 60 + exam_minutes
arrival_in_minutes = arrival_hours * 60 + arrival_minutes

diff = exam_in_minutes - arrival_in_minutes
# Positive if early
# Negative if late

if diff == 0:
    print(f"On time")
elif diff > 0:
     if diff <= 30:
        print(f"On time")
        print(f"{diff} minutes before the start")
     elif diff <= 59:
        print(f"Early")
        print(f"{diff} minutes before the start")
     else:
        hour = diff // 60
        minutes = diff % 60
        if minutes <= 9:
            print(f"Early")
            print(f"{hour}:0{minutes} hours before the start")
        else:
            print(f"Early")
            print(f"{hour}:{minutes} hours before the start")
elif diff < 0:
    print(f"Late")
    diff = abs(diff)
    if diff <= 59:
        print(f"{diff} minutes after the start")
    else:
        hour = diff // 60
        minutes = diff % 60
        if minutes <= 9:
            print(f"{hour}:0{minutes} hours after the start")
        else:
            print(f"{hour}:{minutes} hours after the start")


