import json

class Spec:
    def __init__(self, specPath):
        data = self.importJson(specPath)
        self.schema = data["$schema"]
        self.description = data["description"]
        self.fields = data['fields']

    def importJson(self, specPath):
        with open(specPath, newline='') as json_file:
            data = json.load(json_file)
        return data

    def getFieldDescription(self,tagId):
        try:
            description = self.fields[tagId]
        except:
            description = {
                              "label": "Local Data",
                              "repeatable": True
                          }
        return description