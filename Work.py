class WorkMem():
    def __init__(self, sName, sSurname, iID, sOccu):
        self.uName = sName
        self.uSurname = sSurname
        self.uID = iID
        self.uOccu = sOccu
        self.appDict = { 500936: {"Name": "Steve", "Surname": "Biko", "Occupation": "employee"}}

    def addNewMem(self):
        self.appDict[self.uID] = {}

        self.appDict[self.uID]["Name"] = self.uName
        self.appDict[self.uID]["Surname"] = self.uSurname
        self.appDict[self.uID]["Occupation"] = self.uOccu

        return f"Successfully saved member details({self.uID})"

    def displayMem(self, ID):
        self.uID = ID

        if self.uID in self.appDict:
            return self.appDict[self.uID]
        else:
            return "non existent"

    def displayAllMem(self):
        for i in self.appDict:
            return f"{i}: {self.appDict[i]}"