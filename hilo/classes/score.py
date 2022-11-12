from card import card

""" Score calculator and game logic 
    
    Gets user input to make decisions and calulates score based on the decision made

    Attributes:
        -   score
        -   playerChoice
        -   lastCard
        -   currentCard
        
    """

class score():
    
    def __init__(self):
        """ Constructer for the game instance

            Args:
            - Self (an instance of the game)
        """
        self.currentScore = 300
        self.playerChoice = ''
        self.lastCard = card()
        self.currentCard = card()
        

    
    def getChoice(self):
        """ Gets the users choice
        
            Args:
            - Self (an instance of the game)
        """
        self.playerChoice = input("Higher or lower (h/l)? ")

    def updateScore(self):

        """ Updates the score by taking a guess and checking if higher or lower and updates the score
        
            Args:
            - Self (an instance of the game)
        """
        self.lastCard.generateValue()
        self.currentCard.generateValue()

        print(f'The card is: {self.lastCard.cardValue}' )
        self.getChoice()
        print(f'The next card was: {self.currentCard.cardValue}')
       

        if(self.playerChoice == "h" and self.currentCard.cardValue > self.lastCard.cardValue):
            self.currentScore = self.currentScore + 100
        elif(self.playerChoice == "h" and self.currentCard.cardValue < self.lastCard.cardValue):
            self.currentScore = self.currentScore -75
        elif(self.playerChoice == "l" and self.currentCard.cardValue > self.lastCard.cardValue):
            self.currentScore = self.currentScore - 75
        elif(self.playerChoice == "l" and self.currentCard.cardValue < self.lastCard.cardValue):
            self.currentScore = self.currentScore + 100
        self.lastCard.cardValue = self.currentCard.cardValue
        print(f'The score is: {self.currentScore}')



