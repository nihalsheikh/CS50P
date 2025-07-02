# Create mario brick wall
# def main():
#     bricks = brickSize()
#     wall(bricks)

# def brickSize():
#     height = int(input("enter wall height: "))
#     while True:
#         if height > 0:
#             return height

# def wall(b):
#     for _ in range(b):
#         print("#")

# main()

# Nested Loops
# print a square wall, as we see in the mario underground level
def main():
    ofSize = size()
    printWall(ofSize)

def size():
    s = int(input("Enter wall size: "))
    while True: 
        if s > 0:
            return s

def printWall(size):
    for i in range(size):
        print("#" * size)

main()
