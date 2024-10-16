# AnimalShelter

This project implements an animal shelter management system using Python. The system allows users to create and manage `Animal` and `AnimalShelter` objects, providing functionalities to add, remove, and retrieve animals based on their species. 

## Project Structure

The project consists of two main files:

- `Animal.py`: Defines the `Animal` class, which represents individual animals.
- `AnimalShelter.py`: Defines the `AnimalShelter` class, which manages a collection of `Animal` objects.

## Class Descriptions

### Animal Class

The `Animal` class encapsulates the properties and behaviors of an animal. Each animal has the following attributes:

- **species**: A string representing the species of the animal (stored in uppercase).
- **weight**: A float representing the weight of the animal (in lbs).
- **age**: An integer representing the age of the animal (in years).
- **name**: A string representing the name of the animal (stored in uppercase).

#### Constructor

```python
def __init__(self, species=None, weight=None, age=None, name=None):
```
## Methods

#### Setter Methods:

- `setSpecies(self, species)`: Sets the species of the animal.
- `setWeight(self, weight)`: Sets the weight of the animal.
- `setAge(self, age)`: Sets the age of the animal.
- `setName(self, name)`: Sets the name of the animal.
- `toString()`: Returns a string representation of the animal in the following format:

Species: DOG, Name: RUFFLES, Age: 2, Weight: 12.2

### AnimalShelter Class

The `AnimalShelter` class manages a collection of `Animal` objects. It uses a dictionary where the keys are species (stored in uppercase) and the values are lists of `Animal` objects of that species.

#### Constructor

```python
def __init__(self):
```

I apologize for the confusion earlier! Here’s the entire content formatted in a single code block without any interruptions:

markdown
Copy code
# Animal Shelter Project

## Methods

### Animal Class

#### Setter Methods:

- `setSpecies(self, species)`: Sets the species of the animal.
- `setWeight(self, weight)`: Sets the weight of the animal.
- `setAge(self, age)`: Sets the age of the animal.
- `setName(self, name)`: Sets the name of the animal.
- `toString()`: Returns a string representation of the animal in the following format:
Species: DOG, Name: RUFFLES, Age: 2, Weight: 12.2

### AnimalShelter Class

The `AnimalShelter` class manages a collection of `Animal` objects. It uses a dictionary where the keys are species (stored in uppercase) and the values are lists of `Animal` objects of that species.

#### Constructor

```python
def __init__(self):
```
Initializes an empty dictionary for the animal shelter.

#### Methods
addAnimal(self, animal): Adds an Animal object to the shelter.
removeAnimal(self, animal): Removes an Animal object from the shelter based on matching attributes.
removeSpecies(self, species): Removes all animals of a specified species.
getAnimalsBySpecies(self, species): Returns a string of all animals of a specified species, formatted with each animal on a new line.
doesAnimalExist(self, animal): Checks if an Animal object exists in the shelter based on matching attributes.

#### Usage
To use the classes defined in this project, import them into your Python script:

```python
from Animal import Animal
from AnimalShelter import AnimalShelter
```

You can then create instances of Animal and AnimalShelter, and call the methods to manage animals in the shelter.

#### Example
Here's a brief example demonstrating how to use the classes:

# Create an animal shelter
```python
shelter = AnimalShelter()
```

# Create an animal
```python
dog = Animal("dog", 12.2, 2, "Ruffles")
```

# Add the animal to the shelter
```python
shelter.addAnimal(dog)
```

# Retrieve animals by species
```python
print(shelter.getAnimalsBySpecies("dog"))  # Output: Species: DOG, Name: RUFFLES, Age: 2, Weight: 12.2
```

#### Requirements
Python 3.x

