def square():
    for x in range(4):
        for x in range(4):
            print(' ', end='.')
        print("")

def bigSquare():
    for x in range(7):
        for x in range(7):
            print(' ', end='.')
        print("")

def smallSquare():
    for x in range(2):
        for x in range(2):
            print(' ', end='.')
        print("")


def rightTriangle():
    for x in range(4):
        for y in range(0, x+1):
            print(' ', end='.')
        print("")

def bigRTriangle():
    for x in range(7):
        for y in range(0, x+1):
            print(' ', end='.')
        print("")

def smallRTriangle():
    for x in range(2):
        for y in range(0, x+1):
            print(' ', end='.')
        print("")


def triangle():
    dots = 5

    for y in range(1, 4):
        print(' '*dots, end=' ')
        print(' .'*y)
        dots -=1

def smallTriangle():
    dots = 3

    for y in range(1, 2):
        print(' '*dots, end=' ')
        print(' .'*y)
        dots -=1

def bigTriangle():
    dots = 8

    for y in range(1, 7):
        print(' '*dots, end=' ')
        print(' .'*y)
        dots -=1


def shapes():
    print("Hello! Welcome to the Shape Generator! Please choose a shape to be drawn by our top of the line equipment!")
    while True:
        print("Do you want a square or a triangle?")
        shape = input("")
        if shape == "square":
            print("Do you want small, normal, or big?")
            squareSize = input("")
            if squareSize == "small":
                smallSquare()
            elif squareSize == "normal":
                square()
            elif squareSize == "big":
                bigSquare()
        elif shape == "triangle":
            print("What type of triangle? Equilateral or right?")
            triangles = input("")
            if triangles == "equilateral":
                print("Do you want small, normal, or big?")
                eSize = input("")
                if eSize == "small":
                    smallTriangle()
                elif eSize == "normal":
                    triangle()
                elif eSize == "big":
                    bigTriangle()
            elif triangles == "right":
                print("Do you want small, normal, or big?")
                rSize = input("")
                if rSize == "small":
                    smallRTriangle()
                elif rSize == "normal":
                    rightTriangle()
                elif rSize == "big":
                    bigRTriangle()
        elif shape == "stop":
            print("Ok! Let's stop!")
            exit()
        else:
            print("Please choose either a triangle or a square ^_^ Thank you!")

shapes()








