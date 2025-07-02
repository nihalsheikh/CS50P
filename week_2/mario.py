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
    printWall(3)

def printWall(size):
    # this outer is loop for wall height
    for i in range(size):

        # this inner loop is for wall width
        for j in range(size):

            # this print func is for no. bricks in a row: ---->
            print("#", end="")

        # this print func is for printing new line after coming out of inner loop
        print()

main()
