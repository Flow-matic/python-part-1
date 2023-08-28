file = open( 'example.txt' , 'w' )

print( 'File Name:' , file.name )
print( 'File Open Mode:' , file.mode )

print( 'Readable:' , file.readable( ) )
print( 'Writable:' , file.writable( ) )

def get_status( f ) :
    if not f.closed :
        return 'Open'
    else :
        return 'Closed'

print( 'File Status:' , get_status( file ) )
file.close()
print( '\nFile Status:' , get_status( file ) )


# File Name: example.txt
# File Open Mode: w
# Readable: False
# Writable: True
# File Status: Open

# File Status: Closed

# file = open('example.txt', 'w'):

# This line opens a file named 'example.txt' in write mode ('w'). If the file does not exist, it will be created. If it does exist, its previous content will be erased.
# The file variable now represents the opened file.
# print('File Name:', file.name):

# This line prints the name of the file, which should be 'example.txt'.
# print('File Open Mode:', file.mode):

# This line prints the mode in which the file was opened, which should be 'w' for write mode.
# print('Readable:', file.readable()):

# This line checks if the file is readable and prints False because the file was opened in write mode, which does not allow reading.
# print('Writable:', file.writable()):

# This line checks if the file is writable and prints True because the file was opened in write mode, which allows writing.
# def get_status(f)::

# This line defines a function get_status that takes a file object f as its argument.
# if not f.closed::

# This line checks if the file represented by the f object is not closed.
# return 'Open':

# If the file is not closed, this line returns 'Open' from the get_status function.
# else::

# If the file is closed, this line is executed.
# return 'Closed':

# This line returns 'Closed' from the get_status function.
# print('File Status:', get_status(file)):

# This line prints the status of the file, which should be 'Open' because the file was opened earlier.
# file.close():

# This line closes the file.
# print('\nFile Status:', get_status(file)):

# This line prints the status of the file again, which should now be 'Closed' because the file was explicitly closed using file.close().