# Week 6: Shorts - Reading and Writing Files
def main():
    # read the file
    with open("alice.txt", "r") as f:
        contents = f.readlines()

    # print(contents) # print all contents
    chapter1 = contents[52:271] # string slicing method [indx1:indx2]

    # write the contents in a new file
    with open("chapter1.txt", "w") as f:
        chapt1 = f.writelines(chapter1)

main()
