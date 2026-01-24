import random


class Character :
    """ 
    This class represents a character in the game. 
    
    Attributes:
        name (str): The name of the character.
        description (str): The description of the character.
        current_room (Room): The current room where the character is located.
        msgs (list): A list of messages that the character can say.
        movable (bool): Indicates if the character can move between rooms.
   
    Methods:
        __init__(self, name, description, current_room=None, msgs=None, movable=True): The constructor of the class.
        __str__(self): Returns the string representation of the character.
        get_msg(self): Returns a message from the character.
        move(self): Moves the character to a random adjacent room if movable.
        movable_status(self): Returns the movable status of the character.
    """


    def __init__(self, name, description, current_room=None, msgs=None,movable=True):
        """ Initialize a character with name, description, current room, messages, and movable status. """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs.copy() if msgs else []
        self.msgs_init = self.msgs.copy()  # Store initial messages for reset
        self.movable = movable

        # Register character in the room if provided
        if self.current_room is not None:
            self.current_room.characters[self.name] = self



    def __str__(self) :
        """ Return the string representation of the character. """
        return f"{self.name} : {self.description}"
    


    def get_msg(self):
        """ Return the messages of the character. """
        if not self.msgs:  # if the list is empty
            self.msgs = self.msgs_init.copy()  # Reset to initial messages
        return self.msgs.pop(0)  # Return and remove the first message



    def move(self):
        """ Move the character to a random adjacent room if movable. """
        # No movement possible without a current room or exits
        if not self.current_room or not self.current_room.exits:
            return False

        # 50% chance to move
        if random.choice([0, 1]) == 0 :
            # Select a random exit
            target = random.choice(list(self.current_room.exits.values()))

            # Remove from current room and add to target
            self.current_room.characters.pop(self.name, None)
            target.characters[self.name] = self
            self.current_room = target
            return True
        
        return False
      
        

    def movable_status(self):
        """ Return the movable status of the character. """
        return self.movable