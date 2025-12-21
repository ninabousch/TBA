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

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.directions = set()
    
    # Setup the game
    def setup(self):

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

        
        # Setup rooms

        foret = Room("Foret", "dans la Forêt Interdite, un lieu où même la lumière du jour semble hésiter à entrer. Vous entendez une brise légère transportant des bruits étranges. Cet endroit vous donne la chair de poule.")
        self.rooms.append(foret)
        gare = Room("Gare", "à la gare king's Cross, entouré par le brouhaha des voyageurs pressés et les sifflements des trains à vapeur. Autour de vous, des familles moldues passent sans rien remarquer, tandis qu’un groupe d’élèves en robe noire rit en poussant des chariots chargés de coffres et de cages à hiboux.\n Vous devez prendre le train pour Poudlard ! Choisissez le bon : \n N. L'Ombre du Nord \n E. L'Eclair Ecarlate \n S. Le Noisy-Express")
        self.rooms.append(gare)
        wrongtrain = Room("WrongTrain", "dans un train sombre et froid. Vous réalisez trop tard qu’il se dirige vers Durmstrang... \n PERDU ! \n Tapez 'quit' pour quitter le jeu.")
        self.rooms.append(wrongtrain)
        train = Room("Train", "désormais dans le train à destination de Poudlard dont les fenêtres offrent une vue sur la campagne anglaise qui défile.")
        self.rooms.append(train)
        noisytrain = Room("NoisyTrain", "dans un wagon bruyant rempli d'élèves turbulents. Vous réalisez trop tard que c'est le RER A qui vous emmène à ESIEE Paris \n PERDU ! \n Tapez 'quit' pour quitter le jeu.")
        self.rooms.append(noisytrain)
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
        gare.exits = {"N" : wrongtrain, "E" : train, "S" : noisytrain}
        train.exits = {"E" : entree}
        entree.exits = {"N" : cabane, "E" : couloir, "S" : chemin}
        couloir.exits = {"N" : dortoirs, "E" :escalier, "S" : banquet, "O" : entree}
        escalier.exits = {"U" : palier, "D" : cachots, "O" : couloir}
        cachots.exits = {"U" : escalier}
        palier.exits = {"N" : classe, "S" : bibliotheque, "D" : escalier}
        cabane.exits = {"E" : dortoirs, "S" : couloir}
        chemin.exits = {"N" : entree, "S" : foret}
        dortoirs.exits = {"O" : cabane, "S" : couloir}
        classe.exits = {"S" : palier}
        bibliotheque.exits = {"N" : palier}
        banquet.exits = {"N" : couloir}

        #setup items in rooms
        
        loups = Item("loups", "Plongez dans les secrets les plus sombres de la magie avec ce guide inédit sur les loups-garous.", "1.4")
        bibliotheque.inventory["loups"]= loups
        trolls = Item("trolls", "Découvrez les trolls leurs histoire, forces et faiblesses ", "1.3")
        bibliotheque.inventory["trolls" ]= trolls
        acro = Item("acromentules", "Découvrez les secrets d’Aragog et de sa colonie", "1.5")
        bibliotheque.inventory["acromentules" ] = acro
        fantomes = Item("fantomes", "Découvrez les secrets des résidents spectrales de Poudlard .", "1.2")
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

        papier = Item("papier", "je l'ai vue sortir de la forêt", "0.1")
        palier.inventory["papier"] = papier 
        
        portoloin = Item("portoloin", "Un portoloin ancien, orné de symboles mystérieux.", "2.1")
        couloir.inventory["portoloin"] = portoloin 

        sorts = Item("sortileges", "De « Lumos » à « Expecto Patronum », explorez les sortilèges.", "1.9")
        classe.inventory["sortileges" ] = sorts
        potions = Item("potions", "Plongez dans les chaudrons fumants du cours de potions.", "1.8")
        classe.inventory["potions" ] = potions
        chaudron = Item("chaudron", "Un chaudron en étain, essentiel pour toute potion bien préparée.", "3")
        classe.inventory["chaudron"] = chaudron

        bonbons = Item("bonbons", "Un assortiment de bonbons magiques pour une pause sucrée.", "0.3")
        train.inventory["bonbons"] = bonbons
        
        chouette = Item("chouette", "Une chouette blanche aux yeux perçants, prête à livrer votre courrier magique.", "1.7")
        entree.inventory["chouette"] = chouette

        cookies = Item("cookies", "Un pot de cookies fraîchement cuits, parfaits pour une collation rapide.", "0.5")
        banquet.inventory["cookies"] = cookies

        parchemin = Item("parchemin", "Un plan de la forêt interdite pour vous guider dans cet endroit effrayant.", "0.2")
        cabane.inventory["parchemin"] = parchemin
        bottes = Item("bottes", "Une paire de bottes robustes, elles vous sont nécéssaires pour arpenter les chemins escarpés de la foret interdite.", "1")
        cabane.inventory["bottes"] = bottes

        tissu = Item("tissu", "Un morceau de tissu déchiré, peut-être d'un vêtement, un croissant de lune y est brodé.", "0.1")
        chemin.inventory["tissu"] = tissu

        branche = Item("branche", "Une branche de saule cogneur se trouve suspicieusement sur votre chemin.", "0.6")
        foret.inventory["branche"] = branche

        potion = Item("potion", "Une potion mystérieuse aux couleurs changeantes.", "0.9")
        cachots.inventory["potion"] = potion

        

        # Setup characters in rooms

        Hagrid = Character("Hagrid", "Demi-géant, garde-chasse de Poudlard et ami fidèle des créatures magiques.", cabane, ["Bonjour"], False)
        cabane.characters["Hagrid"] = Hagrid
        
        Dumbledore = Character("Dumbledore", "Le directeur de Poudlard, connu pour sa grande sagesse et son puissant talent en magie.", banquet, ["Bonjour"], False)
        banquet.characters["Dumbledore"] = Dumbledore
        Mcgonagall = Character("McGonagall", "La professeur de métamorphose stricte mais juste, toujours prête à défendre ses élèves.", banquet, ["Bonjour"],True)
        banquet.characters["McGonagall"] = Mcgonagall
        Pomfresh = Character("Pomfresh", "L'infirmière de Poudlard, soigne les blessures des élèves avec douceur.", banquet, ["Bonjour"], True)
        banquet.characters["Pomfresh"] = Pomfresh
        Choipeau = Character("Choipeau", "Le chapeau magique qui répartit les nouveaux élèves dans les différentes maisons de Poudlard.", banquet, ["Bonjour"], False)
        banquet.characters["Choipeau"] = Choipeau

        Dobby = Character("Dobby", "Un elfe de maison loyal et courageux, toujours prêt à aider.", cachots, ["Bonjour", "Dobby est libre!"], True)
        cachots.characters["Dobby"] = Dobby

        Lupin = Character("Lupin", "Un professeur de défense contre les forces du mal.", classe, ["Bonjour"], False)
        classe.characters["Lupin"] = Lupin
        Rogue = Character("Rogue", "Le professeur de potions mystérieux et redouté, avec un passé complexe.", classe, ["Bonjour"], False)
        classe.characters["Rogue"] = Rogue

        Drago = Character("Drago", "Un élève de Serpentard, connu pour son arrogance et sa rivalité avec les Gryffondors.", dortoirs, ["Bonjour"], True)
        dortoirs.characters["Drago"] = Drago
        Luna = Character("Luna", "Une élève excentrique de Serdaigle, connue pour ses idées originales et sa curiosité sans bornes.", dortoirs, ["Bonjour"], False)
        dortoirs.characters["Luna"] = Luna

        Firenze = Character("Firenze", "Un centaure sage et mystérieux, gardien des secrets de la forêt interdite.", foret, ["Bonjour"], False)
        foret.characters["Firenze"] = Firenze
        detraqueur = Character("Detraqueur", "Une créature sombre et terrifiante, gardien des secrets les plus sombres de la forêt interdite.", foret, ["Bonjour"], True)
        foret.characters["Detraqueur"] = detraqueur

        Fantome = Character("Fantome", "Le Baron Sanglant, résident spectral de Poudlard, errant dans les couloirs et racontant des histoires du passé.", escalier, ["Bonjour"], True)
        escalier.characters["Fantome"] = Fantome

        Hermione = Character("Hermione", "Une élève brillante et studieuse, toujours prête à aider ses amis avec ses vastes connaissances.", bibliotheque, ["Bonjour"], True)
        bibliotheque.characters["Hermione"] = Hermione

        Ron = Character("Ron", "Un élève drôle malgré lui et un peu peureux.", train, ["Bonjour"], True)
        train.characters["Ron"] = Ron
        Harry = Character("Harry", "Le célèbre garçon qui a survécu à l'attaque de Voldemort.", train, ["Bonjour"], True)
        train.characters["Harry"] = Harry
        Cedric = Character("Cedric", "Un élève talentueux et courageux de Poufsouffle.", train, ["Bonjour"], False)
        train.characters["Cedric"] = Cedric





       
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = gare

        # Initialize quest manager for the player and setup quests
        self.player.quest_manager = QuestManager(self.player)
        # Setup quests
        self._setup_quests()



    def _setup_quests(self):
        """Initialize all quests."""
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
                        , "Visiter gare"
                        , "Visiter palier"],
            reward="Titre de Grand Explorateur"
        )


        travel_quest = Quest(
            title="Grand Voyageur",
            description="Déplacez-vous 30 fois entre les lieux.",
            objectives=["Se déplacer 30 fois"],
            reward="Bottes de voyageur"
        )


        discovery_quest = Quest(
            title="Découvreur de Secrets",
            description="Découvrez les trois lieux les plus mystérieux.",
            objectives=["Visiter foret"
                        , "Visiter dortoirs"
                        , "Visiter classe"],
            reward="Clé dorée"
        )


        # Add quests to player's quest manager
        self.player.quest_manager.add_quest(exploration_quest)
        self.player.quest_manager.add_quest(travel_quest)
        self.player.quest_manager.add_quest(discovery_quest)

        
        

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
            # Déplacer les personnages non-joueurs dans chaque salle
            for room in self.rooms:
                for character in list(room.characters.values()):
                    if character.movable_status():
                        character.move()

        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, return nothing 
        if command_word not in self.commands.keys():
            return None
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
