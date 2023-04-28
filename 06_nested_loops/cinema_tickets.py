
movie_name = input()

total_tickets_counter = 0
total_student_tickets_counter = 0
total_standard_tickets_counter = 0
total_kid_tickets_counter = 0

while movie_name != "Finish":
    hall_is_full = False
    hall_capacity = int(input())

    student_ticket_counter = 0
    standard_ticket_counter = 0
    kid_ticket_counter = 0
    tickets_for_current_movie = 0

    text_input = input()

    while text_input != "End":
        total_tickets_counter += 1
        tickets_for_current_movie += 1

        if text_input == "student":
            student_ticket_counter += 1
        elif text_input == "standard":
            standard_ticket_counter += 1
        elif text_input == "kid":
            kid_ticket_counter += 1
        if hall_capacity == tickets_for_current_movie:
            hall_is_full = True
            occupancy_rate = 100.00
            break

        text_input = input()

    total_student_tickets_counter += student_ticket_counter
    total_standard_tickets_counter += standard_ticket_counter
    total_kid_tickets_counter += kid_ticket_counter

    if hall_is_full:
        print(f"{movie_name} - {occupancy_rate:.2f}% full.")
    else:
        occupancy_rate = (tickets_for_current_movie / hall_capacity) * 100
        print(f"{movie_name} - {occupancy_rate:.2f}% full.")

    movie_name = input()

student_occupancy = (total_student_tickets_counter / total_tickets_counter) * 100
standard_occupancy = (total_standard_tickets_counter / total_tickets_counter) * 100
kid_occupancy = (total_kid_tickets_counter / total_tickets_counter) * 100


print(f"Total tickets: {total_tickets_counter}")
print(f"{student_occupancy:.2f}% student tickets.")
print(f"{standard_occupancy:.2f}% standard tickets.")
print(f"{kid_occupancy:.2f}% kids tickets.")


