# Week 1: Problem 4
def main():
    e = input("Enter Expression: ")
    solve(e)

def solve(e):
    a,b,c = e.split(" ")
    print(a, c, b)

main()
