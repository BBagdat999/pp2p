date_str1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date_str2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

# Extract year, month, day, hour, minute, and second from the date strings
year1, month1, day1, hour1, minute1, second1 = map(int, date_str1.replace('-', ' ').replace(':', ' ').split())
year2, month2, day2, hour2, minute2, second2 = map(int, date_str2.replace('-', ' ').replace(':', ' ').split())

# Compute the difference in years, months, days, hours, minutes, and seconds
years_diff = year2 - year1
months_diff = month2 - month1
days_diff = day2 - day1
hours_diff = hour2 - hour1
minutes_diff = minute2 - minute1
seconds_diff = second2 - second1

# Convert years and months to days
days_diff += years_diff * 365  # Ignoring leap years for simplicity
for m in range(month1, month2):
    days_diff += 30  # Assuming 30 days in a month

total_seconds_diff = (days_diff * 24 * 60 * 60) + (hours_diff * 60 * 60) + (minutes_diff * 60) + seconds_diff

# Output the difference
print("Difference in seconds:", abs(total_seconds_diff))