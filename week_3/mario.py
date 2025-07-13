# Mario wall
def main():
    wall_height = get_height("Set Pyramid height to: ")
    pyramid(wall_height)

def get_height(h):
    try:
        return int(input(h))
    except ValueError:
        pass

def pyramid(height):
    for i in range(height):
        print(i, end=" ")
        print("#" * (i + 1))

main()
