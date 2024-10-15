from Animal import Animal

class AnimalShelter:
    def __init__(self):
        self.animalshelter = {}
    def addAnimal(self,animal):
        species = animal.species
        if self.animalshelter.get(species) == None:
            print("adding ",animal.toString(),"to the dictionary with species", species)
            self.animalshelter[species] = [animal]
        elif not animal in self.animalshelter.get(species):
            print("appending ", animal.toString(), "to the dictionary with species", species) 
            self.animalshelter[species].append(animal)
    def removeAnimal(self,animal):
        species = animal.species
        if self.animalshelter.get(species) != None:
            animallist = self.animalshelter.get(species)
            for i in animallist:
                if i.toString() == animal.toString():
                    animallist.remove(i)
                    break
    def removeSpecies(self,species):
        species = species.upper() if species else None
        if species in self.animalshelter:
            del self.animalshelter[species]
    def getAnimalsBySpecies(self,species):
        species = species.upper() if species else None
        string = []
        if species in self.animalshelter:
            for animal in self.animalshelter[species]:
                string.append(animal.toString())
        return "\n".join(string)
    def doesAnimalExist(self,animal):
        species = animal.species
        if self.animalshelter.get(species) != None:
            animallist = self.animalshelter.get(species)
            for i in animallist:
                if i.toString() == animal.toString():
                    return True
        return False
