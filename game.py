# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

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
        va = Command("va", " <direction> : se déplacer dans une direction cardinale (N, E, S, O) ou monter (M) ou descendre (D)", Actions.va, 1)
        self.commands["va"] = va
        
        # Setup rooms

        foret = Room("Foret", "dans la Forêt Interdite, un lieu où même la lumière du jour semble hésiter à entrer. L’air est lourd, chargé d’une odeur de terre humide et de champignons. Vous entendez une brise légère qui murmure entre les feuilles des arbres, transportant des chuchotements incompréhensibles et des bruits étranges. Cet endroit vous donne la chair de poule, vous n’êtes pas serein.")
        self.rooms.append(foret)
        gare = Room("Gare", "à la gare king's Cross, entouré par le brouhaha des voyageurs pressés et les sifflements des trains à vapeur. Autour de vous, des familles moldues passent sans rien remarquer, tandis qu’un groupe d’élèves en robe noire rit en poussant des chariots chargés de coffres et de cages à hiboux.")
        self.rooms.append(gare)
        train = Room("train", "désormais dans le train à destination de Poudlard, les sièges en velours rouge sont usés par des décennies d’élèves, et les fenêtres offrent une vue sur la campagne anglaise qui défile. Choisissez à côté de qui vous souhaitez faire le trajet.")
        self.rooms.append(train)
        entree = Room("Entree", "dans l’entrée de Poudlard. Devant vous, les grandes portes en chêne de Poudlard s’élèvent, flanquées de statues de gargouilles qui semblent vous observer. Une lueur dorée filtre à travers les vitraux au-dessus de l’entrée, projetant des ombres mouvantes sur les dalles usées.")
        self.rooms.append(entree)
        couloir = Room("Couloir", "dans le couloir principal qui mène aux différentes pièces de l'école. Les murs de pierre froide du couloir principal semblent respirer l’histoire. Des portraits animés vous observent depuis leurs cadres dorés, chuchotant entre eux.")
        self.rooms.append(couloir)
        bibliotheque = Room("Bibliotheque", "dans dans la majestueuse et imposante bibliothèque de Poudlard. Un silence oppressant règne dans la bibliothèque de Poudlard, seulement rompu par le bruissement des pages tournées et le tictac d’une horloge ensorcelée qui tourne à l’envers. Les étagères, hautes comme des cathédrales, sont remplies de livres aux reliures en cuir usé.")
        self.rooms.append(bibliotheque)
        classe = Room("Classe", "dans la classe de défense contre les forces du mal du professeur Lupin. Une odeur étrange vous enveloppe : un mélange de parchemin ancien, de plantes séchées et d’une pointe de lune froide. Les murs, tapissés d’étagères en bois sombre, sont chargés de boîtes en métal étiquetées “dangereux”, de fioles remplies de liquides troubles et de créatures empaillées aux yeux de verre qui semblent vous suivre du regard.")
        self.rooms.append(classe)
        banquet = Room("banquet", "dans la grande salle de réception. La Grande Salle est un spectacle à couper le souffle : un plafond ensorcelé reflète un ciel étoilé en mouvement, tandis que les quatre longues tables (Gryffondor, Serpentard, Poufsouffle, Serdaigle) sont garnies de plats fumants apparus par magie. Les bougies flottent au-dessus des têtes, projetant une lumière dorée sur les bannières aux couleurs des maisons.")
        self.rooms.append(banquet)
        dortoirs = Room("Dortoirs", "dans les dortoirs des élèves. Cette grande salle circulaire a des murs de pierre ornés des blasons des quatre maisons, chacun brillant faiblement d’une lueur magique. Un tableau magique accroché au mur affiche les points des maisons, mis à jour en temps réel. Quatre portes massives, espacées régulièrement, mènent aux dortoirs respectifs. Entre elles, un grand feu crépite dans une cheminée centrale, autour duquel des élèves des différentes maisons se rassemblent parfois pour discuter… ou se lancer des défis.")
        self.rooms.append(dortoirs)
        cabane = Room("Cabane", "dans la cabane d'Hagrid. On y sent le thé fort, la fourrure mouillée et les citrouilles trop mûres. Le plancher en bois craque sous vos pieds, et un feu de cheminée rugit dans l’âtre, autour duquel ronronne un chat à trois pattes (ou est-ce un autre type de créature ?). Des ustensiles de jardinage géants sont accrochés aux murs, et une théière chante doucement une mélodie étrange.")
        self.rooms.append(cabane)
        chemin = Room("Chemin", "sur un chemin sombre à l’extérieur de Poudlard. Le chemin de pierre qui serpente à l’extérieur de Poudlard est éclairé seulement par la lueur tremblante de la lune, filtrée à travers les nuages. Les arbres bordant le sentier semblent se pencher vers vous, leurs branches formant des arches menaçantes.")
        self.rooms.append(chemin)
        escalier = Room("Escalier", "dans l’escalier qui relie le couloir au palier de l’étage. Les marches de pierre usée de l’escalier sont éclairées par des torches dont les flammes dansent comme si elles étaient vivantes. Certaines marches disparaissent quand vous posez le pied dessus, vous forçant à sauter pour éviter de tomber. Des portraits accrochés aux murs vous suivent des yeux, et un écho de rires résonne, comme si des élèves invisibles couraient à côté de vous.")
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
