#TicTacToe by Chris Peart

#Create starting variables
import math
div_string = "-+-+-"
height = 3
width = 3
board = []


for i in range(height):
    board.append([])
    for j in range(width):
        board[i].append(0)

def checkWin(board):
    #Horizontal check
    for i in range(height):
        if(board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0):
            if(board[i][0] == 1):
                print ("X wins the game")
                return True
            elif(board[i][0] == 2):
                print ("O wins the game")
                return True
        #Vertical check
    for i in range(width):
        if(board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0):
            if(board[0][i] == 1):
                print ("X wins the game")
                return True
            elif(board[0][i] == 2):
                print ("O wins the game")
                return True
    #Diagonal
    if(board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0):
            if(board[0][0] == 1):
                print ("X wins the game")
                return True
            elif(board[0][0] == 2):
                print ("O wins the game")
                return True
    #Diagonal part 2
    if(board[0][2] == board[1][1] == board[2][0] and board[0][0] != 0):
        if(board[0][2] == 1):
                print ("X wins the game")
                return True
        elif(board[0][2] == 2):
                print ("O wins the game")
                return True

    return False
    
    
def printBoard(board):
    boardString = ""
    finalString = ""
    counter = 0

    #Make board string that contains numbers and X or O
    for i in range(height):
        for j in range(width):

            counter += 1

            if(board[i][j] == 0):
                boardString = boardString + str(counter)

            elif(board[i][j] == 1):
                boardString = boardString + 'X'

            elif(board[i][j] == 2):
                boardString = boardString + 'O'
    boardString.split()

    counter = 0
    #From board string create a formatted string
    for i in range(height):
        for j in range(width):
            
            if j != (width-1):
                finalString = finalString + boardString[counter] + '|'
            else:
                finalString = finalString + boardString[counter]
            counter += 1
        if(i != height-1):
            finalString = finalString + "\n" + div_string + '\n'
    print(finalString)
        
def main():
    game = True
    turn = 1
    printBoard(board)
    while(game):
        #X's turn

        choice = int(input("x's turn to choose a square (1-9): "))
        if(choice <= 3):
            if board[math.ceil(choice/3) - 1][choice%4 - 1] == 0:
                board[math.ceil(choice/3) - 1][choice%4 - 1] = 1
                turn += 1
            else:
                print("Invalid choice, turn lost")
        elif (choice <7):
            if board[math.ceil(choice/3) - 1][choice%4] == 0:
                board[math.ceil(choice/3) - 1][choice%4] = 1
                turn += 1
            else:
                print("Invalid choice, turn lost")
        else:
            if board[math.ceil(choice/3) - 1][choice - 7] == 0:
                board[math.ceil(choice/3) - 1][choice - 7] = 1
                turn += 1
            else:
                print("Invalid choice, turn lost")
        printBoard(board)               
        if(checkWin(board)):
            game = False
            break
        if(turn == 9):
            game = False
            print ("Game over: DRAW")
            break

        #o's turn
        choice = int(input("o's turn to choose a square (1-9): "))
        if(choice <= 3):
            if board[math.ceil(choice/3) - 1][choice%4 - 1] == 0:
                board[math.ceil(choice/3) - 1][choice%4 - 1] = 2
                turn += 1
            else:
                print("Invalid choice, turn lost")
        elif (choice <7):
            if board[math.ceil(choice/3) - 1][choice%4] == 0:
                board[math.ceil(choice/3) - 1][choice%4] = 2
                turn += 1
            else:
                print("Invalid choice, turn lost")
        else:
            if board[math.ceil(choice/3) - 1][choice - 7] == 0:
                board[math.ceil(choice/3) - 1][choice - 7] = 2
                turn += 1
            else:
                print("Invalid choice, turn lost")
        printBoard(board)   
        if(checkWin(board)):
            game = False
            break


main()







# 1|2|3
# -+-+-
# 4|5|6
# -+-+-
# 7|8|9