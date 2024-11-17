import random
from kiezer import Kiezer

class KiezersRegistratie:
    """Dez class beheert de registratie van kiezers voor de verkiezingen."""

    def __init__(self):
        """Het initialiseert een lege lijst voor de kiezers."""
        self.kiezers = []

    def genereer_kiezers(self, aantal_kiezers):
        """Het zal het opgegeven aantal kiezers met willekeurige namen en leeftijden genereren."""
        for _ in range(aantal_kiezers):
            voornaam = f"Kiezer{random.randint(1, 1200)}"
            achternaam = f"Kiezer{random.randint(1, 1200)}"
            leeftijd = random.randint(18, 90) #dus hier gaat die dan kiezen tussen de leeftijden 18 en 90 zoals gevraagd en hierboven die 1200 genereren
            kiezer = Kiezer(voornaam, achternaam, leeftijd)
            self.kiezers.append(kiezer)

    def voeg_kiezer_toe(self, kiezer):
        """Dit functie voegt een kiezer toe aan de registratie."""
        self.kiezers.append(kiezer)

    def get_aantal_kiezers(self):
        """Het geeft het aantal geregistreerde kiezers terug, dit doen we met de len."""
        return len(self.kiezers)

    def get_kiezers(self):
        """het geeft een lijst van alle geregistreerde kiezers terug."""
        return self.kiezers
