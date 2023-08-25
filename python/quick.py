def quick_sort( array ) :
    if len( array ) > 1 :
        pivot = int( len( array ) -1 )
        less = [ ] ; more =[ ]

        for element in range( len( array ) ) :
            value = array[ element ]
            if element != pivot :
                if value < array[ pivot ] :
                    less.append( value )
                else :
                    more.append( value )

        quick_sort( less ) ; quick_sort( more )
        print( '\tLess:' , less , '\tPivot:' , array[ pivot ] , \
            '\tMore:' , more )
        array[ : ] = less + [ array[ pivot] ] + more
        print( '\t\t...Merged:' , array )

array = [ 5 , 3, 1, 2, 6, 4 ]
print( 'Quick Sort...\nArray :' , array )
quick_sort( array )
print( 'Array :' , array )


# Quick Sort...
# Array : [5, 3, 1, 2, 6, 4]
#        Less: [1]       Pivot: 2        More: [3]
#                ...Merged: [1, 2, 3]
#        Less: [5]       Pivot: 6        More: []
#                ...Merged: [5, 6]
#        Less: [1, 2, 3]         Pivot: 4        More: [5, 6]
#                ...Merged: [1, 2, 3, 4, 5, 6]
# Array : [1, 2, 3, 4, 5, 6]


# The quick_sort function takes an array as input.

# Inside the quick_sort function:

# It first checks if the length of the input array is greater than 1, as quicksort is only performed on arrays with more than one element.

# It selects the pivot element as the last element in the array (index len(array) - 1).

# It initializes two empty lists: less and more, which will be used to store elements less than and greater than the pivot, respectively.

# It iterates through each element in the array (except for the pivot element) and adds elements to either the less or more list based on whether they are less than or greater than the pivot element.

# It recursively calls the quick_sort function on both the less and more lists.

# It prints the content of the less list, the pivot element, and the content of the more list to show the partitioning process.

# Finally, it updates the original array by concatenating less, the pivot element, and more. This effectively sorts the array.

# It prints the merged array after the partitioning and sorting process.

# An initial array [5, 3, 1, 2, 6, 4] is defined.

# The code prints "Quick Sort..." and the original array:

# mathematica
# Quick Sort...
# Array : [5, 3, 1, 2, 6, 4]
# The quick_sort function is called with the original array as an argument.

# Inside the quick_sort function, the array is recursively partitioned and sorted.

# After the quick_sort function completes, the sorted array becomes [1, 2, 3, 4, 5, 6].

# The code prints the final sorted array:
