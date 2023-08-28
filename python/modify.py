string = 'coding for beginners in easy steps'

print( '\nCapitalized:\t' , string.capitalize( ) )
print( '\nTitled:\t\t' , string.title( ) )
print( '\nCentered:\t' , string.center( 30 , '*' ) )

print( '\nUppercase:\t' , string.upper( ) )
print( '\nJoined:\t\t' , string.join( '**' ) )

print( '\nJustified:\t\t' , string.rjust( 30 , '*' ) )

print( '\nReplaced:\t' , string.replace( 's' , '*' ) )



# Capitalized:     Coding for beginners in easy steps

# Titled:          Coding For Beginners In Easy Steps

# Centered:        coding for beginners in easy steps

# Uppercase:       CODING FOR BEGINNERS IN EASY STEPS

# Joined:          *coding for beginners in easy steps*

# Justified:               coding for beginners in easy steps

# Replaced:        coding for beginner* in ea*y *tep*


# string.capitalize():

# This method capitalizes the first character of the string.
# It prints: "Capitalized: Coding for beginners in easy steps"
# string.title():

# This method capitalizes the first character of each word in the string.
# It prints: "Titled: Coding For Beginners In Easy Steps"
# string.center(30, '*'):

# This method centers the string within a field of 30 characters, padding it with '*' characters on both sides if necessary.
# It prints: "Centered: coding for beginners in easy steps"
# string.upper():

# This method converts all characters in the string to uppercase.
# It prints: "Uppercase: CODING FOR BEGINNERS IN EASY STEPS"
# string.join('**'):

# This method attempts to join the string 'coding for beginners in easy steps' with '**', 
# but it will raise a TypeError because join() expects an iterable (like a list) as an argument, not a string.
# It will not print anything because of the error.
# string.rjust(30, '*'):

# This method right-justifies the string within a field of 30 characters, padding it with '*' characters on the left if necessary.
# It prints: "Justified: *********coding for beginners in easy steps"
# string.replace('s', '*'):

# This method replaces all occurrences of the character 's' with the '*' character in the string.
# It prints: "Replaced: coding for beginner* in ea*y tep"