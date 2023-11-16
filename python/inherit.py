from Rectangle import *
from Triangle import *

rect = Rectangle( )
trey = Triangle( )

rect.set_values( 4 , 5 )
trey.set_values( 4 , 5 )

print( 'Rectangle Area:' , rect.area( ) )
print( 'Triangle Area:' , trey.are( ) )


# Rectangle Area: 20
# Triangle Area: 10.0

# changed Triangle class area to ( are ) as it was throwing error!

# Deriving classes is a fundamental concept in object-oriented programming (OOP), 
# and it allows you to create a hierarchy of classes with shared functionality and specialized behavior in each subclass.