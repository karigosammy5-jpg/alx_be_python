#Define the number of hours to convert
hours = 2

# Define the conversion factor (seconds per hour: 60 minutes * 60 seconds)
SECONDS_PER_HOUR = 3600

# Calculate the total number of seconds
# seconds = hours * 3600
seconds = hours * SECONDS_PER_HOUR

# Print the result in the required format
print(f"{hours} hour(s) is {seconds} seconds.")