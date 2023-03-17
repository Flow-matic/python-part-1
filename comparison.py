nil = 0
num = 0
top = 1
cap = 'A'  # The inicode value for uppercase "A" is 65 but for lowercase "a" it's 97 so their comparison returns False.
low = 'a'  # A-Z uppercase characters have unicode values 65-90 and a-z lowercase characters have unicode values 97-122.

print( 'Equality :\t\t' , nil , '==' , num , nil == num )
print( 'Equality :\t \t' , cap , '==' , low , cap == low )
print( 'Inequality :\t' , nil , '!=' , top , nil != top )

print( 'Greater :\t\t' , nil , '>' , top , nil > top )
print( 'Lesser :\t\t' , nil , '<' , top , nil < top )

print( 'More or Equal :\t' , nil , '>=' , num , nil >= num )
print( 'Less or Equal :\t' , top , '<=' , num , top <= num )

# The \t escape sequence  shown here adds an invisible  tab character  to format the output.