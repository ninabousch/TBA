# Define the Player class.
class Player():
    """
    This class represents a player in the game.

    Attributes:
        name (str): The name of the player.
        current_room (Room): The current room where the player is located.
        history (list): A list of rooms the player has visited.
        inventory (dict): The inventory of the player.
        max_weight (float): The maximum weight the player can carry.
        rewards (list): A list of rewards earned by the player.
        move_count (int): A counter for the number of moves made by the player.
        active_quests (list): A list of active quests for the player.
        completed_quests (list): A list of completed quests for the player.
        quest_manager (QuestManager): An instance to manage quests for the player.

    Methods:
        __init__(self, name): The constructor.
        move(self, direction): Move the player in the given direction.
        get_history(self): Return the history of rooms visited by the player.
        get_inventory(self): Return the inventory of the player.
        add_reward(self, reward): Add a reward to the player's rewards list.
        show_rewards(self): Display all rewards earned by the player.
     
    """


    # Define the constructor.
    def __init__(self, name):
        """ Initialize a player with a name, current room, history, inventory, and other attributes. """
        self.name = name
        self.current_room = None
        self.history = []  
        self.inventory = {} 
        self.max_weight = 10
        self.rewards = []  # List to store rewards earned by the player. 
        self.move_count = 0  # Counter for the number of moves made by the player.
        self.active_quests = []  # List to store active quests for the player.
        self.completed_quests = []  # List to store completed quests for the player.
        self.quest_manager = None # QuestManager instance to manage quests for the player.
    

    # Define the move method.
    def move(self, direction):
        """ Move the player in the given direction."""
        # Safely get the next room using Room.get_exit to avoid KeyError.
        next_room = self.current_room.get_exit(direction)
        self.history.append(self.current_room)

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        # Update move counter and notify quest manager (if any)
        try:
            self.move_count += 1
        except Exception:
            self.move_count = 1

        if self.quest_manager:
            # Update any counter-based objectives
            self.quest_manager.check_counter_objectives("Se déplacer", self.move_count)
            # Check room-related objectives for the new room
            self.quest_manager.check_room_objectives(self.current_room.name)

        return True


    def get_history(self):
        """Return the history of rooms visited by the player.

        Fixed signature to accept the instance (self).
        """
        return self.history
    

    def get_inventory(self):
        """Return the inventory of the player."""
        return self.inventory
    

    def add_reward(self, reward):
       """
       Add a reward to the player's rewards list.
      
       Args:
           reward (str): The reward to add.
          
       Examples:
      
       >>> player = Player("Bob")
       >>> player.add_reward("Héros de Poudlard") # doctest: +NORMALIZE_WHITESPACE
       <BLANKLINE>
       🎁 Vous avez obtenu: Héros de Poudlard
       """
       if reward and reward not in self.rewards:
           self.rewards.append(reward)
           print(f"\n🎁 Vous avez obtenu: {reward}\n")


    def show_rewards(self):
       """
       Display all rewards earned by the player.
      
       Examples:
      
       >>> player = Player("Charlie")
       >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
       <BLANKLINE>
       🎁 Aucune récompense obtenue pour le moment.
       <BLANKLINE>
       >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
       <BLANKLINE>
       🎁 Vos récompenses:
       • Héros de Poudlard
       <BLANKLINE>
       """
       if not self.rewards:
           print("\n🎁 Aucune récompense obtenue pour le moment.\n")
       else:
           print("\n🎁 Vos récompenses:")
           for reward in self.rewards:
               print(f"  • {reward}")
           print()
