# TBA

Ce repo contient la dernière version du jeu d'aventure TBA l'ombre de Poudlard.

Les lieux sont au nombre de 16. les objets au


## Structuration

Il y a pour le moment 5 modules contenant chacun une classe.

- `game.py` / `Game` : description de l'environnement, interface avec le joueur ;
- `room.py` / `Room` : propriétés génériques d'un lieu  ;
- `player.py` / `Player` : le joueur ;
- `command.py` / `Command` : les consignes données par le joueur ;
- `actions.py` / `Action` : les interactions entre .

## Diagramme 

```mermaid
---
title: l'ombre de Poudlard
---
classDiagram
    room -- player
    command -- actions
    game -- command
    game -- actions
    game -- item
    game -- character
    game -- quest
    game -- quest_manager
    character -- room
    player -- quest_manager

    class actions{
        +go() 
        +quit()
        +help()
        +history()
        +back()
        +inventory()
        +check()
        +look()
        +take()
        +drop()
        +charger()
        +use()
        +read()
        +talk()
        +quests()
        +quest()
        +activate()
        +activate_all()
        +rewards()
        +give()
        +add()
        +spell()
    }

    class characters{
        -name (str): The name of the character.
        -description (str): The description of the character.
        -current_room (Room): The current room where the character is located.
        -msgs (list): A list of messages that the character can say.
        -movable (bool): Indicates if the character can move between rooms.
        __init__(self, name, description, current_room=None, msgs=None, movable=True): The constructor of the class.
        __str__(self): Returns the string representation of the character.
        +get_msg(self): Returns a message from the character.
        +move(self): Moves the character to a random adjacent room if movable.
        +movable_status(self): Returns the movable status of the character.
    }
    class command{
        -command_word (str): The command word.
        -help_string (str): The help string.
        -action (function): The action to execute when the command is called.
        -number_of_parameters (int): The number of parameters expected by the command.
        __init__(self, command_word, help_string, action, number_of_parameters) : The constructor.
        __str__(self) : The string representation of the command.

    }
    class game{
        -inished (bool): Flag indicating whether the game has ended.
        -rooms (list): List of all Room objects in the game.
        -commands (dict): Dictionary mapping command names to Command objects.
        -player (Player): The player object controlling the game.
        -directions (set): Set of valid direction tokens (N, S, E, O, U, D, etc.).
        __init__(self) : The constructor.
        +setup(self) : Initializes all game elements (rooms, items, characters, +commands, player, quests).
        +play(self) : Main game loop that processes player commands until the game ends.
        +print_welcome(self) : Displays the welcome message and starting room description.
        +process_command(self, command_string) : Parses and executes a player command.   
        +_setup_quests(self) : Initializes all quests available in the game.
    }
    class item{
        -name (str): The name of the item.
        -description (str): The description of the item.
        -weight (float): The weight of the item in kilograms.
        __init__(self, name, description, weight): The constructor of the class.
        __str__(self): Returns the string representation of the item.
    }
    class player{
        -name (str): The name of the player.
        -current_room (Room): The current room where the player is located.
        -history (list): A list of rooms the player has visited.
        -inventory (dict): The inventory of the player.
        -max_weight (float): The maximum weight the player can carry.
        -rewards (list): A list of rewards earned by the player.
        -move_count (int): A counter for the number of moves made by the player.
        -active_quests (list): A list of active quests for the player.
        -completed_quests (list): A list of completed quests for the player.
        -quest_manager (QuestManager): An instance to manage quests for the player.
        __init__(self, name): The constructor.
        +move(self, direction): Move the player in the given direction.
        +get_history(self): Return the history of rooms visited by the player.
        +get_inventory(self): Return the inventory of the player.
        +add_reward(self, reward): Add a reward to the player's rewards list.
        +show_rewards(self): Display all rewards earned by the player.
    }
    class quest{
        -title (str): The title of the quest.
        -description (str): The description of the quest.
        -objectives (list): List of objectives to complete.
        -is_completed (bool): Whether the quest is completed.
        -is_active (bool): Whether the quest is currently active.
        -reward (str): Optional reward for completing the quest.
        __init__(self, title, description, objectives=None, reward=None): The constructor.
        +activate(self): Activate the quest.
        +complete_objective(self, objective, player=None): Mark an objective as completed.
        +complete_quest(self, player=None): Complete the quest.
        +get_status(self): Get the current status of the quest.
        +get_details(self, current_counts=None): Get detailed information about the quest.
        +_format_objective_with_progress(self, objective, current_counts): Format an objective with progress info.
        +_extract_number_from_text(self, text): Extract the first number from a text string.
        +check_room_objective(self, room_name, player=None): Check if visiting a room completes an objective.
        +check_action_objective(self, action, target=None, player=None): Check if performing an action completes an objective.
        +check_counter_objective(self, counter_name, current_count, player=None): Check counting objectives.
        __str__(self): Return a string representation of the quest.
    }

    class quest_manager{
         __init__(self, player=None): The constructor.
        -add_quest(self, quest): Add a quest to the game.    
        -activate_quest(self, quest_title): Activate a quest by its title.
        -complete_objective(self, objective_text): Complete an objective in any active quest.
        -check_room_objectives(self, room_name): Check all active quests for room-related objectives.
        -check_action_objectives(self, action, target=None): Check all active quests for action-related objectives.
        -check_counter_objectives(self, counter_name, current_count): Check all active -quests for counter-related objectives.
        -get_active_quests(self): Get all active quests.
        -get_all_quests(self): Get all quests.
        -get_quest_by_title(self, title): Get a quest by its title.
        -show_quests(self): Display all quests and their status.
        -show_quest_details(self, quest_title, current_counts=None): Show detailed information about a specific quest
    
    }
    class room{
        -name (str): The name of the room.
        -description (str): A text description of what the room looks like.
        -exits (dict): Dictionary mapping directions to adjacent Room objects.
        -inventory (dict): Dictionary mapping item names to Item objects in this room.
        -characters (dict): Dictionary mapping character names to Character objects in this room.
        __init__(self, name, description): the constructor
        +get_exit(self, direction): get the room in the given direction
        +get_exit_string(self): Generate a formatted string listing all available exits from this room.
        +get_long_description(self): Get a complete description of the room including location and available exits.
        +get_inventory(self): Get the inventory of items available in this room.
    
    }
```
