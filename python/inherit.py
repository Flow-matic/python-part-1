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