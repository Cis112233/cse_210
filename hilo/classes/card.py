from random import randint

"""Card creater and picker 
    
    The card class generates a new card with a value from 1 to 13

    Attributes:
        - cardValue
        -
        -
        
"""
class card():

    def __init__(self):
        self.cardValue = 0
    
    def generateValue(self):
        self.cardValue = randint(1,13)
        
        