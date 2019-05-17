#Read a .txt file

def readFile(pathOfFile):
    with open(pathOfFile,'r') as f:
        for line in f:
            print(line, end='')
