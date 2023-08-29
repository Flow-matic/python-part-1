'''
An excerpt from The Ballad of Reading Gaol.
'''
poem = 'I never saw a man who looked\n'
poem += 'With such a wistful eye\n'
poem += 'Upon that little tent of blue\n'
poem += 'Which prisoners call the sky\n'

file = open( 'poem.txt' , 'w' )

file.write( poem )
file.close( )

file = open( 'poem.txt' , 'r' )

for line in file :
    print( line , end = '' )
file.close( )

file = open( 'poem.txt' , 'a' )
file.write( '(Oscar Wilde)' )
file.close( )


# I never saw a man who looked
# With such a wistful eye
# Upon that little tent of blue
# Which prisoners call the sky

# Constructs a poem as a string and stores it in the variable poem.
# Opens a file named 'poem.txt' in write mode ('w') and writes the poem to it.
# Closes the file.
# Reopens the 'poem.txt' file in read mode ('r') and prints each line from the file.
# Closes the file.
# Reopens the 'poem.txt' file in append mode ('a') and appends the text '(Oscar Wilde)' to it.
# Closes the file again.
# This script essentially writes the poem to a text file, reads and prints it, and then appends '(Oscar Wilde)' to the end of the file