num = input( 'Enter An Integer:' )

def square( num ) :

    if not num.isdigit( ) :
        return 'Invalid Entry'

    num = int( num )
    return num * num

print( num , 'Squared Is:' , square( num ) )


# Enter An Integer:8 ( 8 Squared Is: 64 )

# Enter An Integer:8.0  ( 8.0 Squared Is: Invalid Entry )

# Enter An Integer:Eight ( Eight Squared Is: Invalid Entry )


# This code is designed to take an integer as input from the user, calculate the square of that integer, and then print the result. Here's a breakdown of what the code does step by step:

# It prompts the user to enter an integer by displaying the message "Enter An Integer:" and waits for user input using the input function. The user's input is stored in the variable num as a string.

# It defines a function named square that takes one argument, num.

# Inside the square function:

# It checks if the input num is not composed entirely of digits using the isdigit() method. If it's not composed of digits, it returns the string 'Invalid Entry' to indicate that the input is not a valid integer.
# If num is composed of digits, it converts num to an integer using int(num).
# It calculates the square of the integer by multiplying num by itself (num * num) and returns the result.
# It calls the square function with the num that the user entered and stores the result.

# It prints the original num (the user's input) and the result of the square function, indicating that the number squared is being displayed.

# In summary, this code takes user input, checks if it's a valid integer, calculates the square of that integer if it is valid, and then displays the result. If the input is not a valid integer, it displays an "Invalid Entry" message.

