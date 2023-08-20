for i in range( 1 , 4 ) :

    for j in range( 1 , 4 ) :
        if i == 2 and j == 1 :
            print( 'Breaks inner loop at i=2 j=1' )
            continue
        print( 'Running i =' , i , ' j =' , j )


# adding a break statement 
# Running i = 1  j = 1
# Running i = 1  j = 2
# Running i = 1  j = 3
# Breaks inner loop at i=2 j=1
# Running i = 3  j = 1
# Running i = 3  j = 2
# Running i = 3  j = 3

# adding a continue statement
# Running i = 1  j = 1
# Running i = 1  j = 2
# Running i = 1  j = 3
# Breaks inner loop at i=2 j=1
# Running i = 2  j = 2
# Running i = 2  j = 3
# Running i = 3  j = 1
# Running i = 3  j = 2
# Running i = 3  j = 3