#define the Room class

"""Room module.

This module defines the Room class which represents a location in the game world.
Rooms can contain items, characters, and connections to other rooms via exits.
"""

class Room:
    """
    Represents a room/location in the game world.
    
    A room is a physical space where the player can be. Each room has:
    - A name identifying it
    - A description of the location
    - Exits connecting it to other rooms
    - An inventory of items that can be picked up
    - Characters that inhabit the room
    
    Attributes:
        name (str): The name of the room.
        description (str): A text description of what the room looks like.
        exits (dict): Dictionary mapping directions to adjacent Room objects.
        inventory (dict): Dictionary mapping item names to Item objects in this room.
        characters (dict): Dictionary mapping character names to Character objects in this room.
    """



    # Define the constructor.
    def __init__(self, name, description):
        """
        Initialize a new Room.
        
        Args:
            name (str): The name of the room (e.g., "Foret", "Bibliotheque").
            description (str): A detailed description of the room's appearance and atmosphere.
        
        The exits, inventory, and characters are initialized as empty collections
        and can be populated after the room is created.
        """
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.characters = {}
    


    # Define the get_exit method.
    def get_exit(self, direction):
        """
        Get the room connected in the given direction.
        
        Args:
            direction (str): A direction code (e.g., 'N', 'S', 'E', 'O', 'U', 'D').
        
        Returns:
            Room or None: The connected room if an exit exists in that direction,
                         None otherwise.
        """

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    


    # Return a string describing the room's exits.
    def get_exit_string(self):
        """
        Generate a formatted string listing all available exits from this room.
        
        Returns:
            str: A string in the format "Sorties: N, E, S, O" showing all directions
                 with available exits, comma-separated.
        """
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string



    # Return a long description of this room including exits.
    def get_long_description(self):
        """
        Get a complete description of the room including location and available exits.
        
        Returns:
            str: A formatted string containing:
                 - A newline
                 - The room description with "Vous êtes" prefix
                 - The list of available exits
                 - Additional newlines for formatting
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
    

    
    def get_inventory(self):
        """
        Get the inventory of items available in this room.
        
        Returns:
            dict: Dictionary mapping item names (str) to Item objects.
                 This includes items that players can pick up.
        """
        return self.inventory
