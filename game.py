# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item

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
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O) ou monter (M) ou descendre (D)", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : afficher l'historique des pièces visitées", Actions.history, 0)
        self.commands["history"] = history  
        back = Command("back", " : revenir à la pièce précédente", Actions.back, 0)
        self.commands["back"] = back
        inventory = Command("inventory", " : afficher l'inventaire du joueur", Actions.inventory, 0)
        self.commands["inventory"] = inventory
        look = Command("look", " : regarder autour de soi dans la pièce actuelle", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " <item_name> : prendre un objet dans la pièce actuelle", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " <item_name> : déposer un objet de l'inventaire du joueur dans la pièce actuelle", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " <item_name> : examiner un objet de l'inventaire du joueur", Actions.check, 0)
        self.commands["check"] = check
        
        # Setup rooms

        foret = Room("Foret", "dans la Forêt Interdite, un lieu où même la lumière du jour semble hésiter à entrer. Vous entendez une brise légère transportant des bruits étranges. Cet endroit vous donne la chair de poule.")
        self.rooms.append(foret)
        gare = Room("Gare", "à la gare king's Cross, entouré par le brouhaha des voyageurs pressés et les sifflements des trains à vapeur. Autour de vous, des familles moldues passent sans rien remarquer, tandis qu’un groupe d’élèves en robe noire rit en poussant des chariots chargés de coffres et de cages à hiboux.")
        self.rooms.append(gare)
        train = Room("train", "désormais dans le train à destination de Poudlard dont les fenêtres offrent une vue sur la campagne anglaise qui défile. Choisissez à côté de qui vous souhaitez faire le trajet.")
        self.rooms.append(train)
        entree = Room("Entree", "dans l’entrée de Poudlard. Devant vous, les grandes portes s’élèvent, flanquées de gargouilles qui semblent vous observer. Une lueur dorée filtre à travers les vitraux, projetant des ombres mouvantes sur les dalles usées.")
        self.rooms.append(entree)
        couloir = Room("Couloir", "dans le couloir principal qui mène aux différentes pièces de l'école. Les murs de pierre froide sont ornés de portraits animés qui vous observent, murmurant entre eux.")
        self.rooms.append(couloir)
        bibliotheque = Room("Bibliotheque", "dans dans la majestueuse et imposante bibliothèque de Poudlard. Un silence oppressant règne, seulement rompu par le bruissement des pages tournées et le tictac d’une horloge ensorcelée qui tourne à l’envers.")
        self.rooms.append(bibliotheque)
        classe = Room("Classe", "dans la classe de défense contre les forces du mal du professeur Lupin. Une odeur étrange vous enveloppe : un mélange de parchemin ancien et de plantes séchées. Les étagères sont chargées de boîtes étiquetées “dangereux”, de fioles remplies de liquides troubles et de créatures empaillées qui semblent vous suivre du regard.")
        self.rooms.append(classe)
        banquet = Room("banquet", "dans la grande salle de réception. La Grande Salle est un spectacle à couper le souffle : un plafond ensorcelé reflète un ciel étoilé en mouvement, tandis que les quatre longues tables (Gryffondor, Serpentard, Poufsouffle, Serdaigle) sont garnies de plats fumants. Les bougies flottent au-dessus des têtes, projetant une lumière dorée sur les bannières aux couleurs des maisons.")
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

        # setup directions
        # Store allowed direction tokens on the game object so actions can check them
        self.directions = set(['N', 'NORD', 'Nord', 'nord', 'S', 'SUD', 'Sud', 'sud', 'E', 'EST', 'Est', 'est', 'O', 'OUEST', 'Ouest', 'ouest', 'M', 'MONTER', 'Monter', 'monter', 'D', 'DESCENDRE', 'Descendre', 'descendre'])



        # Create exits for rooms

        foret.exits = {"N" : chemin}
        gare.exits = {"E" : train}
        train.exits = {"E" : entree}
        entree.exits = {"N" : cabane, "E" : couloir, "S" : chemin}
        couloir.exits = {"N" : dortoirs, "E" :escalier, "S" : banquet, "O" : entree}
        escalier.exits = {"M" : palier, "O" : couloir}
        palier.exits = {"N" : classe, "S" : bibliotheque, "D" : escalier}
        cabane.exits = {"E" : dortoirs, "S" : couloir}
        chemin.exits = {"N" : entree, "S" : foret}
        dortoirs.exits = {"O" : cabane, "S" : couloir}
        classe.exits = {"S" : palier}
        bibliotheque.exits = {"N" : palier}
        banquet.exits = {"N" : couloir}

        #setup items in rooms
        
        lg = Item("Loups", "Plongez dans les secrets les plus sombres de la magie avec ce guide inédit sur les loups-garous. Découvrez l’histoire tragique de Remus Lupin, les rituels de transformation, et les liens mystérieux entre la lycanthropie et les forces obscures.", "2")
        bibliotheque.inventory["Loups"] = lg
        troll = Item("Fiche Magizoologique : Les Trolls", "Découvrez les trolls, ces géants maladroits mais redoutables, de la forêt interdite aux montagnes enneigées. Ce livre explore leurs différentes espèces, leur force colossale et les rares sorciers qui osent les affronter. A voir : types de Trolls, comportements, faiblesses et défenses, conseils de survie, anecdotes et faits marquants.", "2")
        bibliotheque.inventory["Fiche Magizoologique : Les Trolls" ]= troll
        acro = Item("Acromentules : Les Géants des Ténèbres", "Découvrez les secrets d’Aragog et de sa colonie, ces araignées géantes aux yeux brillants et au venin redouté. Entre légendes et réalité, ce livre explore leur intelligence, leur territoire et la peur qu’elles inspirent aux sorciers.", "2")
        bibliotheque.inventory["Acromentules : Les Géants des Ténèbres" ] = acro
        fantome = Item("Les Voiles de Poudlard : Fantômes et Mémoires Éternelles", "Découvrez les secrets des résidents spectrales de Poudlard : Nick-Quasi-Sans-Tête, le Baron Sanglant, la Dame Grise et bien d’autres. Ce livre lève le voile sur leur existence entre deux mondes, leurs regrets, leurs farces et leur rôle insoupçonné dans l’histoire de l’école.", "2")
        bibliotheque.inventory["Les Voiles de Poudlard : Fantômes et Mémoires Éternelles" ] = fantome
        sort = Item("Sortilèges & Incantations : L’Art Invisible de la Magie", "De « Lumos » à « Expecto Patronum », explorez les sortilèges qui façonnent le monde des sorciers. Ce guide révèle l’origine, la puissance et les dangers des formules les plus célèbres — et les moins connues — enseignées à Poudlard.", "2")
        bibliotheque.inventory["Sortilèges & Incantations : L’Art Invisible de la Magie" ] = sort
        potion = Item("Potions Magiques : Élixirs, Poisons et Remèdes de Poudlard", "Plongez dans les chaudrons fumants du cours de potions : du Polynectar au Felix Felicis, en passant par les mixtures les plus dangereuses. Ce livre révèle les ingrédients rares, les erreurs à éviter et les secrets de Severus Rogue.", "2")
        bibliotheque.inventory["Potions Magiques : Élixirs, Poisons et Remèdes de Poudlard" ] = potion


        
        echarpe = Item("Echarpe de Gryffondor", "Une écharpe aux couleurs rouge et or, symbole de courage et de bravoure.", "2")
        dortoirs.inventory["Echarpe de Gryffondor" ] = echarpe
        chapeau = Item("Chapeau de Sorcier", "Un chapeau pointu noir orné d'une bande argentée, parfait pour compléter votre tenue de sorcier.", "2")
        dortoirs.inventory["Chapeau de Sorcier" ] = chapeau
        journal = Item("Journal intime", "Un petit carnet à couverture en cuir qui ne semble pas à sa place ici.", "2")
        dortoirs.inventory["Journal intime" ]  = journal

        valise = Item("Valise", "Une valise en cuir usée, prête pour une aventure magique.", "2")
        gare.inventory["Valise" ] = valise




       
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = gare
        
        

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
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
