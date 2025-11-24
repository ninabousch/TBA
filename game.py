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
        self.directions={}
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        va = Command("va", " <direction> : se déplacer dans une direction cardinale (N, E, S, O) ou monter (M) ou descendre (D)", Actions.go, 1)
        self.commands["va"] = va
        
        # Setup rooms

        foret = Room("Foret", "dans la forêt interdite. Vous entendez une brise légère qui fait bouger les feuilles des arbres. Cet endroit vous donne la chair de poule, vous n’êtes pas serein.")
        self.rooms.append(foret)
        gare = Room("Gare", "A la gare king's Cross.")
        self.rooms.append(gare)
        train = Room("train", "désormais dans le train à destination de poudlard, choisissez à côté de qui vous souhaitez faire le trajet.")
        self.rooms.append(train)
        entree = Room("Entree", "dans l’entrée de Poudlard.")
        self.rooms.append(entree)
        couloir = Room("Couloir", "dans le couloir principal qui mène aux différentes pièces de l'école.")
        self.rooms.append(couloir)
        bibliotheque = Room("Bibliotheque", "dans dans la majestueuse et imposante bibliothèque de Poudlard .")
        self.rooms.append(bibliotheque)
        classe = Room("Classe", "dans la classe de défense contre les forces du mal du professeur Lupin.")
        self.rooms.append(classe)
        banquet = Room("banquet", "dans la grande salle de réception.")
        self.rooms.append(banquet)
        dortoirs = Room("Dortoirs", "dans les dortoirs des élèves.")
        self.rooms.append(dortoirs)
        cabane = Room("Cabane", "dans la cabane d'Hagrid.")
        self.rooms.append(cabane)
        chemin = Room("Chemin", "sur un chemin sombre à l’extérieur de Poudlard.")
        self.rooms.append(cabane)
        escalier = Room("Escalier", "dans l’escalier qui relie le couloir au palier de l’étage.")
        self.rooms.append(escalier)
        palier = Room("Palier", "sur le palier à l’étage. Il y a deux portes.")
        self.rooms.append(palier)

        # setup directions

        directions = set(['N','NORD','Nord', 'nord', 'S', 'SUD', 'Sud', 'sud', 'E', 'EST', 'Est', 'est',  'O', 'OUEST', 'Ouest', 'ouest', 'M', 'MONTER', 'Monter', 'monter', 'D', 'DESCENDRE', 'Descendre', 'descendre'])



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
