class Animal:
    def __init__(self,species = None,weight=None, age=None, name=None):
        self.species = species.upper() if species else None
        self.weight = weight
        self.age = age
        self.name = name.upper()if name else None           
    def setSpecies(self, species):
        self.species = species.upper()
    def setWeight(self,weight):
        self.weight = weight
    def setAge(self,age):
        self.age = age
    def setName(self,name):
        self.name = name.upper()
    def toString(self):
       return ("Species: {}, Name: {}, Age: {}, Weight: {}".format(
            self.species, self.name, self.age, self.weight))
    def getSound(self):
        return ("I am an animal!")


a = Animal()
print(a.toString())
