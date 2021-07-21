import random
board = [[' _ ', ' _ ', ' _ '], [' _ ', ' _ ', ' _ '], [' _ ', ' _ ', ' _ ']]
ifWins = False

def makeBoard():
    for x in range(len(board)):
        for y in range(len(board[0])):
            print(board[x][y], end= "")
        print("")

def chooseLetter():
    while True:
        print("Do you want to be 'X' or 'O'?")
        letter = input("")
        if letter == "X":
            global playerSymbol
            global compSymbol
            playerSymbol = ' X '
            compSymbol = ' O '
            print("Ok! You're 'X'!")
            break
        elif letter == "O":
            playerSymbol = ' O '
            compSymbol = ' X '
            print("Ok! You're 'O'!")
            break
        else:
            print("Please type in 'O' or 'X'! [Case sensitive.]")

def computerPlay():
    while True:
        x = random.randint(0,2)
        y = random.randint(0,2)
        if (board[x][y]) == ' _ ':
            board[x][y] = compSymbol
            print("Computer move:")
            makeBoard()
            break

def playerPlay():
    while True:
        print("Enter the x value of your turn. [0-2]")
        x = int(input(""))
        print("Enter the y value of your turn. [0-2]")
        y = int(input(""))
        if (board[x][y]) != ' _ ':
            print("Please enter a different set of coordinates.")
        else: 
            (board[x][y]) = playerSymbol
            makeBoard()
            break

def computerWins():
    print("The computer won!")
    exit()

def playerWins():
    print("You win!")
    exit()

def checkWin(board):
    #player rows
    if (board[0][0]) == playerSymbol and (board[0][1]) == playerSymbol and (board[0][2]) == playerSymbol:
        global ifWins
        ifWins = True
        playerWins()
    if (board[1][0]) == playerSymbol and (board[1][1]) == playerSymbol and (board[1][2]) == playerSymbol:
        ifWins = True
        playerWins()    
    if (board[2][0]) == playerSymbol and (board[2][1]) == playerSymbol and (board[2][2]) == playerSymbol:
        ifWins = True
        playerWins()
    #computer rows
    elif (board[0][0]) == compSymbol and (board[0][1]) == compSymbol and (board[0][2]) == compSymbol:
        ifWins = True
        computerWins()
    elif (board[1][0]) == compSymbol and (board[1][1]) == compSymbol and (board[1][2]) == compSymbol:
        ifWins = True
        computerWins()
    elif (board[2][0]) == compSymbol and (board[2][1]) == compSymbol and (board[2][2]) == compSymbol:
        ifWins = True
        computerWins()
    #player columns
    if (board[0][0]) == playerSymbol and (board[1][0]) == playerSymbol and (board[2][0]) == playerSymbol:
        ifWins = True
        playerWins()
    if (board[0][1]) == playerSymbol and (board[1][1]) == playerSymbol and (board[2][1]) == playerSymbol:
        ifWins = True
        playerWins()    
    if (board[0][2]) == playerSymbol and (board[1][2]) == playerSymbol and (board[2][2]) == playerSymbol:
        ifWins = True
        playerWins()
    #computer columns
    elif (board[0][0]) == compSymbol and (board[1][0]) == compSymbol and (board[2][0]) == compSymbol:
        ifWins = True
        computerWins()
    elif (board[0][1]) == compSymbol and (board[1][1]) == compSymbol and (board[2][1]) == compSymbol:
        ifWins = True
        computerWins()
    elif (board[0][2]) == compSymbol and (board[1][2]) == compSymbol and (board[2][2]) == compSymbol:
        ifWins = True
        computerWins()
    #player diagonals
    if (board[0][0]) == playerSymbol and (board[1][1]) == playerSymbol and (board[2][2]) == playerSymbol:
        ifWins = True
        playerWins()
    if (board[0][2]) == playerSymbol and (board[1][1]) == playerSymbol and (board[2][0]) == playerSymbol:
        ifWins = True
        playerWins()
    #computer diagonals
    if (board[0][0]) == compSymbol and (board[1][1]) == compSymbol and (board[2][2]) == compSymbol:
        ifWins = True
        computerWins()
    if (board[0][2]) == compSymbol and (board[1][1]) == compSymbol and (board[2][0]) == compSymbol:
        ifWins = True
        computerWins()
    #tie
    if (board[0][0]) != ' _ ' and (board[0][1]) != ' _ ' and (board[0][2]) != ' _ ' and (board[1][0]) != ' _ ' and (board[2][0]) != ' _ ' and (board[1][1]) != ' _ ' and (board[1][2]) != ' _ ' and (board[2][1]) != ' _ ' and (board[2][2]) != ' _ ' and ifWins == False:
        print("Tie!")
        exit()

def play():
    while True:
        computerPlay()
        checkWin(board)
        playerPlay()
        checkWin(board)
        if ifWins:
            break

makeBoard()
chooseLetter()
play()