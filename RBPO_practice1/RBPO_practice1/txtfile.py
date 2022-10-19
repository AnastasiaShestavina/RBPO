import os
class TxtFile:
    def createFile(self, fileName, str):
        fileName += '.txt'

        with open(fileName, 'w+', encoding = 'utf-8') as file:
            file.write(str)
            file.close()

    def readFile(self, fileName):
        fileName += '.txt'
        try:
            with open(fileName, 'r', encoding = 'utf-8') as read:
                return read.read()
                read.close()
        except FileNotFoundError:
            return 'Error'
        
    def removeFile(self, fileName):
        fileName += '.txt'
        try:
            os.remove(fileName)
            return True
        except FileNotFoundError:
            return False