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
    @staticmethod
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
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
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

        # Afficher les objets présents dans la pièce (s'il y en a)
        if room.get_inventory():
            for item in room.get_inventory().values():
                print(item)
        else:
            print("Il n'y a pas d'objet ici.\n")

        # Afficher les personnages non-joueurs présents dans la pièce (toujours)
        if player.current_room.characters:
            print("\nPersonnages présents dans la pièce :\n")
            for personnage in player.current_room.characters.values():
                print(personnage)
        else:
            print("Il n'y a aucun personnage ici.\n")
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
                # Notify quest manager about taking items
                if player.quest_manager:
                    # Try a common phrasing used in quests
                    player.quest_manager.complete_objective(f"take {item_name}")
                if item_name == "portoloin":
                    print("\nEn prenant le portoloin, une sensation étrange vous envahit...\n"
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
            # Notify quest manager about dropping items
            if player.quest_manager:
                player.quest_manager.complete_objective(f"drop {item_name}")
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
                # Ensure a room was saved with the portoloin before transporting
                if getattr(game, 'saved_room', None) is None:
                    print("\nLe portoloin n'a pas de destination enregistrée. Utilisez 'charger' d'abord.\n")
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
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        item_name = list_of_words[1]
        if item_name in player.get_inventory():
            if item_name == "detraqueurs":
                print("\nLes Détraqueurs sont des créatures sombres et effrayantes qui se nourrissent du bonheur des êtres vivants.\n"
                      "Ils sont souvent utilisés par les forces du mal pour semer la terreur.\n")
            if item_name == "sortileges":  
                print("En lisant le livre, vous découvrez un sortilège de protection contre les Détraqueurs : 'Expecto Patronum'.\n"
                          "Vous sentez que vous avez appris quelque chose d'important.\n")
            if item_name == "loups":
                print("Le livre raconte l'histoire des loups-garous, des êtres maudits qui se transforment lors des nuits de pleine lune.\n"
                      "Il explique également comment les reconnaître et les éviter.\n")
            if item_name == "acro":
                print("Le livre raconte l'histoire des Acromentules, des arachnides gigantesques et dangereux.\n"
                      "Il explique également comment les reconnaître et les éviter.\n")
            if item_name == "trolls ":
                print("Le livre raconte l'histoire des Trolls, des créatures massives et brutales.\n"
                      "Il explique également comment les reconnaître et les éviter.\n")
            if item_name == "fantomes":
                print("Le livre raconte l'histoire des Fantômes, des esprits errants des anciens habitants de Poudlard.\n"
                      "Il explique également comment les reconnaître et les éviter.\n")
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
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        room = player.current_room
        character_name = list_of_words[1]
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
       >>> Actions.quests(game, ["quests"], 0)
       <BLANKLINE>
       📋 Liste des quêtes:
         ❓ Grand Explorateur (Non activée)
         ❓ Grand Voyageur (Non activée)
         ❓ Découvreur de Secrets (Non activée)
       <BLANKLINE>
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
       >>> Actions.quest(game, ["quest", "Grand", "Voyageur"], 1)
       <BLANKLINE>
       📋 Quête: Grand Voyageur
       📖 Déplacez-vous 10 fois entre les lieux.
       <BLANKLINE>
       Objectifs:
         ⬜ Se déplacer 10 fois (Progression: 0/10)
       <BLANKLINE>
       🎁 Récompense: Bottes de voyageur
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
       >>> Actions.activate(game, ["activate", "Grand", "Voyageur"], 1) # doctest: +ELLIPSIS
       <BLANKLINE>
       🗡️  Nouvelle quête activée: Grand Voyageur
       📝 Déplacez-vous 10 fois entre les lieux.
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
         🗡️  Nouvelle quête activée: Grand Explorateur
         📝 Explorez 5 pièces différentes dans le jeu.
         
         
         🗡️  Nouvelle quête activée: Potion Magique
         📝 Récupérez les ingrédients et préparez la potion magique.
         
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
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        room = player.current_room
        item_name = list_of_words[1]
        character_name = list_of_words[2]
        if item_name in player.get_inventory():
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
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        room = player.current_room
        item_name = list_of_words[1]
        if item_name in player.get_inventory():
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
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
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