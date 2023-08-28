def display( s ) :
    '''Display an argument value.'''
    print( s )

display( display.__doc__ )

display( r'C:\Program Files' )

display( '\nHello' + ' Python' )

display( 'Python in easy steps\n' [ 7  : ] )

display( 'P' in 'Python' )
display( 'p' in 'Python' )


# Display an argument value.
# C:\Program Files

# Hello Python
# in easy steps

# True
# False


# display(display.__doc__):

# This prints the docstring of the display function. The docstring is a string enclosed in triple quotes (''') that provides documentation or comments about the function. 
# In this case, it explains that the function is used to display an argument value.
# display(r'C:\Program Files'):

# This prints the string 'C:\Program Files'. The r before the string indicates a raw string, which treats backslashes as literal characters and doesn't escape them. 
# This is commonly used for file paths in Windows to avoid issues with backslashes.
# display('\nHello' + ' Python'):

# This prints the string '\nHello Python', which starts with a newline character (\n) and then contains 'Hello Python'.
# display('Python in easy steps\n' [ 7 : ]):

# This prints a substring of the string 'Python in easy steps\n'. It uses slicing to extract characters from index 7 to the end of the string. So, it prints 'easy steps\n'.
# display('P' in 'Python'):

# This prints True. It checks if the character 'P' is in the string 'Python', which it is, so it returns True.
# display('p' in 'Python'):

#This prints False. It checks if the character 'p' is in the string 'Python', which it is not, so it returns False.