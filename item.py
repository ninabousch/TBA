class Item :
    """
    This class represents an item in the game with a name, description, and weight.

    Attributes:
        name (str): The name of the item.
        description (str): The description of the item.
        weight (float): The weight of the item in kilograms.

    Methods:
        __init__(self, name, description, weight): The constructor of the class.
        __str__(self): Returns the string representation of the item.

    """


    def __init__(self, name, description, weight):
        """ Initialize an item with name, description, and weight. """
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self) :
        """ Return the string representation of the item. """
        return f"{self.name} : {self.description} (poids: {self.weight} kg)"
    