# Launch a '.x' file type
import mimetypes # to know what the file extension

# user inputs file name:
def main():
    fileName = input("Enter file name: ")
    fileExt(fileName)

def fileExt(f):
    ext, encoding = mimetypes.guess_type(f)
    if encoding == "None":
        print("application/octet-stream")
    print(ext)

main()
