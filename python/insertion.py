def insertion_sort( array ) :

    for index in range( 1 , len( array ) ) :

        value = array[ index ]

        while array[ index-1 ] > value and index >= 1 :
                array[ index ] = array[ index -1 ]
                index -= 1
        array[ index ] = value

        print( '\tResolving element[' , index , '] to' , array )

array = [5 , 3 , 1 , 2 , 6 , 4 ]
print( 'Insertion Sort...\nArray :' , array )

insertion_sort( array )
print( 'Array :' , array )


# Insertion Sort...
# Array : [5, 3, 1, 2, 6, 4]
#         Resolving element[ 0 ] to [3, 5, 1, 2, 6, 4]
#         Resolving element[ 0 ] to [1, 3, 5, 2, 6, 4]
#         Resolving element[ 1 ] to [1, 2, 3, 5, 6, 4]
#         Resolving element[ 4 ] to [1, 2, 3, 5, 6, 4]
#         Resolving element[ 3 ] to [1, 2, 3, 4, 5, 6]
# Array : [1, 2, 3, 4, 5, 6]