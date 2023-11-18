from Man import *
from Hombre import *

guy_1 = Man( 'Richard' )
guy_2 = Hombre( 'Ricardo' )

guy_1.speak( 'It\'s a beautiful evening.\n' )
guy_2.speak( 'Es una tarde hermosa.\n' )

Person.speak( guy_1 )
Person.speak( guy_2 )


# Richard :
        # Hello! It's a beautiful evening.

# Ricardo :
       # Hola! Es una tarde hermosa.

# Richard (Calling The Base Class)
# Ricardo (Calling The Base Class)

# Method overriding is a powerful feature that promotes code reusability and allows for more flexible and dynamic behavior in a program