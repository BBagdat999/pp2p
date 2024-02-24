days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

current_day_index = (int(input("Enter today's day index (0 for Monday, 1 for Tuesday, ..., 6 for Sunday): ")) + 7) % 7

yesterday_index = (current_day_index - 1) % 7

tomorrow_index = (current_day_index + 1) % 7

print("Yesterday:", days_of_week[yesterday_index])
print("Today:", days_of_week[current_day_index])
print("Tomorrow:", days_of_week[tomorrow_index])