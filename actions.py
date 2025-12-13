# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1][0]
        direction = direction.upper()
        # if the direction is unrecognized, print an error message and return false.
        if direction in game.directions :
            player.move(direction)
            return True
        # Move the player in the direction specified by the parameter.
        else:
            print("\nTu ne peux pas aller par ici jeune sorcier.\n")
            return False

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def history(game, list_of_words, number_of_parameters):
        """
        Print the history of rooms visited by the player.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> history(game, ["history"], 0)
        True
        >>> history(game, ["history", "N"], 0)
        False
        >>> history(game, ["history", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the history of rooms visited by the player.
        player = game.player
        print("Historique des pièces visitées :\n")   
        for room in player.get_history():
            print(room.name)
        print("\n")
        return True

        
    def back(game, list_of_words, number_of_parameters):
        """
        Move the player back to the previous room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> back(game, ["back"], 0)
        True
        >>> back(game, ["back", "N"], 0)
        False
        >>> back(game, ["back", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        if not player.history:
            print("\nAucune pièce précédente dans l'historique !\n")
            return False
        
        previous_room = player.history.pop()
        player.current_room = previous_room
        print(player.current_room.get_long_description())
        return True
    
    def inventory(game, list_of_words, number_of_parameters):
        """
        Print the inventory of the player.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> inventory(game, ["inventory"], 0)
        True
        >>> inventory(game, ["inventory", "N"], 0)
        False
        >>> inventory(game, ["inventory", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the inventory of the player.
        player = game.player
        print("Inventaire du joueur :\n")   
        if player.get_inventory():
            for item in player.get_inventory().values():
                print(item)
        else:
            print("L'inventaire est vide.\n")
        print("\n")
    
    
    
    def look(game, list_of_words, number_of_parameters):

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the inventory of the current room.
        player = game.player
        room = player.current_room
        print(room.get_long_description())
        print("La pièce contient :\n")   
        if room.get_inventory():
            for item in room.get_inventory().values():
                print(item)
            for personnage in player.current_room.characters.values():
                print(personnage)
        else:       
            print("Il n'y a rien ici.\n")
        print("\n")
        return True
    

    def take(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        room = player.current_room
        item_name = list_of_words[1]
        if item_name in room.get_inventory():
            if sum(float(item.weight) for item in player.get_inventory().values()) + float(room.get_inventory()[item_name].weight) <= player.max_weight:
                item = room.get_inventory().pop(item_name)
                player.get_inventory()[item_name] = item
                print(f"\nVous avez pris l'objet : {item_name}\n")
                if item_name == "porteloin":
                    print("\nEn prenant le porteloin, une sensation étrange vous envahit...\n"
                          "le bouton en or se met à briller intensément et semble vous appeler.\n")
            else:
                print(f"\nVous ne pouvez pas prendre l'objet '{item_name}', il est trop lourd.\n")  
                return True
        else:
            print(f"\nL'objet '{item_name}' n'est pas dans cette pièce.\n")
            return False    
        

    def drop(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        room = player.current_room
        item_name = list_of_words[1]
        if item_name in player.get_inventory():
            item = player.get_inventory().pop(item_name)
            room.get_inventory()[item_name] = item
            print(f"\nVous avez déposé l'objet : {item_name}\n")
            return True
        else:
            print(f"\nL'objet '{item_name}' n'est pas dans votre inventaire.\n")
            return False
        

    def check(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        print("\nVous disposez des items suivant :\n")
        for _,item in player.get_inventory().items():
            print(item.name)
            return True



    def charger(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        save_room = game.player.current_room
        game.saved_room = save_room
        print("\nLe portoloin enregistre cette pièce. Vous pourrez y revenir directement lorsque vous le souhaitez.\n")
        return True



    def use(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player = game.player
        item_name = list_of_words[1]
        if item_name in player.get_inventory():
            if item_name == "portoloin":
                print("\nSoudain, une lumière éblouissante vous enveloppe et vous sentez\n"
                      "une force mystérieuse vous transporter à un autre endroit...\n")
                # Here you could add logic to transport the player to another room.
                player.current_room = game.saved_room 
                print("\nVous vous retrouvez dans la pièce enregistrée précédemment avec le portoloin.\n")
                print(player.current_room.get_long_description())
                return True
            else:
                print(f"\nL'objet '{item_name}' ne peut pas être utilisé maintenant.\n")
                return False
       