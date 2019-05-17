import readFile as rf
import writeFile as wf
import copyFile as cf
import copyImage as ci


filePath = 'the path of your file goes here'
newFileName = 'the name of your new file goes here'
imagePath = 'the path of your image goes here'
newImageName = 'the name of your new image goes here'+'.'+'format of your image'
writeContent = 'content to write to file'


rf.readFile(filePath)
wf.writeFile(filePath, writeContent)
cf.copyFile(filePath, newFileName)
ci.copyImage(imagePath, newImageName)