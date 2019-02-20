'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''


class Flower():
    kingdom = "Plantae"
    type = "flower"

    def __init__(self, flower_name = "unknown", petal_colour="unknown", occasion="unknown", mood="unknown"):
        self.petal_colour = petal_colour
        self.occasion = occasion
        self.mood = mood
        self.flower_name = flower_name

    def __str__(self):
        return f"Name: {self.flower_name}\r\nColor: {self.petal_colour} \r\nOccasion: {self.occasion} \r\nVibe: {self.mood}"
    def print(self):
        return print(f"The {self.petal_colour} {self.flower_name} is the {Flower.type} for a {self.mood} {self.occasion}.")


class Fruit():
    category = "fruit"
    edible = "edible"

    def __init__(self, name="unknown", colour="unknown", flavour="unknown", shape="unknown"):
        self.colour = colour
        self.name = name
        self.flavour = flavour
        self.shape = shape

    def __str__(self):
        return f"Colour: {self.colour} \r\nName: {self.name} \r\nFlavour: {self.flavour}\r\nShape: {self.shape}"

    def print(self):
        return print(f"{self.name} is a {self.flavour} {self.shape} {self.colour} {Fruit.category} that is {Fruit.edible}.")


class Dwarf():
    protagonist = "Snow White"
    creature = "dwarf"

    def __init__(self, name="unknown", personality_trait = "unknown", facial_hair="unknown", hospititable=False):
        self.personality_trait = personality_trait
        self.facial_hair = facial_hair
        self.name = name
        self.hospititable = hospititable


    def __str__(self):
        return f"Name: {self.name} \r\nPersonality: {self.personality_trait} \r\nWelcoming: {self.hospititable}"

    def print(self):
        return print(f"{self.name} is the {self.personality_trait} {self.facial_hair} {Dwarf.creature} from {Dwarf.protagonist}. He probably {'likes' if self.hospititable == True else 'doesnt like'} guests.")




red_rose = Flower("rose", "red", "Valentines Day", "romantic")
white_carnation = Flower("carnation", "white", "funeral", "romantic")

grumpy = Dwarf("Grumpy", "curmudgeonly", "bearded", False)
dopey = Dwarf("Dopey", "silent", "beardless", True)

apple = Fruit("Granny Smith Apple", "green", "tart", "round")
banana = Fruit("banana", "yellow", "mild", "bendy")



grumpy.print()
dopey.print()
red_rose.print()
white_carnation.print()
banana.print()
apple.print()



