i = 1

while i < 4 :
    print( 'Outer Loop Iteration:' , i )
    i += 1

    j = 1
    while j < 4 :
        print( '\tInner Loop Iteration:' , j )
        j += 1

# Outer Loop Iteration: 1
#         Inner Loop Iteration: 1
#         Inner Loop Iteration: 2
#         Inner Loop Iteration: 3
# Outer Loop Iteration: 2
#         Inner Loop Iteration: 1
#         Inner Loop Iteration: 2
#         Inner Loop Iteration: 3
# Outer Loop Iteration: 3
#         Inner Loop Iteration: 1
#         Inner Loop Iteration: 2
#         Inner Loop Iteration: 3