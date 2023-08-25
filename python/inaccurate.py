item = 0.70
rate = 1.05

tax = item * rate
total = item + tax

print( 'Item:\t', '{:.2f}'.format( item ) )
print( 'Tax:\t', '{:.2f}'.format( tax ) )
print( 'Total:\t', '{:.2f}'.format( total ) )


# Item:    0.70
# Tax:     0.73
# Total:   1.44

# item = 0.70: Assigns the item's price, which is 0.70.

# rate = 1.05: Assigns the tax rate, which is 1.05 (105%).

# tax = item * rate: Calculates the tax amount by multiplying the item price by the tax rate.

# total = item + tax: Calculates the total cost by adding the item price to the tax amount.

# print('Item:\t', '{:.2f}'.format(item)): Prints the item price with two decimal places, formatted as a floating-point number with a width of 2. 
# The \t is used for tabulation to align the output.

# print('Tax:\t', '{:.2f}'.format(tax)): Prints the tax amount with two decimal places, formatted similarly to the item price.

# print('Total:\t', '{:.2f}'.format(total)): Prints the total cost with two decimal places, formatted as a floating-point number with a width of 2.