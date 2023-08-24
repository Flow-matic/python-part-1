def selection_sort( array ) :

    for index in range( 0 , len( array ) -1 ) :
        value = array[ index ]
        current = index

        for element in range( index+1 , len( array ) ) :
            if array[ element ] < array[ current ] :
                current = element

        array[ index ] = array[ current ]
        array[ current ] = value
        print( '\tResolving element[' , index , '] to ' , array )
array = [ 5 , 3 , 1 , 2 , 6 , 4 ]
print( 'Selection Sort...\nArray :' , array )

selection_sort( array )
print( 'Array :' , array )


# Selection Sort...
# Array : [5, 3, 1, 2, 6, 4]
   #    Resolving element[ 0 ] to  [1, 3, 5, 2, 6, 4]
   #    Resolving element[ 1 ] to  [1, 2, 5, 3, 6, 4]
   #    Resolving element[ 2 ] to  [1, 2, 3, 5, 6, 4]
   #    Resolving element[ 3 ] to  [1, 2, 3, 4, 6, 5]
   #    Resolving element[ 4 ] to  [1, 2, 3, 4, 5, 6]
# Array : [1, 2, 3, 4, 5, 6]

# Selection Sort algorithm in Python. Selection Sort is a simple sorting algorithm that works by repeatedly selecting the minimum element from an unsorted part of the array and putting it at the beginning. 
# Here's what each part of the code does:

# Function Definition: The code defines a function called selection_sort that takes an array as its parameter.

# Outer Loop: The outer loop iterates through the array from the first element (index 0) to the second-to-last element (index len(array) - 1). 
# It selects each element in the array one by one.

# Initialization: Inside the outer loop, it initializes value with the value of the current element (array[index]) and current with the index of the current element.

# Inner Loop: There's an inner loop that starts from the element after the current element (index + 1) and goes to the end of the array. 
# This inner loop is used to find the index of the smallest element in the remaining unsorted portion of the array.

# Comparison: In the inner loop, it compares the value of the element at the current index (array[element]) with the value of the element at the current index (array[current]). 
# If the element being considered in the inner loop is smaller than the current minimum element (array[element] < array[current]), 
# it updates current to be the index of the smaller element.

# Swap: After the inner loop completes, it performs a swap operation. It swaps the value of the current element (array[index])
# with the smallest element found in the inner loop (the element at array[current]). This places the smallest element in its correct sorted position.

# Print: It prints the array after each swap operation to visualize how the sorting is progressing.

# Array Initialization: An array named array is defined with some initial values [5, 3, 1, 2, 6, 4].

# Sorting: The selection_sort function is called with the array as an argument, effectively sorting the array using the Selection Sort algorithm.

# Print Sorted Array: Finally, it prints the sorted array after the sorting process is complete.

# So, the code is demonstrating the Selection Sort algorithm by sorting the array in ascending order and printing the array
# at each step to show how the elements are swapped to achieve the sorted order.

# An array is a fundamental data structure in computer programming and computer science. 
# It is a collection of elements, each identified by an index or a key. Arrays are used to store and organize a fixed-size sequence of elements of the same data type. 
# Here are some key characteristics of arrays:

# Ordered Collection: Arrays maintain the order of elements, which means that elements are stored in a specific sequence, 
# and you can access them based on their position within the array.

# Fixed Size: Arrays typically have a fixed size, meaning that you must specify the number of elements the array can hold when it is created. 
# In most programming languages, this size cannot be changed after creation.

# Homogeneous Elements: In most programming languages, arrays can only hold elements of the same data type. For example, 
# you can have an array of integers, an array of characters, or an array of floating-point numbers, but not a mix of different data types in the same array.

# Zero-Based Indexing: Many programming languages use zero-based indexing for arrays. This means that the first element is accessed using index 0, 
# the second element with index 1, and so on.

# Here's an example of an array in Python:

# python
# my_array = [10, 20, 30, 40, 50]
# In this example, my_array is an array of integers containing five elements. You can access elements in the array using their index. 
# For instance, my_array[0] would give you the value 10, and my_array[3] would give you 40.

# Arrays are widely used in programming for tasks such as storing and manipulating collections of data, implementing data structures like lists, queues, and stacks, 
# and for various algorithmic operations like sorting and searching.

# In Python, len(array) is a built-in function that returns the number of elements in a given iterable, including lists, tuples, strings, and other collection-like objects. When you use len(array), it will return the length or the count of items in the specified iterable.

# For example, if you have a list called array:

# python
# array = [5, 3, 1, 2, 6, 4]
# You can use len(array) to determine how many elements are in this list:

# length = len(array)
# print(length)  # This will print 6, as there are six elements in the list.
# So, len(array) is a convenient way to find out the size or length of an iterable in Python.