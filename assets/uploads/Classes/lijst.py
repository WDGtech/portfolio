class Lijst:
    """Deze class vertegenwoordigt een lijst van kandidaten voor de verkiezingen."""

    def __init__(self, naam):
        """We maken een lege lijst aan"""
        self.naam = naam
        self.kandidaten = []

    def voeg_kandidaat_toe(self, kandidaat):
        """Hier voegen we een kandidaat toe aan de lege lijst."""
        self.kandidaten.append(kandidaat)

    def krijg_kandidaten(self):
        """Dit functie geeft een lijst terug van alle kandidaten op deze lijst."""
        return self.kandidaten

    def get_totaal_stemmen(self):
        """En dit geeft het totale aantal stemmen voor deze lijst terug."""
        return sum(kandidaat.get_aantal_stemmen() for kandidaat in self.kandidaten)

    def __str__(self):
        """Dit retourneert dan de resultaten terug"""
        return f"Lijst '{self.naam}' met {len(self.kandidaten)} kandidaten"
