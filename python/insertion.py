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

# Function Definition: The code defines a function called insertion_sort that takes an array as its parameter.

# Outer Loop: The outer loop iterates through the elements of the array starting from the second element (index 1) and going to the last element (index len(array) - 1). 
# This loop considers each element to insert it into its correct position within the sorted portion of the array.

# Element Selection: Inside the outer loop, it selects the current element to be considered for insertion. This element is stored in the variable value.

# Inner While Loop: It enters a while loop that continues as long as the current element (array[index]) is greater than the element immediately before it (array[index - 1])
#  and index is greater than or equal to 1. This while loop is used to shift elements to the right to make room for the value to be inserted in its correct sorted position.

# Element Shifting: Inside the while loop, it shifts the element at array[index - 1] to the right by assigning array[index] to array[index - 1]. It also decrements index by 1.

# Insertion: After the while loop completes, it assigns the value to array[index], effectively inserting the value into its correct sorted position within the array.

# Print: It prints the array after each insertion operation to visualize how the sorting is progressing.

# Array Initialization: An array named array is defined with some initial values [5, 3, 1, 2, 6, 4].

# Sorting: The insertion_sort function is called with the array as an argument, effectively sorting the array using the Insertion Sort algorithm.

# Print Sorted Array: Finally, it prints the sorted array after the sorting process is complete.

# So, the code demonstrates the Insertion Sort algorithm by sorting the array in ascending order and printing the array
#  at each step to show how the elements are inserted into their correct positions to achieve the sorted order.