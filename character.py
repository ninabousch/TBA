import random


class Character :

    def __init__(self, name, description, current_room=None, msgs=None,movable=True):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs.copy() if msgs else []
        self.msgs_init = self.msgs.copy()  # Copie pour réinitialiser plus tard
        self.movable = movable

        # Register character in the room if provided
        if self.current_room is not None:
            self.current_room.characters[self.name] = self

    def __str__(self) :
        """ Return the string representation of the character. """
        return f"{self.name} : {self.description}"
    
    def get_msg(self):
        """ Return the messages of the character. """
        if not self.msgs:  # Si la liste est vide
            self.msgs = self.msgs_init.copy()  # On réinitialise la liste
        return self.msgs.pop(0)  # On retourne et supprime le premier message
    
    def move(self):
        """ Move the character to a random adjacent room if movable. """
        # No movement possible without a current room or exits
        if not self.current_room or not self.current_room.exits:
            return False

        # 50% chance de bouger
        if random.choice([0, 1]) == 0 :
            # Choisir une pièce voisine au hasard
            target = random.choice(list(self.current_room.exits.values()))

            # Retirer de la pièce actuelle et ajouter à la cible
            self.current_room.characters.pop(self.name, None)
            target.characters[self.name] = self
            self.current_room = target
            return True
        
        return False
        
    def movable_status(self):
        """ Return the movable status of the character. """
        return self.movable