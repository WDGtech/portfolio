class Kandidaat:
    """deze class vertegenwoordigt een kandidaat voor de verkiezingen."""

    def __init__(self, voornaam, achternaam):
        """de functie initialiseert een kandidaat met de opgegeven voornaam en achternaam."""
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.stemmen_ontvangen = 0 

    def ontvang_stem(self):
        """de functie ontvangt een stem."""
        self.stemmen_ontvangen += 1

    def get_aantal_stemmen(self):
        """ de functie geeft het aantal ontvangen stemmen terug."""
        return self.stemmen_ontvangen

    def __str__(self):
        """de functie geeft de string van de kandidaat weer."""
        return f"{self.voornaam} {self.achternaam}"
