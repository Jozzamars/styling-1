import random
import copy
board = [[0,0,2,2], [2,2,2,0],[4,0,0,4], [0,2,0,0]]
boardSize = 4

def display():

    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element

    numSpaces = len(str(element))

    for row in board:
        currRow = "|"
        for element in row:

            if element == 0:
                currRow += " " * numSpaces + "|"

            else:
                currRow += (" " * (numSpaces - len(str(element)))) + str(element) + "|"

        print(currRow)
    print()

display()    

def mergeOneRowL(row):

    for j in range(boardSize -1):
      for i in range(boardSize -1, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0

    for i in range(boardSize - 1):

        if row[i] == row[i + 1]:
            row[i] *2
            row[i + 1] = 0

    for i in range(boardSize - 1, 0, -1):
        if row[i -1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row

def merge_left(currentBoard):

    for i in range(boardSize):
        currentBoard[i] = mergeOneRowL(currentBoard[i])

    return currentBoard 

def reverse(row):
    
    new = []
    for i in range(boardSize - 1, -1, -1):
        new.append(row[i])
    return new 

def merge_right(currentBoard):

    for i in range(boardSize):

        currentBoard[i] = reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowL(currentBoard[i])
        currentBoard[i] = reverse(currentBoard[i])
    return currentBoard


def transpose(currentBoard):
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i == j:
                temp = currentBoard[j][i]
                currentBoard[j][i] = currentBoard[i][j]
                currentBoard[i][j] = temp
    return currentBoard            

def merge_up(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = merge_left(currentBoard)
    currentBoard = transpose(currentBoard)
    
    return currentBoard

def merge_down(currentBoard):

    currentBoard = transpose(currentBoard)
    currentBoard = merge_right(currentBoard)
    currentBoard = transpose(currentBoard)

    return currentBoard

def pickNewValue():
    if random.randint(1, 8) == 1:
        return 4
    else:
        return 2
    
def addNewValue():
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)

    while not board[rowNum][colNum] == 0:
        rowNum = random.randint(0, boardSize - 1)
        colNum = random.randint(0, boardSize - 1)

    board[rowNum][colNum] = pickNewValue()

def won():
    for row in board:
        if 2048 in row:
            return True
    return False

def noMoves():

    tempBoard1 = copy.deepcopy(board)
    tempBoard2 = copy.deepcopy(board)

    tempBoard1 = merge_down(tempBoard1)
    if tempBoard1 == tempBoard2:
        tempBoard1 = merge_up(tempBoard1)
        if tempBoard1 == tempBoard2:
            tempBoard1 = merge_left(tempBoard1)
            if tempBoard1 == tempBoard2:
                tempBoard1 = merge_right(tempBoard1)
                if tempBoard1 == tempBoard2:
                    return True
    return False


board = []
for i in range(boardSize):
    row = []
    for j in range(boardSize):
        row.append(0)
    board.append(row)

numNeeded = 2
while numNeeded > 0:
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)

    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = pickNewValue()
        numNeeded -=1
    print("Welcome to 2048! Your goal is to combine values to get the number 2048, by merging the board in different directions.You will need to type 'd' to merge rignt, 'w' to merge up, 'a' to merge left, 's' to merge down. \n\n Here is the starting board:")
display()

gameOver = False

while not gameOver: 
    move = input("Which way you want to move?")

    validInput = True

    tempBoard = copy.deepcopy(board)

    if move == "d":
        board = merge_right(board)
    elif move == "w":
        board = merge_up(board)
    elif move == "a":
        board = merge_left(board)
    elif move == "s":
        board = merge_down(board)
    else:
        validInput = False

    if not validInput:
        print("You enter was not valid, Try again")
    else:
       
       if board == tempBoard:
           
           print("Try a different direction: ")
       else:
           if won():
               display()
               print("You Won!")
               gameOver = True
           else:
               
               addNewValue()
               
               display()
               if noMoves():
                   print("Sorry, you run out of moves")
                   gameOver = True
