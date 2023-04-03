info = { 'name' : 'Bob' , 'ref' : 'Python' , 'sys' : 'Win' }
print( 'info:' , type( info ) )
print( 'Dictionary:' , info )

print( '\nReference:' , info[ 'ref' ] )

print( '\nKeys:' , info.keys( ) )

del info[ 'name' ]
info[ 'user' ] = 'Tom'
print( '\nDictionary:' , info )

print( '\nIs There A name Key?:' ,'name' in info )

# info: <class 'dict'>
# Dictionary: {'name': 'Bob', 'ref': 'Python', 'sys': 'Win'}
 
# Reference: Python
 
# Keys: dict_keys(['name', 'ref', 'sys'])
 
# Dictionary: {'ref': 'Python', 'sys': 'Win', 'user': 'Tom'}
 
# Is There A name Key?: False

# Naming elements

# Variable = stores a single value

# List = stores multiple values in an ordered index

# Tuple = stores multiple unique values in an unordered collection

# Dictionary = stores multiple unordered key:value pairs