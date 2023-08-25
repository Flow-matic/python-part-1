import sys , keyword

print( ' Python Version:' , sys.version )

print( 'Python Interpreter Location:' , sys.executable )

print( 'Python Module Search Path: ' )
for folder in sys.path :
    print( folder )

print( 'Python Keywords: ' )
for word in keyword.kwlist :
    print( word )


# Python Keywords: 
# False
# None
# True
# and
# as
# assert
# async
# await
# break
# class
# continue
# def
# del
# elif
# else
# except
# finally
# for
# from
# global
# if
# import
# in
# is
# lambda
# nonlocal
# not
# or
# pass
# raise
# return
# try
# while
# with
# yield

# import sys, keyword: This line imports two Python modules, sys and keyword, which are used later in the script.

# print('Python Version:', sys.version): This line prints the version of Python you are using. It uses sys.version to access this information.

# print('Python Interpreter Location:', sys.executable): This line prints the location of the Python interpreter executable that is currently running the script. 
# It uses sys.executable to access this information.

# print('Python Module Search Path:'): This line prints a header indicating that the following lines will display the Python module search path.

# for folder in sys.path:: This is a for loop that iterates over each entry in the sys.path list. sys.
# path is a list of directory names where Python looks for modules when you try to import them.

# print(folder): This line inside the loop prints each folder in the module search path.

# print('Python Keywords:'): This line prints a header indicating that the following lines will display the list of Python keywords.

# for word in keyword.kwlist:: This is another for loop that iterates over each keyword in the keyword.kwlist list. 
# These are Python's reserved keywords that have special meanings and cannot be used as variable names or identifiers.

# print(word): This line inside the loop prints each keyword one by one.