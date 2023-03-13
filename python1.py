print('Hello World')

var = 8
print(var)
#8

var = 3.142
print(var)
# 3.142

var = True
print(var)
# True

# Initialise program status
running = True
print('run state', running)
# run state True

# Store Input
name = input('please enter your name')
print('Hi, name')
print('welcome to coding for beginners in easy steps')
print('remember to have fun', name, '!')
# Jonathan

# Controlling output
name = input( 'please enter your name: ' )
print( 'Hi ' + name , end=' ' )
print( '- welcome to coding for beginners in easy steps' )
print( 'remember to have fun ' + name + '!' )
# Sally

# Data types stored in the variables
race = 'Daytona 500' # string
print( race , 'is' , type( race ) )

kilo = 1000  # integer
print( kilo , 'is' , type( kilo ) )

temp = 98.6  # float
print( temp , 'is' , type( temp ) )

flag = True  # boolean
print( flag , 'is' , type( flag ) )

flag = 4 > 8  # boolean
print( flag , 'is' , type( flag ) )

# Converting data
num1 = input( 'please enter a whole number: ' )
num2 = input( 'now enter another whole number: ' )

print( 'input is: ' , type( num1 ) , type( num2 ) )

total = num1 + num2
print( 'total:' , total , type( total ) )

total = int( num1 ) + int( num2 )
print( 'total:' , total , type( total ) )

total = float( num1 ) + float( num2 )
print( 'total: ' + str( total ) , type( total ) )
# input is: <class 'str'> <class 'str'>
# total: 39 <class 'str'>
# total 12 <class 'int'>
# total 12.0 <class 'float'>
