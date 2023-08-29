text = 'The political slogan "Workers Of The World Unite!" \n'
text += 'is from The Communist Manifesto.'

with open( 'update.txt' , 'w' ) as file :
    file.write( text )
    print( '\nFile Now Closed?:' , file.closed )

print( 'File Now Closed?:' , file.closed )

with open( 'update.txt' , 'r+' ) as file :
    text = file.read()
    print( '\nString:' , text )

    print( '\nPosition In File Now:' , file.tell() )
    position = file.seek( 33 )
    print( 'Position In File Now:' , file.tell() )

    file.write( 'All Lands' )

    file.seek( 61 )
    file.write( 'the tombstone of Karl Marx.' )

    file.seek( 0 )
    text = file.read()
    print( '\nString:' , text )



# File Now Closed?: False
# File Now Closed?: True

# String: The political slogan "Workers Of The World Unite!" 
# is from The Communist Manifesto.

# Position In File Now: 84
# Position In File Now: 33

# String: The political slogan "Workers Of All Lands Unite!" 
# is from Tthe tombstone of Karl Marx.

# It writes the text you provided to a file named 'update.txt'.

# It checks whether the file is closed using the file.closed attribute and prints the result.

# It then opens the same file in 'r+' (read and write) mode.

# Reads the content of the file.

# Uses file.tell() to determine the current position in the file and prints it.

# Uses file.seek() to move the cursor to specific positions in the file.

# Writes 'All Lands' starting from position 33 in the file.

# Writes 'the tombstone of Karl Marx.' starting from position 61 in the file.

# Moves the cursor to the beginning of the file using file.seek(0) and reads the entire content of the file.