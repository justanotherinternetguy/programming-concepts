# This is code for implementation of the 4 pillars of OOP in Python


# Abstraction: Only concerning the program w/ relevant data

class Person: # class keyword to create a class
    classAttr = "2 hands" # attribute of the CLASS itself

    def __init__(self, name, age, mood): # __init__ is similar to constructors in c++ and java, it is run when an object is initialized.
        # name, age, mood are attributes we give to each object
        self.name = name
        self.age = age
        self.mood = mood
        # Essentially, attributes describe the object we are working with (think: physical traits, adjectives)

    def introduce(self): # this is a method / operation of the object. Every object created has the ability to carry out the methods
        print("hi! my name is {}".format(self.name)) # the talk() operation allows every Person object to say their name


person1 = Person("Jack", 22, "happy") # Creation of an object
person2 = Person("Joey", 19, "sad") # Creation of an object

# Usage of the method
person1.introduce()
person2.introduce()

"""
OUTPUT should be:

> hi! my name is Jack
> hi! my name is Joey

"""


# Encapsulation: to hide ("encapsulate") some of the complexity behind the classes

# EXAMPLE:

"""
Programmer A writes class Person()

Programmer B wants to use the methods and attributes of Person(), but Programmer A wants to keep his intellectual property.

To avoid Programmer B from actually seeing how Person() was made, all Programmer A has to do is to tell Programmer B the attributes and methods of Programmer A's class.

Programmer B can now import Person() as an obfuscated file, use the class, but not have to look at any of the code.

Encapsulation can also help to keep data and operations within a class secure.
"""

# Inheritance: a class can inherit its methods and attributes from another class (superclass vs. subclass)

# Inheritance is very simple, i'll give you an example

"""
A "superclass" is a class that is GIVING INHERITANCE to a subclass
A "subclass" is a class that INHERITS the attributes from a superclass

E.x:

Superclass Person() can give inheritance to subclasses:
- Doctor(), Athlete(), and Comedian()

Doctors, Athletes, and Comedians are all humans, so they inherit all the qualities of the more general Person() class.

Each subclass can also have its own attributes --> Doctor() can have attribute "field of medicine" while Comedian() cannot (realistically, at least)
"""

# Using superclass Person() from the start:

# subclass Doctor()

class Doctor(Person):
    def __init__(self, name, age, mood, fieldMedicine): # make sure in include parameters from superclass as well
        self.fieldMedicine = fieldMedicine

        Person.__init__(self, name, age, mood) # call upon the attributes of superclass

    def details(self):
        print("hi! my name is {}".format(self.name))
        print("i study {}".format(self.fieldMedicine))

doctor1 = Doctor("Bob", 46, "calm", "dermatology")

"""
OUTPUT:
i! my name is Bob
i study dermatology
"""
# as you can see, we could use all of Person()'s attributes without having to re-declare all of them.
# this makes coding large projects less tedious.

doctor1.details()


# Polymorphism: a subclass can implement an inherited method in its own way

# poly = multiple
# morph = many forms

class WaterAnimals():
    def intro(self):
        print("there are many animals that live in the water.")

    def classify(self):
        print("some water animals can breathe underwater. some cannot")

class salmon(WaterAnimals):
    def classify(self):
        print("salmons can breath underwater with gills")


class whale(WaterAnimals):
    def classify(self):
        print("whales must return to the surface of the water to breath air")


object_WaterAnimal = WaterAnimals()
object_Salmon = salmon()
object_Whale = whale()

object_WaterAnimal.intro()
object_WaterAnimal.classify()

object_Salmon.intro()
object_Salmon.classify()

object_Whale.intro()
object_Whale.classify()

"OUTPUT:
there are many animals that live in the water.
some water animals can breathe underwater. some cannot
there are many animals that live in the water.
salmons can breath underwater with gills
there are many animals that live in the water.
whales must return to the surface of the water to breath air
"

# All subclass can still use method intro() defined ONLY in superclass WaterAnimals(),
# BUT, salmon() and whale() subclasses can modify the classify() method to their own preference.



