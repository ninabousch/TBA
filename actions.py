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
# The MSG3 variable is used when the command takes 3 parameters.
MSG3 = "\nLa commande '{command_word}' prend 3 paramètres.\n"

class Actions:
    """ This class contains the methods that implement the actions of the game."""


    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O) or up/down(U, D).

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
            game.check_lose_conditions()
            game.player.show_history()
            player.move(direction)
            
            return True
        # Move the player in the direction specified by the parameter.
        else:
            print("\nTu ne peux pas aller par ici jeune sorcier...\n")
            return False


    @staticmethod
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
        msg = f"\nMerci {player.name} d'avoir joué à L'Ombre de Poudlard ! Au revoir et à bientôt pour de nouvelles aventures !\n"
        print(msg)
        game.finished = True
        return True


    @staticmethod
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
        
        # Move the player back to the previous room.
        player = game.player                                                            # Get the player object
        if len(player.history) <= 1:                                                    # Check if there's a previous room (need at least 2 rooms in history)
            print("\nIl n'y a aucune pièce précédente dans l'historique !\n")           # Print error message
            return False                                                                # Return False to indicate failure
        
        player.history.pop()                                                            # Remove the current room from history
        previous_room = player.history[-1]                                              # Get the room before current
        player.current_room = previous_room                                             # Set current room to previous room
        print(player.current_room.get_long_description())                               # Print the description of the current room
        return True                                                                     # Return True to indicate success
    

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
        print("\nVoici ce qu'il y a dans ton inventaire :\n")
        if player.get_inventory():
            for item in player.get_inventory().values():
                print(item)
        else:
            print("Oh ! On dirait bien que ton inventaire est vide.\n")
        print("\n")
        return True
    
    
    def look(game, list_of_words, number_of_parameters):
        """
        Print the description of the current room, including items and characters present.
        
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
        >>> look(game, ["look"], 0)
        True
        >>> look(game, ["look", "N"], 0)    
        False
        >>> look(game, ["look", "N", "E"], 0)
        False
        """

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

        # Print items present in the room (if any)
        if room.get_inventory():
            print("Objets présents dans la pièce :\n")
            for item in room.get_inventory().values():
                print(item)
            print("\n")
        else:
            print("Il n'y a pas d'objet ici.\n")

        # Print characters present in the room (if any)
        if player.current_room.characters:
            print("Personnages présents dans la pièce :\n")
            for personnage in player.current_room.characters.values():
                print(personnage)
            print("\n")
        else:
            print("Il n'y a personne ici.\n")
        return True
    

    def take(game, list_of_words, number_of_parameters):
        """
        Take an item from the current room and add it to the player's inventory.
        
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
        >>> take(game, ["take", "portoloin"], 1) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        Vous avez pris l'objet : portoloin
        <BLANKLINE>
        True
        >>> take(game, ["take"], 1)
        <BLANKLINE>
        La commande 'take' prend 1 seul paramètre.
        <BLANKLINE>
        False
        """
        
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        # Take the item from the current room and add it to the player's inventory.
        player = game.player
        room = player.current_room
        item_name = list_of_words[1]
        
        # Check if the item is in the room's inventory
        if item_name in room.get_inventory():
            
            # Check if adding the item would exceed the player's max weight
            if sum(float(item.weight) for item in player.get_inventory().values()) + float(room.get_inventory()[item_name].weight) <= player.max_weight:
                item = room.get_inventory().pop(item_name)
                player.get_inventory()[item_name] = item
                print(f"\nVous avez pris l'objet : {item_name}\n")
                
                # Notify quest manager about taking items
                if player.quest_manager:
                    player.quest_manager.complete_objective(f"take {item_name}")
                
                if item_name == "portoloin":
                    print("\nEn prenant le portoloin, une sensation étrange vous envahit...\n"
                          "le bouton en or se met à briller intensément et semble vous appeler.\n")
            
            else:
                print(f"\nVous ne pouvez pas prendre l'objet '{item_name}', il est trop lourd.\n")  
                return False
            return True
        else:
            print(f"\nL'objet '{item_name}' n'est pas dans cette pièce.\n")
            return False    
        

    def drop(game, list_of_words, number_of_parameters):
        """
        Drop an item from the player's inventory and place it in the current room.

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
        >>> drop(game, ["drop", "portoloin"], 1) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        Vous avez déposé l'objet : portoloin
        <BLANKLINE>
        True
        >>> drop(game, ["drop"], 1)
        <BLANKLINE>
        La commande 'drop' prend 1 seul paramètre.
        <BLANKLINE>
        False
        """
        
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        # Drop the item from the player's inventory and place it in the current room.
        player = game.player
        room = player.current_room
        item_name = list_of_words[1]
        # Check if the item is in the player's inventory
        if item_name in player.get_inventory():
            item = player.get_inventory().pop(item_name)
            room.get_inventory()[item_name] = item
            print(f"\nVous avez déposé l'objet : {item_name}\n")
            
            # Notify quest manager about dropping items
            if player.quest_manager:
                player.quest_manager.complete_objective(f"drop {item_name}")
            
            return True
        else:
            print(f"\nL'objet '{item_name}' n'est pas dans votre inventaire.\n")
            return False
        

    def check(game, list_of_words, number_of_parameters):
        """
        Check the player's inventory.

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
        >>> check(game, ["check"], 0)
        <BLANKLINE>
        Vous disposez des items suivant :
        <BLANKLINE>
        True
        >>> check(game, ["check", "N"], 0)
        <BLANKLINE>
        La commande 'check' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the name of items in the inventory of the player.
        player = game.player
        # Check if the inventory is empty
        if not player.get_inventory():
            print("\n Il n'y a aucun objet dans l'inventaire.\n")
        else:
            print("\nVous disposez des items suivant :\n")
            for _,item in player.get_inventory().items():
                print(item.name)
            print("\n")
        return True


    def charger(game, list_of_words, number_of_parameters):
        """
        Load the saved room using the portoloin.
        
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
        >>> charger(game, ["charger"], 0)
        True
        >>> charger(game, ["charger", "N"], 0)
        False
        """

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Save the current room in the portoloin.
        save_room = game.player.current_room
        game.saved_room = save_room
        print("\nLe portoloin enregistre cette pièce. Vous pourrez y revenir directement lorsque vous le souhaitez en utilisant la commande 'use'.\n")
        return True


    def use(game, list_of_words, number_of_parameters):
        """
        Use an item from the player's inventory.

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
        >>> use(game, ["use", "portoloin"], 1) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        Soudain, une lumière éblouissante vous enveloppe et vous sentez une force mystérieuse vous transporter à un autre endroit...
        <BLANKLINE>
        Vous vous retrouvez dans la pièce enregistrée précédemment avec le portoloin.
        <BLANKLINE>
        True
        >>> use(game, ["use"], 1)
        <BLANKLINE>
        La commande 'use' prend 1 seul paramètre.
        <BLANKLINE>
        False
        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        # Use the item from the player's inventory.
        player = game.player
        item_name = list_of_words[1]
        
        # Check if the item is in the player's inventory
        if item_name in player.get_inventory():
            if item_name == "portoloin":
                print("\nSoudain, une lumière éblouissante vous enveloppe et vous sentez une force mystérieuse vous transporter à un autre endroit...\n")
                
                # Ensure a room was saved with the portoloin before transporting
                if getattr(game, 'saved_room', None) is None:
                    print("\nLe portoloin n'a pas de destination enregistrée. Utilisez la commande 'charger' d'abord.\n")
                    return False

                player.current_room = game.saved_room
                print("\nVous vous retrouvez dans la pièce enregistrée précédemment avec le portoloin.\n")
                print(player.current_room.get_long_description())
                
                # Notify quest manager about using the portoloin
                if player.quest_manager:
                    player.quest_manager.complete_objective("use portoloin")
                return True
            
            # Notify quest manager about using the item 
            if player.quest_manager:
                player.quest_manager.complete_objective(f"use {item_name}")
                return True
            else:
                print(f"\nL'objet '{item_name}' ne peut pas être utilisé maintenant.\n")
                return False


    def read(game, list_of_words, number_of_parameters):
        """
        Read a book from the player's inventory.

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
        >>> read(game, ["read", "sortileges"], 1) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        En lisant le livre, vous découvrez un sortilège de protection contre les Détraqueurs : 'Expecto Patronum'.
        Vous sentez que vous avez appris quelque chose d'important.
        <BLANKLINE>
        True
        >>> read(game, ["read"], 1)
        <BLANKLINE>
        La commande 'read' prend 1 seul paramètre.
        <BLANKLINE>
        False
        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        # Read the book from the player's inventory.
        player = game.player
        item_name = list_of_words[1]
        # Check if the item is in the player's inventory
        if item_name in player.get_inventory():
            if item_name == "detraqueurs":
                print("\nLes Détraqueurs sont des créatures sombres et effrayantes qui se nourrissent du bonheur des êtres vivants.\n"
                      "Ils sont souvent utilisés par les forces du mal pour semer la terreur.\n"
                      "Ils sont attirés par les émotions négatives et peuvent provoquer un sentiment de désespoir chez ceux qui les approchent.\n"
                      "Il est important de savoir comment les reconnaître et les éviter.\n"
                      "Heureusement, il existe des moyens de se protéger contre eux, notamment en utilisant le sortilège 'Expecto Patronum'.\n"
                      "Restez vigilant et méfiez-vous des Détraqueurs !\n")
            if item_name == "sortileges":  
                print("En lisant le livre, vous découvrez un sortilège de protection contre les Détraqueurs : 'Expecto Patronum'.\n"
                      "Pour utiliser ce sortilège, vous devez concentrer vos pensées sur un souvenir heureux et prononcer les mots magiques.\n"
                          "Vous sentez que vous avez appris quelque chose d'important.\n")
            if item_name == "loups":
                print("Le livre raconte l'histoire des loups-garous, des êtres maudits qui se transforment lors des nuits de pleine lune.\n"
                      "Il explique également comment les reconnaître et les éviter.\n")
            if item_name == "acromentules":
                print("Le livre raconte l'histoire des Acromentules, des arachnides gigantesques et dangereux.\n"
                      "Il explique également comment les reconnaître et les éviter.\n")
            if item_name == "trolls ":
                print("Le livre raconte l'histoire des Trolls, des créatures massives et brutales.\n"
                      "Il explique également comment les reconnaître et les éviter.\n")
            if item_name == "fantomes":
                print("Le livre raconte l'histoire des Fantômes, des esprits errants des anciens habitants de Poudlard.\n"
                      "Il explique également comment les reconnaître et les éviter.\n")
            if item_name == "papier":
                print("En lisant le papier, vous découvrez un message mystérieux :\n"
                      "'Le chemin vers la vérité est caché dans l'ombre.\n")   

            # Notify quest manager about reading the book   
            if player.quest_manager:
                player.quest_manager.complete_objective(f"read {item_name}")
                return True
            else:
                print(f"\nL'objet '{item_name}' ne peut pas être lu.\n")
                return False
        else:
            print(f"\nL'objet '{item_name}' n'est pas dans votre inventaire.\n")
            return False


  
    def talk(game, list_of_words, number_of_parameters):
        """
        Talk to a character in the current room.

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
        >>> talk(game, ["talk", "Hagrid"], 1) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        Hagrid dit : 'Bonjour jeune sorcier ! Comment puis-je t'aider aujourd'hui ?'
        <BLANKLINE>
        True
        >>> talk(game, ["talk"], 1)
        <BLANKLINE>
        La commande 'talk' prend 1 seul paramètre.
        <BLANKLINE>
        False
        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        # Talk to a character in the current room.
        player = game.player
        room = player.current_room
        character_name = list_of_words[1]
        # Check if the character is in the room
        if character_name in room.characters:
            character = room.characters[character_name]
            messages = character.get_msg()
            print(f"\n{character.name} dit : '{messages}'\n")
            
            # Notify quest manager about talk-related objectives
            if player.quest_manager:
                # Use the verb 'talk' which matches quest phrasing
                player.quest_manager.check_action_objectives("talk", character_name)
            return True
        else:
            print(f"\nLe personnage '{character_name}' n'est pas dans cette pièce.\n")
            return False



    @staticmethod
    def quests(game, list_of_words, number_of_parameters):
       """
       Show all quests and their status.
      
       Args:
           game (Game): The game object.
           list_of_words (list): The list of words in the command.
           number_of_parameters (int): The number of parameters expected by the command.


       Returns:
           bool: True if the command was executed successfully, False otherwise.


       Examples:


       >>> from game import Game
       >>> game = Game()
       >>> game.setup("TestPlayer")
       >>> Actions.quests(game, ["quests"], 0) # doctest: +NORMALIZE_WHITESPACE
       <BLANKLINE>
        Quêtes disponibles :
        📋 Quête: 
            ❓Grand Explorateur (Statut: Non activée)
            ❓Installation (Statut: Non activée)
            ❓Petit Voyageur (Statut: Non activée)
       True
        >>> Actions.quests(game, ["quests", "param"], 0)
        <BLANKLINE>
        La commande 'quests' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """

       # If the number of parameters is incorrect, print an error message and return False.
       n = len(list_of_words)
       if n != number_of_parameters + 1:
           command_word = list_of_words[0]
           print(MSG0.format(command_word=command_word))
           return False


       # Show all quests
       game.player.quest_manager.show_quests()
       return True



    @staticmethod
    def quest(game, list_of_words, number_of_parameters):
       """
       Show details about a specific quest.
      
       Args:
           game (Game): The game object.
           list_of_words (list): The list of words in the command.
           number_of_parameters (int): The number of parameters expected by the command.


       Returns:
           bool: True if the command was executed successfully, False otherwise.


       Examples:


       >>> from game import Game
       >>> game = Game()
       >>> game.setup("TestPlayer")
       >>> Actions.quest(game, ["quest", "Petit", "Voyageur"], 1)
       <BLANKLINE>
       📋 Quête: Petit Voyageur
       📖 Prenez le bon train pour aller à Poudlard.
       <BLANKLINE>
       Objectifs:
         ⬜ Aller dans le bon train
       <BLANKLINE>
       🎁 Récompense: Ticket de train
       <BLANKLINE>
       True
       >>> Actions.quest(game, ["quest"], 1)
       <BLANKLINE>
       La commande 'quest' prend 1 seul paramètre.
       <BLANKLINE>
       False
       """

       # If the number of parameters is incorrect, print an error message and return False.
       n = len(list_of_words)
       if n < number_of_parameters + 1:
           command_word = list_of_words[0]
           print(MSG1.format(command_word=command_word))
           return False


       # Get the quest title from the list of words (join all words after command)
       quest_title = " ".join(list_of_words[1:])


       # Prepare current counter values to show progress
       current_counts = {
           "Se déplacer": game.player.move_count
       }


       # Show quest details
       game.player.quest_manager.show_quest_details(quest_title, current_counts)
       return True




    @staticmethod
    def activate(game, list_of_words, number_of_parameters):
       """
       Activate a specific quest.
      
       Args:
           game (Game): The game object.
           list_of_words (list): The list of words in the command.
           number_of_parameters (int): The number of parameters expected by the command.


       Returns:
           bool: True if the command was executed successfully, False otherwise.


       Examples:


       >>> from game import Game
       >>> game = Game()
       >>> game.setup("TestPlayer")
       >>> Actions.activate(game, ["activate", "Petit", "Voyageur"], 1) # doctest: +ELLIPSIS
       <BLANKLINE>
       🗡️  Nouvelle quête activée: Petit Voyageur
       📝 Prenez le bon train pour aller à Poudlard.
       <BLANKLINE>
       True
       >>> Actions.activate(game, ["activate"], 1)
       <BLANKLINE>
       La commande 'activate' prend 1 seul paramètre.
       <BLANKLINE>
       False
       """

       # If the number of parameters is incorrect, print an error message and return False.
       n = len(list_of_words)
       if n < number_of_parameters + 1:
           command_word = list_of_words[0]
           print(MSG1.format(command_word=command_word))
           return False


       # Get the quest title from the list of words (join all words after command)
       quest_title = " ".join(list_of_words[1:])


       # Try to activate the quest
       if game.player.quest_manager.activate_quest(quest_title):
           return True


       msg1 = f"\nImpossible d'activer la quête '{quest_title}'. "
       msg2 = "Vérifiez le nom ou si elle n'est pas déjà active.\n"
       print(msg1 + msg2)
       # print(f"\nImpossible d'activer la quête '{quest_title}'. \
       #             Vérifiez le nom ou si elle n'est pas déjà active.\n")
       return False



    @staticmethod
    def activate_all(game, list_of_words, number_of_parameters):
         """
         Activate all available quests.
        
         Args:
              game (Game): The game object.
              list_of_words (list): The list of words in the command.
              number_of_parameters (int): The number of parameters expected by the command.
    
    
         Returns:
              bool: True if the command was executed successfully, False otherwise.
    
    
         Examples:
    
    
         >>> from game import Game
         >>> game = Game()
         >>> game.setup("TestPlayer")
         >>> Actions.activate_all(game, ["activate_all"], 0) # doctest: +ELLIPSIS
         <BLANKLINE>
         🗡️ Nouvelle quête activée: Installation
         📝 Installez-vous à Poudlard, allez déposer votre valise dans les dortoirs.
         
         
         🗡️ Nouvelle quête activée: Grand Explorateur
         📝 Explorez tous les lieux de ce monde mystérieux.
         
         <BLANKLINE>
         True
         >>> Actions.activate_all(game, ["activate_all", "param"], 0)
         <BLANKLINE>
         La commande 'activate_all' ne prend pas de paramètre.
         <BLANKLINE>
         False

         """

         # If the number of parameters is incorrect, print an error message and return False.
         n = len(list_of_words)
         if n != number_of_parameters + 1:
              command_word = list_of_words[0]
              print(MSG0.format(command_word=command_word))
              return False
    
    
         # Activate all quests
         for quest in game.player.quest_manager.quests:
              if quest not in game.player.quest_manager.active_quests:
                   game.player.quest_manager.activate_quest(quest.title)
         return True
      


    @staticmethod
    def rewards(game, list_of_words, number_of_parameters):
       """
       Display all rewards earned by the player.
      
       Args:
           game (Game): The game object.
           list_of_words (list): The list of words in the command.
           number_of_parameters (int): The number of parameters expected by the command.


       Returns:
           bool: True if the command was executed successfully, False otherwise.


       Examples:


       >>> from game import Game
       >>> game = Game()
       >>> game.setup("TestPlayer")
       >>> Actions.rewards(game, ["rewards"], 0)
       <BLANKLINE>
       🎁 Aucune récompense obtenue pour le moment.
       <BLANKLINE>
       True
       >>> Actions.rewards(game, ["rewards", "param"], 0)
       <BLANKLINE>
       La commande 'rewards' ne prend pas de paramètre.
       <BLANKLINE>
       False
       """

       # If the number of parameters is incorrect, print an error message and return False.
       n = len(list_of_words)
       if n != number_of_parameters + 1:
           command_word = list_of_words[0]
           print(MSG0.format(command_word=command_word))
           return False


       # Show all rewards
       game.player.show_rewards()
       return True



    @staticmethod
    def give(game, list_of_words, number_of_parameters):
        """
        Give an item from the player's inventory to a character in the current room.

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
        >>> give(game, ["give", "potion", "Luna"], 3) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        vous avez donné l'objet : potion à : Luna
        <BLANKLINE>
        True
        >>> give(game, ["give", "potion"], 3)
        <BLANKLINE>
        La commande 'give' prend 3 paramètres.
        <BLANKLINE>
        False
        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG3.format(command_word=command_word))
            return False
        
        # Give the item from the player's inventory to the character in the current room.
        player = game.player
        room = player.current_room
        item_name = list_of_words[1]
        character_name = list_of_words[3]
        # Check if the item is in the player's inventory
        if item_name in player.get_inventory():
            # Check if the character is in the room
            if character_name not in room.characters:
                print(f"\nLe personnage '{character_name}' n'est pas dans cette pièce.\n")      
                return False
            else:
                item = player.get_inventory().pop(item_name)
                room.get_inventory()[item_name] = item
                print(f"\n vous avez donné l'objet : {item_name} à : {character_name}\n")
                
                # Notify quest manager about giving items
                if player.quest_manager:
                    player.quest_manager.complete_objective(f"give {item_name} to {character_name}")    
            return True
        else:
            print(f"\nL'objet '{item_name}' n'est pas dans cette pièce.\n")
            return False
            


    def add(game, list_of_words, number_of_parameters,):
        """
        Add an ingredient from the player's inventory to the cauldron.

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
        >>> add(game, ["add", "ingredient_1"], 3) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        Vous avez ajouté l'ingrédient dans le chaudron : ingredient_1
        <BLANKLINE>
        True
        >>> add(game, ["add"], 3)
        <BLANKLINE>
        La commande 'add' prend 3 paramètres.
        <BLANKLINE>
        False
        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Add the ingredient from the player's inventory to the cauldron.
        player = game.player
        room = player.current_room
        item_name = list_of_words[1]
        # Check if the item is in the player's inventory
        if item_name in player.get_inventory():
            # Check if the cauldron is in the player's inventory
            if "chaudron" in player.get_inventory():
                item = player.get_inventory().pop(item_name)
                room.get_inventory()[item_name] = item
                print(f"\nVous avez ajouté l'ingrédient dans le chaudron : {item_name}\n")
                
                # Notify quest manager about adding items
                if player.quest_manager:
                    player.quest_manager.complete_objective(f"add {item_name} to chaudron") 
                return True
        else:
            print(f"\nL'objet '{item_name}' n'est pas dans l'inventaire du joueur.\n")
            return False



    def spell(game, list_of_words, number_of_parameters):
        """
        Cast a spell using an item from the player's inventory.
        
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
        >>> spell(game, ["spell", "expecto_patronum"], 1) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        Vous lancez le sort Expecto Patronum avec succès !
        <BLANKLINE>
        True
        >>> spell(game, ["spell"], 1)
        <BLANKLINE>
        La commande 'spell' prend 1 seul paramètre.
        <BLANKLINE>
        False
        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Cast the spell using an item from the player's inventory.
        player = game.player
        spell_name = list_of_words[1]
        if spell_name == "expecto_patronum":
            if "baguette" in player.get_inventory():
                print("\nVous lancez le sort Expecto Patronum avec succès !\n")
                
                # Notify quest manager about casting the spell      
                if player.quest_manager:
                    player.quest_manager.complete_objective("spell expecto_patronum")
                return True
            else:
                print("\nVous n'avez pas la baguette magique pour lancer ce sort.\n")
                return False
        else:
            print(f"\nLe sort '{spell_name}' n'est pas reconnu.\n")
            return False
        