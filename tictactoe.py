# This is a tic tac toe game in python 

# Choose X or O 
#player X chooses first space, that space goes from nothing to X 
#player O goes second, picks unoccupied space 
#whichever player gets three in a row or diagonal wins the game 
# if there is no winner there is a tie 


playerChoice = ""
playerChoice = input("Choose X or O. Player X goes first: ")


gameBoard = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
print(" ", "1", "2", "3")
print("1", gameBoard[0], gameBoard[1], gameBoard[2])
print("2", gameBoard[3], gameBoard[4], gameBoard[5])
print("3", gameBoard[6], gameBoard[7], gameBoard[8])

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

playerOneMove = input("Choose a space (example: 1,1): ")

gameBoard[coordMap[playerOneMove]] = "X"

print(" ", "1", "2", "3")
print("1", gameBoard[0], gameBoard[1], gameBoard[2])
print("2", gameBoard[3], gameBoard[4], gameBoard[5])
print("3", gameBoard[6], gameBoard[7], gameBoard[8])