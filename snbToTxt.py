'''Converts SNB files to TXT files'''

import os
import re
import zipfile

def convertToTxt(snbFile, destination = None):
    '''Used to convert a single file'''
    with zipfile.ZipFile(snbFile) as snbArchive:
        snbArchive.extract('snote/snote.xml')
    with open('snote/snote.xml', 'r') as xmlFile:
        xmlText = xmlFile.read()
    txtText = re.sub('<.*?>', '', xmlText)
    txtFileName = snbFile.replace('.snb', '.txt')
    if destination is not None:
        txtFileName = '/'.join((destination, txtFileName))
    with open(txtFileName, 'w') as txtFile:
        txtFile.write(txtText)
    os.remove('snote/snote.xml')
    os.rmdir('snote')

def convertDirectory(directory):
    '''Used to convert a folder of SNB files'''
    os.chdir(directory)
    targetDirectory = '/'.join((directory, 'TXT'))
    os.mkdir(targetDirectory)
    for i in os.listdir(directory):
        if os.path.splitext(i)[1] == '.snb':
            convertToTxt(i, targetDirectory)
