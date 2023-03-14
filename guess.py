import random    # random library class provides random number generator function

num = random.randint( 1, 20 )    # randint() function specifies an upper and lower range whitin the parentheses
flag = True
guess = 0

print( 'guess my number 1-20 : ' , end = ' ' )

while flag:                 # while flag remains True

    guess = input( )

    if not guess.isdigit( ) :
        print( 'invalid! enter only digits 1-20' )
    elif int( guess ) < num :
        print( 'too low, try again : ' , end= ' ' )
    elif int( guess ) > num :
        print( 'too high, try again : ' , end = ' ' )
    else:
        print( 'correct... my number is ' + guess )
        flag = False