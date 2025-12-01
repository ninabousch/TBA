class Item :

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.weight = 0

    def __str__() :
        return f"{self.name} : {self.description} (poids: {self.weight} kg)"
    