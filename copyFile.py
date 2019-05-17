#Copy a .txt file

def copyFile(filePathToCopy, fileNameToPaste):
    with open(filePathToCopy, 'r') as rf:
        with open(fileNameToPaste, 'w') as wf:
            for line in rf:
                wf.write(line)