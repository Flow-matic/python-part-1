from Person import *

class Hombre( Person ) :

        """Aderived class to define Hombre properties."""
        def speak( self , msg ) :
            print( self.name , ':\n\tHola!' , msg )