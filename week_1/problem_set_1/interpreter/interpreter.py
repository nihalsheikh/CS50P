# Week 1: Problem 4
# Solve arithmetic expressions provided by user
def main():
    e = input("Enter an expression: ").strip()
    print(perform(e))

def perform(exp):
    a,b,c = exp.split(" ")
    a = float(a)
    c = float(c)

    match b:
        case "+":
            return float(a + c)
        case "-":
            return float(a - c)
        case "*":
            return float(a * c)
        case "/":
            return float(a / c)
        case "%":
            return float(a % c)
        case _:
            return "In"
        
main()