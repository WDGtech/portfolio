class Scanner:
    """Deze class vertegenwoordigt een scanner die stembiljetten controleert en registreert."""

    def __init__(self):
        """ Het initialiseert de scanner."""
        pass

    def controleer_stembiljet(self, stembiljet):
        """Dit controleert of het stembiljet geldig is."""
        if stembiljet.is_geldig():
            print("Stembiljet is geldig.")
            return True
        else:
            print("Ongeldig stembiljet. Controleer opnieuw.")
            return False

    def registreer_stembiljet(self, stembiljet):
        """Het registreert het stembiljet na controle."""
        if self.controleer_stembiljet(stembiljet):
            print("Stembiljet wordt geregistreerd.")
            return True
        else:
            print("Stembiljet kan niet worden geregistreerd omdat het ongeldig is.")
            return False
