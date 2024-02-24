import datetime

days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

today = datetime.datetime.now().weekday()
yesterday = (today - 1) % 7
tomorrow =  (today + 1) % 7

print("Yesterday:", days_of_the_week[yesterday])
print("Today:", days_of_the_week[today])
print("Tomorrow:", days_of_the_week[tomorrow])