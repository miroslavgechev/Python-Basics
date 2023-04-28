book_pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_reading_time = book_pages // pages_per_hour
total_hours_per_day = total_reading_time // days

print (total_hours_per_day)
