# Between 1/1/1901 - 31/12/2000, how many Sundays fell on first of the month?

# Context:
# - 1/1/1900 was a Monday
# - 9,4,6,11 have 30 days
# - rest have 31
# - feb has 28, and on leap years 29
# - Leap year occurs on any year evenly divisible by 4,
#       but not on a centruy unless divisible by 400

# Num of days per month
month_dictionary = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
                     6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# Tracker of days passed from 1/1/1900
iterator = 1
# 
month = 1
year = 1900
# Instances where 1st is a Sunday
occurrences = 0
# While within 20th Century
while year < 2001:
    # If fulfill leap year condition
    if month == 2 and year % 4 == 0:
        # And its not a century
        if year % 100 != 0:
            # Feb == 29
            month_duration = 29
        # If it is a century
        else:
            # Only a leap year when divisible by 400
            if year % 400 == 0:
                month_duration = 29
            else:
                month_duration = 28
    # For all other instances, length of month in dictionary
    else:
        month_duration = month_dictionary[month]

    day = 0
    # Repeat for duration of month
    for _ in range(month_duration):
        day += 1
        # If first of month, and its a Sunday
        if day == 1 and iterator % 7 == 0:
            # Provided we are in century (1901 on)
            if year >= 1901:
                # Add 1 to occurrences
                occurrences += 1
        # Add one to tracker days passed
        iterator += 1
    # At end of month, go to new month
    month += 1
    # If we reach end of year, add to year and reset month
    if month == 13:
        year += 1
        month = 1

# print occurrences where Sunday occurs on 1st of month
print(occurrences)