from decimal import *

item = Decimal( 0.70 )
rate = Decimal( 1.05 )

tax = item * rate
total = item + tax

print( 'Item:\t' , '%.2f' % item )
print( 'Tax:\t' ,  '%.2f' % tax )
print( 'Total:\t',     '%.2f' % total )


# Item:    0.70
# Tax:     0.73
# Total:   1.43

# from decimal import *: Imports the decimal module, which allows you to work with arbitrary-precision decimal numbers.

# item = Decimal(0.70): Creates a Decimal object for the item's price, with a value of 0.70.

# rate = Decimal(1.05): Creates a Decimal object for the tax rate, with a value of 1.05 (105%).

# tax = item * rate: Calculates the tax amount by multiplying the Decimal objects item and rate. The result is a Decimal object with the precise value.

# total = item + tax: Calculates the total cost by adding the item and tax Decimal objects. Again, the result is a Decimal object with precise value.

# print('Item:\t', '%.2f' % item): Prints the item price with two decimal places using the % formatting operator. 
# This formatting specifies that the value should be displayed with exactly two decimal places.

# print('Tax:\t', '%.2f' % tax): Prints the tax amount with two decimal places using the same % formatting operator.

# print('Total:\t', '%.2f' % total): Prints the total cost with two decimal places using the % formatting operator.

# This code ensures that the values are displayed with two decimal places, and it maintains precision using the decimal module, 
# which is useful when working with financial calculations or any situation where precision matters.