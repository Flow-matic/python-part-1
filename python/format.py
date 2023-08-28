snack = '{} and {}'.format( 'Burger' , 'Fries' )

print( '\nReplaced:' , snack )

snack = '{1} and {0}'.format( 'Burger' , 'Fries' )

print( 'Replaced:' , snack )

snack = '%s and %s' % ( 'Milk' , 'Cookies' )

print( '\nSubstituted:' , snack )


# Replaced: Burger and Fries
# Replaced: Fries and Burger

# Substituted: Milk and Cookies


# snack = '{} and {}'.format('Burger', 'Fries'):

# This line uses the format() method to create a string where '{}' is a placeholder for values. It then uses the format() method to substitute 'Burger' and 'Fries' into these placeholders.
# After this line, snack contains the string 'Burger and Fries'.
# print('\nReplaced:', snack):

# This line prints the value of snack, which is 'Burger and Fries', preceded by 'Replaced:' and a newline character.
# snack = '{1} and {0}'.format('Burger', 'Fries'):

# This line uses the format() method again, but this time it specifies the positions of the arguments in the placeholders using {0} and {1}. So, 'Burger' is placed at position 1 and 'Fries' at position 0.
# After this line, snack contains the string 'Fries and Burger'.
# print('Replaced:', snack):

# This line prints the value of snack, which is now 'Fries and Burger', preceded by 'Replaced:'.
# snack = '%s and %s' % ('Milk', 'Cookies'):

# This line uses the old-style string formatting with % placeholders. It substitutes 'Milk' into the first %s and 'Cookies' into the second %s.
# After this line, snack contains the string 'Milk and Cookies'.
# print('\nSubstituted:', snack):

# This line prints the value of snack, which is 'Milk and Cookies', preceded by 'Substituted:' and a newline character.