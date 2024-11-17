class USBStick:
    """Deze class vertegenwoordigt een USB-stick die gebruikt wordt om stemmen op te slaan."""

    def __init__(self):
        """Initialiseert de USB-stick."""
        self.stemmen = []
        self.opstartcode = None

    def laad_opstartcodes(self, code):
        """Laadt de opstartcodes op de USB-stick."""
        self.opstartcode = code
        print(f"Opstartcodes geladen: {self.opstartcode}")

    def sla_stemmen_op(self, stembiljet):
        """Slaat de stemmen van een stembiljet op."""
        if self.opstartcode is not None:
            self.stemmen.append(stembiljet)
            print("Stemmen opgeslagen op USB-stick.")
        else:
            print("Geen opstartcodes gevonden. Kan stemmen niet opslaan.")

    def geautoriseerd(self, chipkaart):
        """Controleert of de gegeven chipkaart geautoriseerd is om de USB-stick te gebruiken."""
        return self.opstartcode is not None and chipkaart.is_geinitialiseerd()
