import random

class Kiessysteem:
    """deze class verkoepelende zorgt voor het beheer van het stemproces."""

    def __init__(self, stembus, stemcomputers):
        """ het initialiseert het kiessysteem met de stembus en stemcomputers."""
        self.stembus = stembus
        self.stemcomputers = stemcomputers

    def stem_proces(self, kiezers):
        """ Dit simuleert het stemproces voor de gegeven lijst van kiezers."""
        for kiezer in kiezers:
            stemcomputer = random.choice(self.stemcomputers)
            stemcomputer.stemmen(kiezer, self.stembus)

    def toon_stembus_inhoud(self):
        """ Het toont de inhoud van de stembus."""
        print("Inhoud van de stembus:")
        for stembiljet in self.stembus.inhoud:
            print(stembiljet)

    def ken_zetels_toe(self, lijst, aantal_zetels):
        """Kent zetels toe aan de kandidaten op de lijst op basis van het aantal voorkeurstemmen."""
        kandidaten = sorted(lijst.kandidaten, key=self._sorteer_op_stemmen, reverse=True)
        gekozen_kandidaten = kandidaten[:aantal_zetels]
        return gekozen_kandidaten

    def _sorteer_op_stemmen(self, kandidaat):
        """Hulpfunctie om kandidaten te sorteren op basis van het aantal stemmen."""
        return kandidaat.get_aantal_stemmen()
