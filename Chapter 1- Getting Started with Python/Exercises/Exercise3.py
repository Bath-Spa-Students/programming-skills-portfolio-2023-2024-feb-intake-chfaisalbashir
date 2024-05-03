#Write a Python program to display the current date and time.

import datetime

# current date and time 
current_datetime = datetime.datetime.now()

# Format the date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Print the  date and time
print(f"Current date and time: {formatted_datetime}")
