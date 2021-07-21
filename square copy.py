def square(size):
    for x in range(size):
        for y in range(size):
            print(' ', end='.')
        print("")


def rightTriangle(size):
    for x in range(size):
        for y in range(0, x+1):
            print(' ', end='.')
        print("")

def triangle(size):
    dots = size

    for y in range(size):
        print(' '*dots, end=' ')
        print(' .'*y)
        dots -=1

def shapes():
    print("Hello! Welcome to the Shape Generator! Please choose a shape to be drawn by our top of the line equipment!")
    while True:
        print("Do you want a square or a triangle?")
        shape = input("")
        if shape == "square":
            size = int(input("What size?"))
            square(size)
        elif shape == "triangle":
            print("What type of triangle? Equilateral or right?")
            triangles = input("")
            if triangles == "equilateral":
                size = int(input("What size?"))
                triangle(size)
            elif triangles == "right":
                size = int(input("What size?"))
                rightTriangle(size)
        elif shape == "stop":
            print("Ok! Let's stop!")
            exit()
        else:
            print("Please choose either a triangle or a square ^_^ Thank you!")

shapes()