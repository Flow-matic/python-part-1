basket = [ 'Apple' , 'Bun' , 'Cola' ]
crate = [ 'Egg' , 'Fig' , 'Grape' ]

print( 'Basket List:' , basket )
print( 'Basket Elements:' , len( basket ) )

basket.append( 'Damson' )
print( 'Appended:' , basket )
print( 'Last Item Removed:' , basket.pop( ) )
print( 'Basket List:' , basket )

basket.extend( crate )
print( 'Extend:' , basket )
del basket[ 1 ]
print( 'ItemRemoved:' , basket )
del basket[ 1 : 3 ]
print( 'SliceRemoved:' , basket )