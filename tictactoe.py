# This is a tic tac toe game in python 

# Choose X or O 
#player X chooses first space, that space goes from nothing to X 
#player O goes second, picks unoccupied space 
#whichever player gets three in a row or diagonal wins the game 
# if there is no winner there is a tie 

playerChoice = ""

gameBoard = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

coordMap = {
    "1,1": 0,
    "1,2": 1,
    "1,3": 2,
    "2,1": 3,
    "2,2": 4,
    "2,3": 5,
    "3,1": 6,
    "3,2": 7,
    "3,3": 8
}

def checkForWin(board):
    if board[0] != "_" and board[0] == board[1] == board[2]:
        return True
    if board[3] != "_" and board[3] == board[4] == board[5]:
        return True
    if board[6] != "_" and board[6] == board[7] == board[8]:
        return True 
    if board[0] != "_" and board[0] == board[3] == board[6]:
        return True
    if board[1] != "_" and board[1] == board[4] == board[7]:
        return True
    if board[2] != "_" and board[2] == board[5] == board[8]:
        return True
    if board[0] != "_" and board[0] == board[1] == board[2]:
         return True
    if  board[2] != "_" and board[2] == board[4] == board[6]:
         return True
    return False

def displayGameBoard(board):  
    print(" ", "1", "2", "3")
    print("1", board[0], board[1], board[2])
    print("2", board[3], board[4], board[5])
    print("3", board[6], board[7], board[8])

playerChoice = input("Choose X or O. Player X goes first: ")

displayGameBoard(gameBoard)



while checkForWin(gameBoard) == False: 
    playerOneMove = input("Player X choose a space (example: 1,1): ")

    gameBoard[coordMap[playerOneMove]] = "X"

    displayGameBoard(gameBoard)

    if checkForWin(gameBoard): 
        print("Player X Wins")
        break

    playerTwoMove = input("Player O choose a space (example: 1,1): ")

    gameBoard[coordMap[playerTwoMove]] = "O"

    displayGameBoard(gameBoard)

    if checkForWin(gameBoard):  
        print("Player O Wins")
        break


       
