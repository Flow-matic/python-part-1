def copy_sort( array ) :

    copy = array[ : ]
    sorted_copy = [ ]

    while len( copy ) > 0 :

        minimum = 0

        for element in range( 0 , len( copy ) ) :
            if copy[ element ] < copy[ minimum ] :
                minimum = element

        print( '\tRemoving' , copy[ minimum ] , \
                    'from' , copy )
        sorted_copy.append( copy.pop( minimum ) )

    return sorted_copy

array = [ 5 , 3 , 1 , 2 , 6 , 4 ]
print( 'Copy Sort...\nArray :' , array )

print( 'Copy :' , copy_sort( array ) )
print( 'Array :' , array )


# Copy Sort...
# Array : [5, 3, 1, 2, 6, 4]
       # Removing 1 from [5, 3, 1, 2, 6, 4]
       # Removing 2 from [5, 3, 2, 6, 4]
       # Removing 3 from [5, 3, 6, 4]
       # Removing 4 from [5, 6, 4]
       # Removing 5 from [5, 6]
       # Removing 6 from [6]
# Copy : [1, 2, 3, 4, 5, 6]
# Array : [5, 3, 1, 2, 6, 4]

# def copy_sort(array):: This line defines a function named copy_sort that takes an array as its argument.

# copy = array[:]: This line creates a copy of the input array using slicing. The copy variable will be used to work with the copy of the input array, leaving the original array unchanged.

# sorted_copy = []: This line initializes an empty list called sorted_copy, which will eventually store the sorted elements.

# while len(copy) > 0:: This line starts a while loop that continues as long as there are elements in the copy list.

# minimum = 0: This line initializes the minimum variable to 0, which will keep track of the index of the minimum element in the copy list.

# The for loop iterates over each element in the copy list to find the index of the minimum element:

# for element in range(0, len(copy)):
# Inside the loop, it checks if the current element (copy[element]) is less than the element at the current minimum index (copy[minimum]).
# If the current element is smaller, it updates the minimum variable to the index of the current element.
# print('\tRemoving', copy[minimum], 'from', copy): This line prints a message indicating that an element is being removed from the copy list. 
# It shows the element being removed and the current state of the copy list.

# sorted_copy.append(copy.pop(minimum)): This line removes the minimum element from the copy list using the pop method with the index minimum and appends it to the sorted_copy list.

# The loop continues until all elements have been sorted and moved from copy to sorted_copy.

# return sorted_copy: Once the while loop completes, the sorted_copy list containing the sorted elements is returned.

# array = [5, 3, 1, 2, 6, 4]: This line defines an example array.

# print('Copy Sort...\nArray:', array): This line prints a message indicating that the "Copy Sort" is about to begin and displays the original array.

# print('Copy:', copy_sort(array)): This line calls the copy_sort function with the array as an argument, prints the sorted copy of the array, and stores it in the sorted_copy list.

# print('Array:', array): This line prints the original array again. Note that the original array remains unchanged because the sorting operations were performed on the copy of the array.

# The output of this code will show the sorting process (removing elements from the copy and adding them to the sorted copy) and then display both the sorted copy and the original array.