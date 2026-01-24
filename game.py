# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from quest import Quest, QuestManager

class Game:
    """
    Class representing the game.
    
    This class manages the entire game environment, including rooms, commands,
    the player, and game state. It handles the main game loop and coordinates
    interactions between different game components.
    
    Attributes:
        finished (bool): Flag indicating whether the game has ended.
        rooms (list): List of all Room objects in the game.
        commands (dict): Dictionary mapping command names to Command objects.
        player (Player): The player object controlling the game.
        directions (set): Set of valid direction tokens (N, S, E, O, U, D, etc.).
    
    Methods:  
        __init__(self) : The constructor.
        setup(self) : Initializes all game elements (rooms, items, characters, commands, player, quests).
        play(self) : Main game loop that processes player commands until the game ends.
        print_welcome(self) : Displays the welcome message and starting room description.
        process_command(self, command_string) : Parses and executes a player command.   
        _setup_quests(self) : Initializes all quests available in the game.
        def check_win_conditions(self) : Checks if the player has met the conditions to win the game.
        def check_lose_conditions(self) : Checks if the player has met the conditions to lose the game.

    """


    # Constructor
    def __init__(self):
        """
        Initialize a new Game object.
        
        Sets up the initial game state with empty collections and no player.
        """
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.directions = set()
    
    # Setup the game
    def setup(self):
        """
        Initialize and configure all game elements.
        
        This method sets up:
        - All available commands with their descriptions and actions
        - All rooms with their descriptions and connections
        - All items distributed across rooms
        - All characters positioned in specific rooms
        - The player object and starting position
        - All quests for the player
        """

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O) ou monter (U) ou descendre (D)", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : afficher l'historique des pièces visitées", Actions.history, 0)
        self.commands["history"] = history  
        back = Command("back", " : revenir à la pièce précédente", Actions.back, 0)
        self.commands["back"] = back
        inventory = Command("inventory", " : afficher l'inventaire du joueur", Actions.inventory, 0)
        self.commands["inventory"] = inventory
        look = Command("look", " : regarder autour de soi dans la pièce actuelle", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : prendre un objet dans la pièce actuelle", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : déposer un objet de l'inventaire du joueur dans la pièce actuelle", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " : examiner un objet de l'inventaire du joueur", Actions.check, 0)
        self.commands["check"] = check
        charger = Command("charger", " : charger une pièce dans le portoloin", Actions.charger, 0)
        self.commands["charger"] = charger
        use = Command("use", " : utiliser un objet de l'inventaire du joueur", Actions.use, 1)
        self.commands["use"] = use
        read = Command("read", " : lire un objet de l'inventaire du joueur", Actions.read, 1)
        self.commands["read"] = read
        talk = Command("talk", " : parler à un personnage dans la pièce actuelle", Actions.talk, 1)
        self.commands["talk"] = talk
        quests = Command("quests", " : afficher les quêtes en cours et leurs statuts", Actions.quests, 0)
        self.commands["quests"] = quests
        rewards = Command("rewards", " : afficher les récompenses obtenues", Actions.rewards, 0)
        self.commands["rewards"] = rewards 
        quest = Command("quest", " <titre de la quête> : afficher les détails d'une quête spécifique", Actions.quest, 1)
        self.commands["quest"] = quest
        activate = Command("activate", " : activer une quête", Actions.activate, 1)
        self.commands["activate"] = activate  
        activate_all = Command("activate_all", " : activer toutes les quêtes", Actions.activate_all, 0)
        self.commands["activate_all"] = activate_all
        give = Command("give", " < objet + to + personnage > : donner un objet à un personnage dans la pièce actuelle", Actions.give, 3)
        self.commands["give"] = give
        spell = Command("spell", " : lancer un sort avec un objet de l'inventaire du joueur", Actions.spell, 1)         
        self.commands["spell"] = spell
        add = Command("add", " < objet + to + objet > : ajouter un ingrédient dans le chaudron", Actions.add, 3)   
        self.commands["add"] = add
        

        
        # Setup rooms

        foret = Room("Foret", "dans la Forêt Interdite, un lieu où même la lumière du jour semble hésiter à entrer. Vous entendez une brise légère transportant des bruits étranges. Cet endroit vous donne la chair de poule.")
        self.rooms.append(foret)
        gare = Room("Gare", "à la gare king's Cross, entouré par le brouhaha des voyageurs pressés et les sifflements des trains à vapeur. Autour de vous, des familles moldues passent sans rien remarquer, tandis qu’un groupe d’élèves en robe noire rit en poussant des chariots chargés de coffres et de cages à hiboux.\n Vous devez prendre le train pour Poudlard ! Choisissez le bon : \n N. L'Ombre du Nord \n E. L'Eclair Ecarlate \n S. Le Noisy-Express")
        self.rooms.append(gare)
        lombredunord = Room("LOmbreDuNord", "dans un train sombre et froid. Vous réalisez trop tard qu’il se dirige vers Durmstrang.")
        self.rooms.append(lombredunord)
        train = Room("Train", "désormais dans le train à destination de Poudlard dont les fenêtres offrent une vue sur la campagne anglaise qui défile.")
        self.rooms.append(train)
        noisyexpress = Room("NoisyExpress", "dans un wagon bruyant rempli d'élèves turbulents. Vous réalisez trop tard que c'est le RER A qui vous emmène à ESIEE Paris.")
        self.rooms.append(noisyexpress)
        entree = Room("Entree", "dans l’entrée de Poudlard. Devant vous, les grandes portes s’élèvent, flanquées de gargouilles qui semblent vous observer. Une lueur dorée filtre à travers les vitraux, projetant des ombres mouvantes sur les dalles usées.")
        self.rooms.append(entree)
        couloir = Room("Couloir", "dans le couloir principal qui mène aux différentes pièces de l'école. Les murs de pierre froide sont ornés de portraits animés qui vous observent, murmurant entre eux.")
        self.rooms.append(couloir)
        bibliotheque = Room("Bibliotheque", "dans dans la majestueuse et imposante bibliothèque de Poudlard. Un silence oppressant règne, seulement rompu par le bruissement des pages tournées et le tictac d’une horloge ensorcelée qui tourne à l’envers.")
        self.rooms.append(bibliotheque)
        classe = Room("Classe", "dans la classe de défense contre les forces du mal du professeur Lupin. Une odeur étrange vous enveloppe : un mélange de parchemin ancien et de plantes séchées. Les étagères sont chargées de boîtes étiquetées “dangereux”, de fioles remplies de liquides troubles et de créatures empaillées qui semblent vous suivre du regard.")
        self.rooms.append(classe)
        banquet = Room("Banquet", "dans la grande salle de réception. La Grande Salle est un spectacle à couper le souffle : un plafond ensorcelé reflète un ciel étoilé en mouvement, tandis que les quatre longues tables (Gryffondor, Serpentard, Poufsouffle, Serdaigle) sont garnies de plats fumants. Les bougies flottent au-dessus des têtes, projetant une lumière dorée sur les bannières aux couleurs des maisons.")
        self.rooms.append(banquet)
        dortoirs = Room("Dortoirs", "dans les dortoirs des élèves. Cette grande salle circulaire a des murs de pierre ornés des blasons des quatre maisons. Quatre portes mènent aux dortoirs respectifs.")
        self.rooms.append(dortoirs)
        cabane = Room("Cabane", "dans la cabane d'Hagrid. On y sent la fourrure mouillée et les citrouilles trop mûres. Le plancher craque sous vos pieds, et un feu de cheminée réchauffe la pièce, autour duquel ronronne un chat à trois pattes.")
        self.rooms.append(cabane)
        chemin = Room("Chemin", "sur un chemin sombre qui serpente à l’extérieur de Poudlard. Le chemin est éclairé seulement par la lueur tremblante de la lune, filtrée à travers les nuages. Les arbres bordant le sentier semblent se pencher vers vous de manière menaçantes.")
        self.rooms.append(chemin)
        escalier = Room("Escalier", "dans l’escalier qui relie le couloir au palier de l’étage. Les marches de pierre usée de l’escalier sont éclairées par des torches dont les flammes dansent comme si elles étaient vivantes. Certaines marches disparaissent quand vous posez le pied dessus.")
        self.rooms.append(escalier)
        palier = Room("Palier", "sur le palier de l’étage. Le palier circulaire est éclairé par une fenêtre en vitrail représentant un phénix, dont les couleurs changent selon la lumière. Deux portes en chêne massif se font face.")
        self.rooms.append(palier)
        cachots = Room("Cachots", "dans les cachots sombres et humides de Poudlard. L'air est frais. Ce lieu n'est pas rassurant.")
        self.rooms.append(cachots)

        # setup directions
        # Store allowed direction tokens on the game object so actions can check them
        self.directions = set(['N', 'NORD', 'Nord', 'nord', 'S', 'SUD', 'Sud', 'sud', 'E', 'EST', 'Est', 'est', 'O', 'OUEST', 'Ouest', 'ouest', 'U', 'UP', 'Up', 'up', 'D', 'DOWN', 'Down', 'down'])



        # Create exits for rooms

        foret.exits = {"N" : chemin}
        gare.exits = {"N" : lombredunord, "E" : train, "S" : noisyexpress}
        train.exits = {"E" : entree}
        entree.exits = {"N" : cabane, "E" : couloir, "S" : chemin}
        couloir.exits = {"N" : dortoirs, "E" :escalier, "S" : banquet, "O" : entree}
        escalier.exits = {"U" : palier, "D" : cachots, "O" : couloir}
        cachots.exits = {"U" : escalier}
        palier.exits = {"N" : classe, "S" : bibliotheque, "D" : escalier}
        cabane.exits = {"E" : dortoirs, "S" : entree}
        chemin.exits = {"N" : entree, "S" : foret}
        dortoirs.exits = {"O" : cabane, "S" : couloir}
        classe.exits = {"S" : palier}
        bibliotheque.exits = {"N" : palier}
        banquet.exits = {"N" : couloir}

        #setup items in rooms
        
        loups = Item("loups", "(livre) Plongez dans les secrets les plus sombres de la magie avec ce guide inédit sur les loups-garous.", "1.4")
        bibliotheque.inventory["loups"]= loups
        trolls = Item("trolls", "(livre) Découvrez les trolls leurs histoire, forces et faiblesses ", "1.3")
        bibliotheque.inventory["trolls" ]= trolls
        acro = Item("acromentules", "(livre) Découvrez les secrets d’Aragog et de sa colonie", "1.5")
        bibliotheque.inventory["acromentules" ] = acro
        detraqueurs = Item("detraqueurs", "(livre) Plongez dans l'effrayant univers des Détraqueurs.", "1.6")
        bibliotheque.inventory["detraqueurs" ] = detraqueurs
        fantomes = Item("fantomes", "(livre) Découvrez les secrets des résidents spectrales de Poudlard .", "1.2")
        bibliotheque.inventory["fantomes" ] = fantomes


        
        echarpe = Item("echarpe", "Une écharpe aux couleurs rouge et or, symbole de courage et de bravoure.", "0.5")
        dortoirs.inventory["echarpe" ] = echarpe
        chapeau = Item("chapeau", "Un chapeau pointu noir orné d'une bande argentée, parfait pour compléter votre tenue de sorcier.", "0.4")
        dortoirs.inventory["chapeau" ] = chapeau
        journal = Item("journal", "Un petit carnet à couverture en cuir qui ne semble pas à sa place ici.", "0.7")
        dortoirs.inventory["journal" ]  = journal
        chaussettes = Item("chaussettes", "Une paire de chaussettes colorées et confortables, idéales pour se détendre après une longue journée de cours.", "0.3")
        dortoirs.inventory["chaussettes" ] = chaussettes


        valise = Item("valise", "Une valise en cuir usée, prête pour une aventure magique.", "8")
        gare.inventory["valise" ] = valise
        baguette= Item("baguette", "N'oubliez pas votre baguette magique!", "0.5")
        gare.inventory["baguette"] = baguette

        papier = Item("papier", "vous trouvez un papier par terre prenez le et lisez le", "0.1")
        palier.inventory["papier"] = papier 
        
        portoloin = Item("portoloin", "Un portoloin ancien, orné de symboles mystérieux.", "2.1")
        couloir.inventory["portoloin"] = portoloin 

        sortileges = Item("sortileges", "De « Lumos » à « Expecto Patronum », explorez les sortilèges.", "1.9")
        classe.inventory["sortileges" ] = sortileges
        chaudron = Item("chaudron", "Un chaudron en étain, essentiel pour toute potion bien préparée.", "3")
        classe.inventory["chaudron"] = chaudron
        mandragore = Item("mandragore", "Une mandragore fraîchement récoltée, ses racines sont encore couvertes de terre.", "2.5")
        classe.inventory["mandragore"] = mandragore


        bonbons = Item("bonbons", "Un assortiment de bonbons magiques pour une pause sucrée.", "0.3")
        train.inventory["bonbons"] = bonbons
        
        chouette = Item("chouette", "Une chouette blanche aux yeux perçants, prête à livrer votre courrier magique.", "1.7")
        entree.inventory["chouette"] = chouette

        cookies = Item("cookies", "Un pot de cookies fraîchement cuits, parfaits pour une collation rapide.", "0.5")
        banquet.inventory["cookies"] = cookies

        parchemin = Item("parchemin", "Un plan de la forêt interdite pour vous guider dans cet endroit effrayant.", "0.2")
        cabane.inventory["parchemin"] = parchemin
        bottes = Item("bottes", "Une paire de bottes robustes, utiles pour arpenter les chemins escarpés de la forêt interdite.", "1")
        cabane.inventory["bottes"] = bottes
        licorne = Item("licorne", "Un poil de licorne, réputé pour ses propriétés magiques et sa pureté.", "0.3")
        cabane.inventory["licorne"] = licorne

        tissu = Item("tissu", "Un morceau de tissu déchiré, peut-être d'un vêtement, un croissant de lune y est brodé.", "0.1")
        chemin.inventory["tissu"] = tissu

        branche = Item("branche", "Une branche de saule cogneur se trouve suspicieusement sur votre chemin.", "0.6")
        foret.inventory["branche"] = branche

        phenix = Item("phenix", "Une larme de phénix, symbole de renaissance et de puissance magique.", "0.4")
        cachots.inventory["phenix"] = phenix

        # Setup characters in rooms

        Hagrid = Character("Hagrid", "Demi-géant, garde-chasse de Poudlard et ami fidèle des créatures magiques.", cabane, ["Bonjour à toi !", "Veux-tu voir mon nouvel animal de companie? Il s'appelle Fumier."], False)
        cabane.characters["Hagrid"] = Hagrid

        Dumbledore = Character("Dumbledore", "Le directeur de Poudlard, connu pour sa grande sagesse et son puissant talent en magie.", banquet, ["Bienvenue à Poudlard jeune sorcier.", "Je vous avertis, une créature rôde dans les couloirs et menace la sécurité de l'école. Soyez prudent."], False)
        banquet.characters["Dumbledore"] = Dumbledore
        Mcgonagall = Character("McGonagall", "La professeur de métamorphose stricte mais juste, toujours prête à défendre ses élèves.", banquet, ["Retournez immédiatement à vos dortoirs!", "Avez-vous des questions ?"],True)
        banquet.characters["McGonagall"] = Mcgonagall
        Pomfresh = Character("Pomfresh", "L'infirmière de Poudlard, soigne les blessures des élèves avec douceur.", banquet, ["Comment puis-je t'aider?", "Comment allez-vous?"], True)
        banquet.characters["Pomfresh"] = Pomfresh
        Choixpeau = Character("Choixpeau", "Le chapeau magique qui répartit les nouveaux élèves dans les différentes maisons de Poudlard.", banquet, ["Griffondor, Poussoufle, Serdaigle ou Serpentard?"], False)
        banquet.characters["Choixpeau"] = Choixpeau

        Dobby = Character("Dobby", "Un elfe de maison loyal et courageux, toujours prêt à aider.", cachots, ["Aidez Dobby à sortir, Dobby se sent seul.", "Dobby aimerait aider.","Dobby est libre!"], False)
        cachots.characters["Dobby"] = Dobby

        Lupin = Character("Lupin", "Un professeur de défense contre les forces du mal.", classe, ["Que veux-tu apprendre aujourd'hui?", "Tu es prêt à affronter les forces du mal?"],False)
        classe.characters["Lupin"] = Lupin
        Rogue = Character("Rogue", "Le professeur de potions mystérieux et redouté, avec un passé complexe.", classe, ["Gare à toi, je t'ai à l'oeil !", "As-tu fini ta potion ?"], False)
        classe.characters["Rogue"] = Rogue

        Drago = Character("Drago", "Un élève de Serpentard, connu pour son arrogance et sa rivalité avec les Gryffondors.", dortoirs, ["Va-t'en sale sang de Bourbe !", "Je suis de sang pur."], True)
        dortoirs.characters["Drago"] = Drago
        Luna = Character("Luna", "Une élève excentrique de Serdaigle, connue pour ses idées originales et sa curiosité sans bornes.", dortoirs, ["La lune sera rose ce soir, veux tu venir l'observer avec moi? ", "J'ai eu une pensée tout à l'heure mais je ne m'en souviens plus...", "J'ai essaye de rendre un détraqueur gentil mais il m'a échappé...", "J'ai honte, aide moi à le retrouver."], False)
        dortoirs.characters["Luna"] = Luna

        Firenze = Character("Firenze", "Un centaure sage et mystérieux, gardien des secrets de la forêt interdite.", foret, ["Tu n'as pas le droit d'être ici !",  "Les détraqueurs rôdent dans la forêt."], False)
        foret.characters["Firenze"] = Firenze
        Detraqueur = Character("Detraqueur", "Une créature sombre et terrifiante, gardien des secrets les plus sombres de la forêt interdite.", foret, ["Shhhhhaaaaarh"], False)
        foret.characters["Detraqueur"] = Detraqueur

        Fantome = Character("Fantome", "Le Baron Sanglant, résident spectral de Poudlard, errant dans les couloirs et racontant des histoires du passé.", escalier, ["Ne va surtout pas au cachot.", "L'ambiance est pesante en ce moment."], True)
        escalier.characters["Fantome"] = Fantome

        Hermione = Character("Hermione", "Une élève brillante et studieuse, toujours prête à aider ses amis avec ses vastes connaissances.", bibliotheque, ["tu devrais être en train de réviser à la bibliothèque au lieu de traîner dans les couloirs.", "Est-ce que tu as fini ton devoir ?"], True)
        bibliotheque.characters["Hermione"] = Hermione

        Ron = Character("Ron", "Un élève drôle malgré lui et un peu peureux.", train, ["Je ne sais pas pourquoi mais j'ai comme un mauvais pressentiment pour cette année."], True)
        train.characters["Ron"] = Ron
        Harry = Character("Harry", "Le célèbre garçon qui a survécu à l'attaque de Voldemort.", train, ["Je suis plus célèbre que toi alors va voir ailleurs."], True)
        train.characters["Harry"] = Harry
        Cedric = Character("Cedric", "Un élève talentueux et courageux de Poufsouffle.", train, ["Bonjour, tu peux t'assoir à côté de moi si tu le souhaite.", "Evite Harry, la célébrité lui monte à la tête en ce moment."], False)
        train.characters["Cedric"] = Cedric





       
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = gare
        self.player.history = [gare]

        # Initialize quest manager for the player and setup quests
        self.player.quest_manager = QuestManager(self.player)
        # Setup quests
        self._setup_quests()



    def _setup_quests(self):
        """
        Initialize all quests available in the game.
        
        Creates a series of interconnected quests with varying objectives:
        - train_quest: Tutorial quest to reach Poudlard
        - installation_quest: Basic quest to get settled
        - exploration_quest: Visit all locations
        - livre_quest: Discover information about creatures
        - talking_quest: Interact with key characters
        - dobby_quest: Help free an enslaved elf
        - potion_quest: Craft a special potion
        - fighting_quest: Defeat a dangerous creature
        - saving_quest: Complete all other quests to save Poudlard
        
        All quests are added to the player's quest manager.
        """

        train_quest = Quest(
            title="Petit Voyageur",
            description="Prenez le bon train pour aller à Poudlard.",
            objectives=["Aller dans le bon train"],
            reward="Ticket de train"
        )


        installation_quest = Quest(
            title="Installation",
            description="Installez-vous à Poudlard, allez déposer votre valise dans les dortoirs.",
            objectives=["take valise", "Aller à l'entree", "Aller aux dortoirs", "drop valise"],
            reward="Uniforme de Poudlard"
        )


        exploration_quest = Quest(
            title="Grand Explorateur",
            description="Explorez tous les lieux de ce monde mystérieux.",
            objectives=["Visiter foret"
                        , "Visiter dortoirs"
                        , "Visiter classe"
                        , "Visiter chemin"
                        , "Visiter cabane"
                        , "Visiter banquet"
                        , "Visiter bibliotheque"
                        , "Visiter escalier"
                        , "Visiter couloir"
                        , "Visiter entree"
                        , "Visiter train"
                        , "Visiter palier"
                        , "Visiter cachots"],
            reward="Titre de Grand Explorateur"
        )


        livre_quest = Quest(
            title="Qui est l'ombre",
            description="Découvrez quelle est la créature qui rôde dans les couloirs et menace Poudlard. Prenez le livre à son sujet dans la bibliothèque pour en savoir plus.",
            objectives=["Aller à la bibliotheque", "take detraqueurs", "read detraqueurs"],
            reward="Grimoire magique"
        )


        talking_quest = Quest(
            title="Maître de la Conversation",
            description="Parlez à ces 5 personnages différents dans le jeu (Dumbledore, Hagrid, Rogue, Hermione, Firenze).",                   
            objectives=["talk à Dumbledore", "talk à Hagrid", "talk à Rogue", "talk à Hermione", "talk à Firenze"],
            reward="Amulette de communication"
        )   


        dobby_quest = Quest(
            title="Libérateur d'Elfe",
            description="Aidez Dobby à se libérer de l'esclavage en lui offrant un vêtement.",
            objectives=["take chaussettes", "give chaussettes to Dobby"],
            reward="Gratitude de Dobby"
        )


        potion_quest = Quest(
            title="Apprenti Potioniste",
            description="faire une potion de vérité pour faire parler Luna de son secret.", 
            objectives=["Add licorne to chaudron","Add phenix to chaudron","Add mandragore to chaudron"],
            reward="Potion de vérité"
        )   


        fighting_quest = Quest(
            title="Combattant Courageux",
            description="Vaincre le détraqueur dans la forêt interdite grâce aux sort de protection.",
            objectives=["take baguette","aller à la classe", "take sortileges", "read sortileges", "aller à la foret","spell expecto_patronum", "use portoloin"],
            reward="Cape d'invisibilité"
        )


        saving_quest = Quest(
            title="Sauveur de Poudlard",
            description="Sauvez Poudlard de la menace qui plane sur elle en accomplissant toutes les autres quêtes.",
            objectives=["Compléter Combattant Courageux","Compléter Grand Explorateur", "Compléter Petit Voyageur"],
            reward="Héros de Poudlard"
        )


        # Add quests to player's quest manager
        self.player.quest_manager.add_quest(train_quest)
        self.player.quest_manager.add_quest(installation_quest)
        self.player.quest_manager.add_quest(exploration_quest)
        self.player.quest_manager.add_quest(livre_quest)
        self.player.quest_manager.add_quest(talking_quest)
        self.player.quest_manager.add_quest(dobby_quest)
        self.player.quest_manager.add_quest(potion_quest)    
        self.player.quest_manager.add_quest(fighting_quest)   
        self.player.quest_manager.add_quest(saving_quest)

        # Activate the main quest
        self.player.quest_manager.activate_quest("Sauveur de Poudlard")
        
        

    # Play the game
    def play(self):
        """
        Main game loop.
        
        Orchestrates the entire game flow:
        1. Sets up all game elements
        2. Displays the welcome message
        3. Continuously processes player commands until the game ends
        4. Moves non-player characters after movement commands
        
        Returns:
            None: Game ends when self.finished becomes True.
        """
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player and process it
           command_input = input("> ")
           executed_command = self.process_command(command_input)

           # Check for win conditions after each command
           self.check_win_conditions()

           # Check for lose conditions after each command
           self.check_lose_conditions()

           # Déplacer les personnages non-joueurs uniquement après la commande 'go'
           if executed_command == "go":
               for room in self.rooms:
                   for character in list(room.characters.values()):
                       if character.movable_status():
                           character.move()


        return None


    # Define winning conditions 
    def check_win_conditions(self):
        """
        Check if the player has met the conditions to win the game.
        
        The game is won when the main quest "Sauveur de Poudlard" is completed.
        """
        if not self.finished:
            saving_quest = self.player.quest_manager.get_quest_by_title("Sauveur de Poudlard")
            if saving_quest and saving_quest.is_completed:
                print("\n 🏆 Félicitations ! Vous avez sauvé Poudlard et remporté le jeu ! 🏆")
                print("Vous êtes désormais le Héros de Poudlard.🎖️🎖️🎖️")
                self.finished = True


    # Define loosing conditions
    def check_lose_conditions(self):
        """
        Check if the player has met the conditions to lose the game.
        
        The game is lost when the player enters a losing room.
        """
        if not self.finished:
            # Example losing condition: entering a specific room
            if self.player.current_room.name == "LOmbreDuNord" or self.player.current_room.name == "NoisyExpress":
                print("\n💀 Vous avez perdu le jeu ! 💀")
                print("Mieux vaut réessayer et faire les bons choix cette fois-ci.\n")
                self.finished = True
        

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """
        Parse and execute a command entered by the player.
        
        Args:
            command_string (str): The raw command input from the player.
        
        Returns:
            str or None: The command word if successfully executed, None otherwise.
        
        Process:
        1. Splits the command string by spaces
        2. Extracts the first word as the command name
        3. Validates the command exists in the commands dictionary
        4. Executes the command with its associated action
        5. Returns the command name for tracking purposes
        """

        # Split the command string into a list of words
        list_of_words = command_string.split()

        # If the command is empty, return nothing
        if not list_of_words:
            return None

        command_word = list_of_words[0]

        # If the command is not recognized, return nothing
        if command_word not in self.commands.keys():
            return None

        # If the command is recognized, execute it and return the command word
        command = self.commands[command_word]
        command.action(self, list_of_words, command.number_of_parameters)
        return command_word


    # Print the welcome message
    def print_welcome(self):
        """
        Display the welcome message and initial game information.
        
        Shows:
        - A personalized greeting with the player's name
        - A help hint
        - The full description of the starting room
        """
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.et pour voir toutes les commandes disponibles")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
