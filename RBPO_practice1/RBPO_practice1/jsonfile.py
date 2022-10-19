import json
import os

class JsonFile:
    recipes = {}
    recipes['recipe'] = []

    def writeJson(self, fileName, name, category, ingredient):
        fileName += '.json'
        self.recipes['recipe'].append({
                    'name': name,
                    'category': category, 
                    'ingredient' : ingredient
                })
        with open(fileName, 'w') as f:
            json.dump(self.recipes, f)

    def readJson(self, fileName):
        fileName += '.json'
        try:
            with open(fileName) as j:
                data = json.load(j)
                for elem in data['recipe']:
                    self.recipes['recipe'].append({
                        'name': elem['name'],
                        'category': elem['category'], 
                        'ingredient': elem['ingredient']
                    })
                return json.dumps(data, indent=4)
        except FileNotFoundError:
            return 'Error'

    def removeJson(self, fileName):
        fileName += '.json'
        try:
            os.remove(fileName)
            return True
        except FileNotFoundError:
            return False