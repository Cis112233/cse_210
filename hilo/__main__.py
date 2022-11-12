
from classes.score import score


a = score()
while(a.currentScore):
    a.updateScore()
    if((input("Play again (y/n)? ") == 'n')):
        break