class Stembus:
    """Deze class vertegenwoordigt een stembus die stembiljetten bevat."""

    def __init__(self, usb_stick):
        """Initialiseert de stembus met een USB-stick om de stemmen te verwerken."""
        self.inhoud = []
        self.usb_stick = usb_stick

    def voeg_stembiljet_toe(self, stembiljet):
        """Voegt een stembiljet toe aan de stembus."""
        self.inhoud.append(stembiljet)

    def verwerk_stembiljetten(self):
        """Verwerkt alle stembiljetten in de stembus."""
        for stembiljet in self.inhoud:
            self.usb_stick.sla_stemmen_op(stembiljet)

    def get_stembiljetten(self):
        """Geeft een lijst van alle stembiljetten in de stembus terug."""
        return self.inhoud
