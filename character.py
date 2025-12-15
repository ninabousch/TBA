class Character :

    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = None
        self.msgs = msgs
        self.msgs_init = msgs.copy()  # Copie pour réinitialiser plus tard

    def __str__(self) :
        """ Return the string representation of the character. """
        return f"{self.name} : {self.description}"
    
    def get_msg(self):
        """ Return the messages of the character. """
        if not self.msgs:  # Si la liste est vide
            self.msgs = self.msgs_init.copy()  # On réinitialise la liste
        return self.msgs.pop(0)  # On retourne et supprime le premier message
        

       