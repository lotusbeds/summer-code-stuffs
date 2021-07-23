board = [[' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ '], 
        [' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ '], 
        [' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ '], 
        [' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ '], 
        [' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ '], 
        [' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ '], 
        [' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ']]

cols = [6, 6, 6, 6, 6, 6, 6]
won = False 
x = 0
y = 0

def makeBoard():
    for x in range(len(board)):
        for y in range(len(board[0])):
            print(board[x][y], end= "")
        print("")

def chooseLetter():
    while True:
        print("Player 1, do you want to be 'X' or 'O'?")
        letter = input("")
        if letter == "X":
            print("Ok! You're 'X'!")
            return ' X ', ' O '
        elif letter == "O":
            print("Ok! You're 'O'!")
            return ' O ', ' X '
        else:
            print("Please type in 'O' or 'X'! [Case sensitive.]")

def p1move():
    print("Player 1: what column do you want to put your piece?")
    y = int(input(""))
    x = cols[y]
    while True:
        (board[x][y]) = p1Symbol
        cols[y] = cols[y]-1 
        makeBoard()
        break       

def p2move():
    print("Player 2: what column do you want to put your piece?")
    y = int(input(""))
    x = cols[y]
    while True:
        (board[x][y]) = p2Symbol
        cols[y] = cols[y]-1
        makeBoard()
        break

def p1won():
    print("Player 1 won!")
    exit()
    

def p2won():
    print("Player 2 won!")
    exit()

def checkWin(board):
    for x in range(len(board)):
        for y in range(4):
            if (board[x][y]) == p1Symbol and (board[x][y+1]) == p1Symbol and (board[x][y+2]) == p1Symbol and (board[x][y+3]) == p1Symbol:
                p1won()
    for x in range(len(board)):
        for y in range(4):
            if (board[x][y]) == p2Symbol and (board[x][y+1]) == p2Symbol and (board[x][y+2]) == p2Symbol and (board[x][y+3]) == p2Symbol:
                p2won()
    for x in range(4):
        for y in range(len(board)):
            if (board[x][y]) == p2Symbol and (board[x+1][y]) == p2Symbol and (board[x+2][y]) == p2Symbol and (board[x+3][y]) == p2Symbol:
                p2won()
    for x in range(4):
        for y in range(len(board)):
            if (board[x][y]) == p1Symbol and (board[x+1][y]) == p1Symbol and (board[x+2][y]) == p1Symbol and (board[x+3][y]) == p1Symbol:
                p1won()
    for x in range(4):
        for y in range(4):
            if (board[x][y]) == p1Symbol and (board[x+1][y+1]) == p1Symbol and (board[x+2][y+2]) == p1Symbol and (board[x+3][y+3]) == p1Symbol:
                p1won()
    for x in range(4):
        for y in range(4):
            if (board[x][y]) == p2Symbol and (board[x+1][y+1]) == p2Symbol and (board[x+2][y+2]) == p2Symbol and (board[x+3][y+3]) == p2Symbol:
                p2won()
    for x in range(4):
        for y in range(6, 0, -1):
            if (board[x][y]) == p1Symbol and (board[x+1][y-1]) == p1Symbol and (board[x+2][y-2]) == p1Symbol and (board[x+3][y-3]) == p1Symbol:
                p1won()
    for x in range(4):
        for y in range(6, 0, -1):
            if (board[x][y]) == p2Symbol and (board[x+1][y-1]) == p2Symbol and (board[x+2][y-2]) == p2Symbol and (board[x+3][y-3]) == p2Symbol:
                p2won()
    
def play():
    while True:
        p1move()
        checkWin(board)
        p2move()
        checkWin(board)
            
makeBoard()
p1Symbol, p2Symbol = chooseLetter()
play()