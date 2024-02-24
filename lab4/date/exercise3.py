from datetime import datetime

# Get the current date and time
today = datetime.now()

# Drop microseconds
today_time__without_microseconds = today.replace(microsecond=0)

# Print the original and modified datetime objects
print("Original datetime:", today)