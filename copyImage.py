#Copy a image

def copyImage(imagePathToCopy, imageNameToPaste):
    with open(imagePathToCopy, 'rb') as rf:
        with open(imageNameToPaste, 'wb') as wf:
            for line in rf:
                wf.write(line)