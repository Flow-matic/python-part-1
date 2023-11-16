from Bird import *

chick = Bird( 'Cheep, cheep!' )
chick.age = '1 week'

print( '\nChick Says:' , chick.talk( ) )
print( 'Chick Age:' , chick.age )

chick.age = '2 weeks'
print( 'Chick Now:' , chick.age )

setattr( chick , 'age' , '3 weeks' )

print( '\nChick Attributes...' )
for attrib in dir( chick ) :
    if attrib[0] != '_' :
        print( attrib , ':' , getattr( chick , attrib ) )

delattr( chick , 'age' )
print( '\nChick age Attribute?' , hasattr( chick , 'age' ) )


# Chick Says: Cheep, cheep!
# Chick Age: 1 week
# Chick Now: 2 weeks

# Chick Attributes...
# age : 3 weeks
# count : 1
# sound : Cheep, cheep!
# talk : <bound method Bird.talk of <Bird.Bird object at 0x7f2faa8abfe0>>

# Chick age Attribute? False