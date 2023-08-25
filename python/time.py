from datetime import datetime

today = datetime.now()
print( 'Today Is:' , today )

for attr in \
[ 'year' , 'month' , 'day' , 'hour' , 'minute' , 'second' , 'microsecond' ] :
        print( attr , ':\t' , getattr( today , attr ) )

print( 'Time:' , today.hour , ':' , today.minute , sep = '' )

day = today.strftime( '%A' )
month = today.strftime( '%B' )

print( 'Date:' , day , month , today.day )


# Today Is: 2023-08-25 18:59:18.394778
# year :   :       2023
# month :  :       8
# day :    :       25
# hour :   :       18
# minute :         :       59
# second :         :       18
# microsecond :    :       394778
# Time:18:59
# Date: Friday August 25


# from datetime import datetime

# Get the current date and time
# today = datetime.now()
# print('Today Is:', today)
# Here, you import the datetime class from the datetime module and use the datetime.now() function to get the current date and time. 
# The today variable now holds this information, and it's printed.

# python
# Loop through and print individual date and time components
# for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
#   print(attr, ':\t', ':\t', getattr(today, attr))
# This loop iterates through a list of strings, where each string represents a date or time component (e.g., 'year', 'month', etc.). 
# It uses the getattr function to retrieve the corresponding attribute from the today datetime object and prints it. However, 
# there are two colons (:\t, :\t) after each attribute name that don't seem necessary and might be a typo. The correct code should just have one colon (:).

# Print the time in the format HH:MM
# print('Time:', today.hour, ':', today.minute, sep='')
# This code prints the current time in the format "HH:MM" by accessing the hour and minute attributes of the today datetime object and removing any separator (sep='').

# python
# Format and print the date
# day = today.strftime('%A')
# month = today.strftime('%B')

# print('Date:', day, month, today.day)
# Here, you format and print the date. today.strftime('%A') retrieves the full weekday name, and today.strftime('%B') retrieves the full month name. 
# today.day is used to get the day of the month. All these components are then printed as "Date: [weekday] [month] [day]".