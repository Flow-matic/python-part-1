party_goers = { 'Andrew' , 'Barbara' , 'Carole' , 'David' }
print( 'party_goers:' , type( party_goers ) )

print( 'Did David go to the party?' , 'David' in party_goers )
print( 'Did Kelly go to the party?' , 'Kelly' in party_goers )

students = { 'Andrew' , 'Kelly' , 'Lynn' , 'David' }

commons = party_goers.intersection( students )

party_students = list( commons )

print( 'Students at the party:' , party_students )
print( 'First student at the party:' , party_students[ 0 ] )

# party_goers: <class 'set'>
# Did David go to the party? True
# Did Kelly go to the party? False
# Students at the party: ['Andrew', 'David']
# First student at the party: Andrew