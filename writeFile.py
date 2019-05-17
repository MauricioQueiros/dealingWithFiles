#Write a .txt file 

def writeFile(pathToWriteFile, writeContent):
    with open(pathToWriteFile, 'w') as f:
        f.write(writeContent)
