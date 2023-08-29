from Bird import *

print( '\nClass Instances Of:\n' , Bird.__doc__ )

polly = Bird( 'Squawk, squawk!' )

print( '\nNumber Of Birds:' , Bird.count )
print( 'Polly Says:' , polly.talk( ) )

harry = Bird( 'Tweet, tweet!' )

print( '\nNumber Of Birds:' , Bird.count )
print( 'Harry Says:' , harry.talk( ) )


# Class Instances Of:
# A class to define bird properties.

# Number Of Birds: 1
# Polly Says: Squawk, squawk!

# Number Of Birds: 2
# Harry Says: Tweet, tweet!

# It imports all classes and functions from the 'Bird' module (assuming there is a file named 'Bird.py' in the same directory). 
# The * in from Bird import * imports everything from the 'Bird' module into the current namespace.

# It prints the docstring of the Bird class using Bird.__doc__. The docstring typically contains documentation or information about the class.

# It creates an instance of the Bird class named polly with the sound 'Squawk, squawk!'. This instance represents a bird that can "talk."

# It prints the number of bird instances created using Bird.count. The count attribute is a class-level variable that keeps track of how many bird instances have been created.

# It prints what 'Polly' says by calling the talk() method of the polly instance.

# It creates another instance of the Bird class named harry with the sound 'Tweet, tweet!'.

# It again prints the number of bird instances using Bird.count.

# It prints what 'Harry' says by calling the talk() method of the harry instance.

