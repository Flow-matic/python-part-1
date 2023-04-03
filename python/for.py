chars = [ 'A' , 'B' , 'C' ]
fruit = ( 'Apple' , 'Banana' , 'Cherry' )
info = { 'name' : 'Mike' , 'ref' : 'Python' , 'sys' : 'Win' }

print( 'Elements: \t' , end = ' ' )
for item in chars :
    print( item , end = ' ' )

print( '\nEnumerated:\t' , end = ' ' )
for item in enumerate( chars ) :
    print( item , end = ' ' )

print( '\nZipped: \t' , end = ' ' )
for item in zip( chars , fruit ) :
    print( item , end = ' ' )

print( '\nPaired:' )
for key , value in info.items( ) :
    print( key , '=' , value )

# Elements:        A B C 
# Enumerated:      (0, 'A') (1, 'B') (2, 'C') 
# Zipped:          ('A', 'Apple') ('B', 'Banana') ('C', 'Cherry') 
# Paired:
# name = Mike
# ref = Python
# sys = Win