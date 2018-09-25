def make_sqaure(size):
    pass

def make_rectangle(length, width):
    x = ""
    for i in range(width):
        x += "*"
    for i in range(length):
        print(x)

def make_triangle(size):
    for i in range(size):
        for j in range(size * 2 - 1):
            if(j >= ((size * 2 - 1) // 2 - i) and j <= ((size * 2 - 1) // 2 + i)):
                print("*", end="")
            else:
                print(".",end="")
        print("")


def main():
    while(True):
        print('Hello, please enter what to print')
        print('1\tsquare')
        print('2\trectangle')
        print('3\ttriangle')
        shape = (int)(input('Input: '))
        if(shape == 1):
            size = (int)(input('Input size:'))
            make_square(size)
        elif(shape == 2):
            length = (int)(input('Input length: '))
            width = (int)(input('Input width: '))
            make_rectangle(length, width)
        elif(shape == 3):
            size = (int)(input('Input size: '))
            make_triangle(size)

main()