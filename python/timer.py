from time import *

start_timer = time()

struct = localtime( start_timer )

print( 'Starting Countdown At:' , strftime( '%X' , struct ) )

i = 10
while i > -1 :
    print( i )
    i -= 1
    sleep( 1 )

end_timer = time()

difference = round( end_timer - start_timer )

print( '\nRuntime:' , difference , 'Seconds' )


# Starting Countdown At: 16:52:02
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# Runtime: 11 Seconds


# it imports the time module, which provides various time-related functions and constants.

# It records the current time using time() function and stores it in the start_timer variable.

# It converts the current time to a struct representing the local time using localtime() function and stores it in the struct variable.

# It prints the current time in a specific format (HH:MM:SS) using strftime() function and the '%X' format string. However, 
# there is a missing argument for strftime(), which should be the struct variable. It should be corrected like this:

# print('Starting Countdown At:', strftime('%X', struct))
# It initializes a variable i with the value 10.

# It enters a while loop that counts down from 10 to 0. Inside the loop:

# It prints the current value of i.
# It decrements i by 1.
# It sleeps for 1 second using the sleep(1) function, causing a one-second delay in each iteration.
# After the loop completes, it records the current time again using time() and stores it in the end_timer variable.

# It calculates the difference between end_timer and start_timer to measure the runtime of the code in seconds.

# It prints the runtime in seconds.