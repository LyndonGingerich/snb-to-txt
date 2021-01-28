from os import path
import re
import zipfile

def convertToTxt(snbFile):
    zipfileObject = zipfile.ZipFile(snbFile)
    zipfileObject.extract('snote/snote.xml')
    zipfileObject.close()
    with open('snote.xml', 'r') as xmlFile:
        xmlText = xmlFile.read()
    txtText = re.sub('<.*?>', '', xmlText)
    txtFileName = snbFile.replace('.snb', '.txt')
    with open(txtFileName, 'w') as txtFile:
        txtFile.write(txtText)

convertToTxt('Memo_20160202_122147724.snb') # for testing