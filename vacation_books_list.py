total_count_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

total_time = total_count_pages // pages_per_hour

hour_per_day = total_time // number_of_days
print(hour_per_day)
