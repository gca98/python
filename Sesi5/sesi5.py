class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    def __repr__(self):
        return f"to create instance :: Dog( name={self.name}, age={self.age}, breed={self.breed} ) #REPR"
    def __str__(self):
        return f"clean info :: {self.name} is {self.age} years old {self.breed}  #STR"

# dog = Dog('Miley',4)
# print(dog.name)
# print(dog.species)
# print(dog.age)

# Inherit

class Bulldog(Dog):
    def __init__(self, name, age, breed, weight_in_lbs):
        # super().__init__(self, name, age, breed)
        self.weight_in_lbs = weight_in_lbs
    def speak(self, sound):
        return f"{self.name} says woof woof"
class Dachshunds(Dog):
    species = "Canis familiaris"
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def speak(self, sound):
        return f"{self.name} says {sound}"
    def __add__(self, other):
        return self.weight_in_lbs +other.weight_in_lbs



miles = Bulldog("Miles", 4, "Jack Russell Terrier", 12)
# buddy = Bulldog("Buddy", 9, "Dachshund",12)
# jack = Bulldog("Jack", 3, "Bulldog",12)
jim = Dog("Jim", 5, "Bulldog")

# buddy.speak("Yap")

print(jim.speak("Woof"))
print(jim.__repr__())