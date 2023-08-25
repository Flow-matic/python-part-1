def merge_sort( array ) :

    if len( array ) > 1 :
        middle = int( len( array ) / 2 )
        left = array[ 0 : middle ] ; right = array[ middle : ]
        print( '\tSplit to' , left , right )
        merge_sort( left ) ; merge_sort( right )

        i = j = 0
        for element in range( len( array ) ) :

            L = left[ i ] if i < len( left ) else None
            R = right[ j ] if j < len( right ) else None

            if ( ( L and R ) and ( L < R ) ) or R is None :
                array[ element ] = L ; i += 1
            elif ( ( L and R ) and ( L >= R ) ) or L is None :
                array[ element ] = R ; j += 1
        print( '\t\tMerging' , left , right )

array = [ 5 , 3 , 1 , 2 , 6 , 4 ]
print( 'Merge Sort...\nArray :' , array )

merge_sort( array )
print( 'Array :' , array )


# Merge Sort...
# Array : [5, 3, 1, 2, 6, 4]
#         Split to [5, 3, 1] [2, 6, 4]
#         Split to [5] [3, 1]
 #        Split to [3] [1]
 #               Merging [3] [1]
 #               Merging [5] [1, 3]
 #        Split to [2] [6, 4]
 #        Split to [6] [4]
 #                Merging [6] [4]
  #               Merging [2] [4, 6]
  #               Merging [1, 3, 5] [2, 4, 6]
# Array : [1, 2, 3, 4, 5, 6]

# Here's what the code is doing step by step:

# It defines a function called merge_sort that takes an input array as its argument.

# Inside the merge_sort function:

# It checks if the length of the input array is greater than 1. If not, it means the array is already sorted, so there's no need to perform any sorting.

# If the length of the array is greater than 1, it calculates the middle index of the array (middle), effectively dividing the array into two halves.

# It then creates two sub-arrays: left, which contains elements from the start of the original array up to the middle index, and right, 
# which contains elements from the middle index to the end of the original array.

# It prints the split sub-arrays left and right to show the division.

# It initializes two pointers, i and j, to 0, which will be used to iterate through the left and right sub-arrays.

# It enters a loop that will run for as many iterations as there are elements in the original array.

# Inside the loop, it compares the elements at the current positions i and j in the left and right sub-arrays, respectively, 
# and assigns the smaller of the two elements to the current position in the original array.

# It then increments the pointer for the sub-array from which the element was chosen.

# After the loop, it prints the merged sub-arrays left and right to show the merging process.

# It defines an initial array with unsorted elements [5, 3, 1, 2, 6, 4].

# It prints the original unsorted array.

# It calls the merge_sort function with the original array as an argument, which sorts the array using the merge sort algorithm.

# It prints the sorted array.