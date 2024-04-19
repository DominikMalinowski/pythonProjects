import os

try:
    # Create a new file and check if the file exists
    file = open("data.txt", "x")

    # Open it in write mode
    file = open("data.txt", "a")
    file.write("One\nTwo\nThree")

    #Open it in read mode
    file = open('data.txt', "+r")

    #Create list of all lines
    fileList = []
    for line in file:
        fileList += line.splitlines()
    print(fileList)
    file.close()
    # remoce file
    os.remove('data.txt')
    print("data.txt has been removed.")

except FileExistsError:
    print("File already exists.")