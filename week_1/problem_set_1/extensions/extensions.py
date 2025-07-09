# Week 1: Problem 3
# funcc which tells file's media type

def main():
    name = input("Enter file name: ").strip().lower()
    fileName(name)

def fileName(nameOfFile):
    # splitting filename from right with only one break
    nameOfFile, type = nameOfFile.rsplit(".", 1)
    print(findType(type))

def findType(extType):
    if "." not in extType:
        return "application/octet-stream"

    match type:
        case "gif":
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "file/pdf"
        case "txt":
            return "file/text"
        case "zip":
            return "file/zip"
        case _:
            return "application/octet-stream"


main()
