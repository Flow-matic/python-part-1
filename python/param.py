def echo( user , lang , sys ) :
    print( 'User:' , user , 'Language:' , lang , 'Platform:' , sys )

echo( 'Mike' , 'Python' , 'Windows' )

echo( lang = 'Python' , sys = 'Mac OS' , user = 'Anne' )


def mirror( user = 'Carole' , lang = 'Python' ) :
    print( 'User:' , user , 'Language:' , lang )

mirror( )
mirror( lang = 'Java' )
mirror( 'Tony' )
mirror( 'Susan' , 'C++' )



# with "\n"

# User: Mike Language: Python Platform: Windows
# User: Anne Language: Python Platform: Mac OS

# User: Carole Language: Python

# User: Carole Language: Java

# User: Tony Language: Python

# User: Susan Language: C++

# without "\n"

# User: Mike Language: Python Platform: Windows
# User: Anne Language: Python Platform: Mac OS
# User: Carole Language: Python
# User: Carole Language: Java
# User: Tony Language: Python
# User: Susan Language: C++

# The character sequence "\n" in Python represents a newline character. 
# It is an escape sequence that is used to insert a line break or move the cursor to the next line in a string.

# In your code snippet, "\n" is used within the print function to add a blank line before printing the output of the mirror function.
#  This creates a visual separation between the different calls to the mirror function, making the output more readable. 