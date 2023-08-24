def bubble_sort( array ) :

    for index in range( len( array ) ) :

        for element in range( ( len( array )-1 ) - index ) :
            if array[ element ] > array[ element + 1 ] :
                array[ element ] , array[ element+1 ] = \
                    array[ element+1 ] , array[ element ]

        print( '\tResolving element[' , element , '] to ' , array )

array = [ 5 , 3 , 1 , 2 , 6 , 4 ]
print( 'Bubble Sort...\nArray :' , array )

bubble_sort( array )
print( 'Array :' , array )


# Bubble Sort...
# Array : [5, 3, 1, 2, 6, 4]
#         Resolving element[ 4 ] to  [3, 1, 2, 5, 4, 6]
#         Resolving element[ 3 ] to  [1, 2, 3, 4, 5, 6]
#         Resolving element[ 2 ] to  [1, 2, 3, 4, 5, 6]
#         Resolving element[ 1 ] to  [1, 2, 3, 4, 5, 6]
#         Resolving element[ 0 ] to  [1, 2, 3, 4, 5, 6]
#         Resolving element[ 0 ] to  [1, 2, 3, 4, 5, 6]
# Array : [1, 2, 3, 4, 5, 6]

# An array named array is defined with initial values [5, 3, 1, 2, 6, 4].

# It prints the message "Bubble Sort..." and the initial array, like this:

# mathematica
# Bubble Sort...
# Array : [5, 3, 1, 2, 6, 4]
# It calls the bubble_sort function with the array as an argument.

# Inside the bubble_sort function:

# It iterates through the elements of the array using the index variable.

# Within the outer loop, it iterates through the elements from the beginning of the array up to (len(array) - 1 - index) using the element variable.

# It compares adjacent elements: array[element] and array[element + 1]. If the element at element is greater than the element at element + 1,
#  it swaps them to move the larger element toward the end of the array.

# It prints the current state of the array after each swap operation, showing the progress of the sorting process.

# After the sorting process is complete, it prints the message "Array :" followed by the sorted array, like this:

# Array : [1, 2, 3, 4, 5, 6]
# In summary, the code is using the Bubble Sort algorithm to sort the array in ascending order and displaying the array at each step
#  to visualize how elements are being compared and swapped to achieve the sorted order. Bubble Sort repeatedly compares and swaps adjacent elements until the entire array is sorted.