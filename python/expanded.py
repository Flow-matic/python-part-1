item = 0.70
rate = 1.05

tax = item * rate
total = item + tax

print( 'Item:\t', '{:.20f}'.format( item ) )
print( 'Tax:\t', '{:.20f}'.format( tax ) )
print( 'Total:\t', '{:.20f}'.format( total ) )


# Item:    0.69999999999999995559
# Tax:     0.73499999999999998668
# Total:   1.43500000000000005329

# item = 0.70: Assigns the item's price, which is 0.70.

# rate = 1.05: Assigns the tax rate, which is 1.05 (105%).

# tax = item * rate: Calculates the tax amount by multiplying the item price by the tax rate.

# total = item + tax: Calculates the total cost by adding the item price to the tax amount.

# print('Item:\t', '{:.20f}'.format(item)): Prints the item price with a very high precision of 20 decimal places, 
# formatted as a floating-point number with a width of 20. The \t is used for tabulation to align the output.

# print('Tax:\t', '{:.20f}'.format(tax)): Prints the tax amount with 20 decimal places, formatted similarly to the item price.

# print('Total:\t', '{:.20f}'.format(total)): Prints the total cost with 20 decimal places, formatted as a floating-point number with a width of 20.

# Keep in mind that displaying values with such high precision may not always be necessary, as it can lead to longer and less readable output. 
# The actual precision needed depends on the specific requirements of your application.