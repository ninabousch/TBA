# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
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
        """Return the inventory of the player.
        """
        return self.inventory
    

    def add_reward(self, reward):
       """
       Add a reward to the player's rewards list.
      
       Args:
           reward (str): The reward to add.
          
       Examples:
      
       >>> player = Player("Bob")
       >>> player.add_reward("Épée magique") # doctest: +NORMALIZE_WHITESPACE
       <BLANKLINE>
       🎁 Vous avez obtenu: Épée magique
       <BLANKLINE>
       >>> "Épée magique" in player.rewards
       True
       >>> player.add_reward("Épée magique") # Adding same reward again
       >>> len(player.rewards)
       1
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
       >>> player.add_reward("Bouclier d'or") # doctest: +NORMALIZE_WHITESPACE
       <BLANKLINE>
       🎁 Vous avez obtenu: Bouclier d'or
       <BLANKLINE>
       >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
       <BLANKLINE>
       🎁 Vos récompenses:
       • Bouclier d'or
       <BLANKLINE>
       """
       if not self.rewards:
           print("\n🎁 Aucune récompense obtenue pour le moment.\n")
       else:
           print("\n🎁 Vos récompenses:")
           for reward in self.rewards:
               print(f"  • {reward}")
           print()
