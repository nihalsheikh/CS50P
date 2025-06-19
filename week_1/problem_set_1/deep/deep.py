# Creating a main func
def main():
    # question to be asked to user
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    question.lower().strip()

    # If the user input is a number 42, change input to int()
    if (question == "42"):
        question.strip()
        question = int(question)

    # call the function to check the answer
    ansToQue(question)

# Func to answer the question
def ansToQue(q):
    match q: # using match for more clear code than if, elif and else
        case "forty-two" | "forty two": # condition to match the number if input is a string
            print("Yes")
        case 42: # condition to match if input is a num
            print("Yes")
        case _: # any other input gives this output
            print("No")

main()
