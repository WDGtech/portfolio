from chipkaart import Chipkaart

class Stemcomputer:
    """Klasse is verantwoordelijk voor het beheren van het stemproces en het registreren van stemmen en het berekenen van de resultaten."""

    def __init__(self, usb_stick, scanner, aantal_chipkaarten):
        """Het initialiseert de stemcomputer met de gegeven usb stick, scanner en het aantal chipkaarten."""
        self.usb_stick = usb_stick
        self.scanner = scanner
        self.chipkaarten = [Chipkaart() for _ in range(aantal_chipkaarten)]
        self.gestemde_kiezers = []

    def initialiseer_chipkaarten(self):
        """Dit initialiseert alle chipkaarten."""
        for chipkaart in self.chipkaarten:
            chipkaart.initialiseer()

    def controleer_chipkaart(self, chipkaart):
        """Controleert of de chipkaart geïnitialiseerd is."""
        return chipkaart.is_geinitialiseerd()

    def reset_chipkaarten(self):
        """Zal alle chipkaarten resetten."""
        for chipkaart in self.chipkaarten:
            chipkaart.reset()

    def stem_uitbrengen(self, kiezer, stembiljet, lijst=None, voorkeursstemmen=None):
        """Laat de kiezer stemmen en maakt een stembiljet aan."""
        if kiezer in self.gestemde_kiezers:
            print(f"Kiezer {kiezer.voornaam} {kiezer.achternaam} heeft al gestemd en kan niet opnieuw stemmen.")
            return

        if self.usb_stick.geautoriseerd(kiezer.chipkaart):
            if self.controleer_chipkaart(kiezer.chipkaart):
                print(f"Kiezer {kiezer.voornaam} {kiezer.achternaam} is geautoriseerd om te stemmen.")
                if lijst:
                    stembiljet.voeg_lijststem_toe(lijst)
                if voorkeursstemmen:
                    for kandidaat in voorkeursstemmen:
                        stembiljet.voeg_voorkeurstem_toe(kandidaat)
                self.gestemde_kiezers.append(kiezer)
                kiezer.heeft_gestemd = True
                stembiljet.maak_stembiljet()
                self.usb_stick.reset()
                kiezer.chipkaart.reset()
            else:
                print(f"USB stick autorisatie status voor chipkaart {kiezer.chipkaart.id}: {self.usb_stick.geautoriseerd(kiezer.chipkaart)}")
        else:
            print("Kiezer is niet geautoriseerd om te stemmen.")