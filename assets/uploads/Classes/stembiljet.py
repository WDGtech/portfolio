class Stembiljet:
    """De class vertegenwoordigt een stembiljet met de keuzes van een kiezer."""

    def __init__(self, kiezer):
        """Het initialiseert een stembiljet met de opgegeven kiezer."""
        self.kiezer = kiezer
        self.lijststem = None
        self.voorkeurstemmen = []

    def voeg_lijststem_toe(self, lijst):
        """Dit voegt een lijststem toe aan het stembiljet."""
        self.lijststem = lijst

    def voeg_voorkeurstem_toe(self, kandidaat):
        """Voegt een voorkeurstem toe aan het stembiljet."""
        self.voorkeurstemmen.append(kandidaat)

    def maak_stembiljet(self):
        """Maakt het stembiljet aan."""
        print(f"Stembiljet voor kiezer {self.kiezer.voornaam} {self.kiezer.achternaam} is aangemaakt:")
        if self.lijststem:
            print(f"Lijststem: {self.lijststem.naam}")
        if self.voorkeurstemmen:
            print("Voorkeurstemmen:")
            for i, kandidaat in enumerate(self.voorkeurstemmen, start=1):
                print(f"{i}. {kandidaat.voornaam} {kandidaat.achternaam}")

    def is_geldig(self):
        """Controleert of het stembiljet geldig is."""
        return self.lijststem is not None or bool(self.voorkeurstemmen)  # Een stembiljet is geldig als er minimaal een lijststem of een voorkeurstem is

    def __str__(self):
        """Geeft de stringrepresentatie van het stembiljet weer."""
        lijststem_naam = self.lijststem.naam if self.lijststem else "Geen lijststem"
        voorkeurstemmen_namen = [f"{kandidaat.voornaam} {kandidaat.achternaam}" for kandidaat in self.voorkeurstemmen]
        return f"Stembiljet van {self.kiezer.voornaam} {self.kiezer.achternaam}:\nLijststem: {lijststem_naam}\nVoorkeurstemmen: {', '.join(voorkeurstemmen_namen)}"
