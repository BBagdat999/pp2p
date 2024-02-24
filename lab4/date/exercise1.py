from datetime import datetime, timedelta

initial_date_str = input("Enter the initial date in YYYY-MM-DD format: ")
initial_date = datetime.strptime(initial_date_str, "%Y-%m-%d")
new_date = initial_date - timedelta(days=5)

# Print the new date
print("Date five days ago:", new_date.strftime("%Y-%m-%d"))