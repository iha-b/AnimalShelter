from Animal import Animal

class Cow(Animal):
    def __init__(self, species = None, weight = None, age= None, name = None, sound= None):
        super().__init__(species, weight, age, name)
        #Animal.__init__(self,species,weight,age,name) OK
        self.sound = sound
    

    
    def setSound(self,sound):
        self.sound = sound
    def getSound(self):
        s = "Using super class getSound method\n"
        s += Animal.getSound(self) + "\n"
        #s += super().getSound() + "\n" is OK
        s+= "Extending this with our own stuff\n"
        s+= self.sound
        return s
        #return self.sound
        
c = Cow("Cow",None, None, "Betsy","Moo")
print(c.toString())
#c.setSound("Moo!")
print(c.getSound())

print("---")
a = Animal("Animal",None,None, "Whatever")
print(a.toString())
#a.setSound - this won't work because setSound only exists in the Cow class, not
#the animal class

