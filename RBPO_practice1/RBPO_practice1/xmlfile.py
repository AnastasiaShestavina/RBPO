import xml.etree.ElementTree as ET
import xml.dom.minidom
import os

class XMLFile:
    def writeXml(self, fileName, _name, _category, _mainIngredient):
        fileName += '.xml'
        recipeBook = ET.Element('recipeBook')
        recipeName = ET.Element('recipeName', name = _name, category = _category)
        recipeMainIngr = ET.Element('mainIngredient')
        recipeMainIngr.text = _mainIngredient
        recipeName.append(recipeMainIngr)
        recipeBook.append(recipeName)

        tree = ET.ElementTree(recipeBook)
        tree.write(fileName)

    def readXml(self, fileName):
        fileName += '.xml'
        try:
            dom = xml.dom.minidom.parse(fileName)
            prettyXml = dom.toprettyxml()
            return prettyXml
        except FileNotFoundError:
            return 'Error'

    def removeXml(self, fileName):
        fileName += '.xml'
        try:
            os.remove(fileName)
            return True
        except FileNotFoundError:
            return False