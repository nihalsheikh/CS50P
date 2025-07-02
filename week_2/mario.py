# Create mario brick wall
def main():
    bricks = brickSize()
    wall(bricks)

def brickSize():
    height = int(input("enter wall height: "))
    while True:
        if height > 0:
            return height

def wall(b):
    for _ in range(b):
        print("#")

main()
