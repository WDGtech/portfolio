import random

class Chipkaart:
    """deze class representeert een chipkaart die wordt gebruikt voor de identificatie bij het stemproces."""

    def __init__(self):
        """ de functie initialiseert een chipkaart met een unieke ID en status van de initialisatie."""
        self.id = f"ID-{random.randint(1000, 9999)}"
        self.geinitialiseerd = False

    def initialiseer(self):
        """ de functie markeert de chipkaart als geïnitialiseerd."""
        self.geinitialiseerd = True
        print(f"Chipkaart {self.id} is geïnitialiseerd.")

    def reset(self):
        """ de functie reset de chipkaart door een nieuwe ID te genereren en de initialisatiestatus te resetten."""
        self.id = f"ID-{random.randint(1000, 9999)}"
        self.geinitialiseerd = False

    def is_geinitialiseerd(self):
        """de functie controleert of de chipkaart is geïnitialiseerd."""
        return self.geinitialiseerd
