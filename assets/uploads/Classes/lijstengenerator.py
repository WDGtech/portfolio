from lijst import Lijst
from kandidaat import Kandidaat
import random

voornamen = ["Cristiano", "Lionel", "Kevin", "Youri", "Arthur", "Romelu", "Kylian", "Dani", "Eden", "Arda"]
achternamen = ["Ronaldo", "Messi", "De Bruyne", "Tielemans", "Vermeeren", "Lukaku", "Mbappe", "Carvajal", "Hazard", "Guler"]

def genereer_lijsten_en_kandidaten():
    """Dit zal lijsten met kandidaten genereren voor het stemproces."""
    lijsten = []
    for i in range(5):
        lijst = Lijst(f"Lijst {i + 1}")
        for j in range(10):
            voornaam = random.choice(voornamen)
            achternaam = random.choice(achternamen)
            kandidaat = Kandidaat(voornaam, achternaam)
            lijst.voeg_kandidaat_toe(kandidaat)
        lijsten.append(lijst)
    return lijsten


# Deze class stuk code kon ik in de class lijst invoegen door een static methoden te gebruiken, zoals bij les 8.
# Ik vond het overzichtelijker om het apart te coderen tijdens het debuggen.

