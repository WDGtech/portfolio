from chipkaart import Chipkaart

class Kiezer:
    """ Deze class vertegenwoordigt een persoon die stemt en mag slechts 1 keer stemmen en kan zich ook kandidaat stellen."""

    def __init__(self, voornaam, achternaam, leeftijd, is_kandidaat=False):
        """ Het initialiseert een kiezer met de opgegeven voornaam, achternaam en leeftijd."""
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.leeftijd = leeftijd
        self.heeft_gestemd = False
        self.is_kandidaat = is_kandidaat
        self.stemmen_ontvangen = 0 if is_kandidaat else None  # Houdt het aantal ontvangen stemmen bij als kiezer een kandidaat is
        self.chipkaart = Chipkaart()  #Elke kiezer krijgt een unieke chipkaart

    def stemmen(self):
        """De functie laat de kiezer stemmen."""
        if not self.heeft_gestemd:
            print(f"{self.voornaam} {self.achternaam} heeft gestemd.")
            self.heeft_gestemd = True
        else:
            print(f"{self.voornaam} {self.achternaam} heeft al gestemd en kan niet opnieuw stemmen.")

    def ontvang_stem(self):
        """ Deze functie zal een stem ontvangen als de kiezer een kandidaat is."""
        if self.is_kandidaat:
            self.stemmen_ontvangen += 1

    def get_aantal_stemmen(self):
        """Het zal het aantal ontvangen stemmen terugeven als de kiezer een kandidaat is."""
        return self.stemmen_ontvangen if self.is_kandidaat else None

    def __str__(self):
        """ Dit retourneert een string van de kiezer terug."""
        return f"{self.voornaam} {self.achternaam}, Leeftijd: {self.leeftijd}"
