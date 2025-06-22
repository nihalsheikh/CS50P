# Week 1: Problem 4
def main():
    e = input("Enter Expression: ")
    solve(e)

def solve(e):
    a,b,c = e.split(" ")
    a = int(a)
    b = int(b)
    print(a, c, b)

main()
