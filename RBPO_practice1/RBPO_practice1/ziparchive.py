import zipfile
import os
import time

class ZipArchive:
    def createFile(self, archiveName):
        archiveName += '.zip'
        zip = zipfile.ZipFile(archiveName, 'w')
        return zip

    def writeFile(self, fileName, zip):
        try:
            zip.write(fileName, os.path.basename(fileName))
            zip.close()
            return zip.infolist()
        except FileNotFoundError:
            return 'Error'

    def readFile(self, archiveName, fileName):
        archiveName += '.zip'
        try:
            with zipfile.ZipFile(archiveName, 'r') as zip:
                zip.extract(os.path.basename(fileName))
                zip.close()
                return os.stat(os.path.basename(fileName))
        except FileNotFoundError:
            return 'Error'

    def removeFiles(self, archiveName, fileName):
        archiveName += '.zip'
        try:
            os.remove(os.path.basename(fileName))
            os.remove(archiveName)
            return 'Ok'
        except FileNotFoundError:
            return 'Error'