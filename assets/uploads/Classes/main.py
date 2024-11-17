from jinja2 import Environment, FileSystemLoader
from kiezer import Kiezer
from stemcomputer import Stemcomputer
from kandidaat import Kandidaat
from lijst import Lijst
from stembus import Stembus
from stembiljet import Stembiljet
from scanner import Scanner
from usbstick import USBStick
from kiezersregistratie import KiezersRegistratie
from lijstengenerator import genereer_lijsten_en_kandidaten
import random

voornamen = ["Cristiano", "Lionel", "Kevin", "Youri", "Arthur", "Romelu", "Kylian", "Dani", "Eden", "Arda"]
achternamen = ["Ronaldo", "Messi", "De Bruyne", "Tielemans", "Vermeeren", "Lukaku", "Mbappe", "Carvajal", "Hazard", "Guler"]

def genereer_willekeurige_kiezers(aantal):
    """ Dit zal genereren van een lijst van willekeurige kiezers met voor en achternamen en leeftijden."""
    kiezers = []
    for _ in range(aantal):
        voornaam = random.choice(voornamen)
        achternaam = random.choice(achternamen)
        leeftijd = random.randint(18, 90)  
        kiezers.append(Kiezer(voornaam, achternaam, leeftijd))
    return kiezers

def verdeel_zetels_dhondt(lijsten, totaal_zetels):
    """Verdeel zetels over de lijsten op basis van de D'Hondt-methode."""
    stemmen = {lijst.naam: lijst.get_totaal_stemmen() for lijst in lijsten}
    zetels = {lijst.naam: 0 for lijst in lijsten}

    print("Initiale zetelverdeling:", zetels)
    print("Stemmen per lijst:", stemmen)

    for _ in range(totaal_zetels):
        max_quotiënt = 0
        lijst_met_max_quotiënt = None

        for lijst in lijsten:
            quotiënt = stemmen[lijst.naam] / (zetels[lijst.naam] + 1)
            if quotiënt > max_quotiënt:
                max_quotiënt = quotiënt
                lijst_met_max_quotiënt = lijst.naam

        zetels[lijst_met_max_quotiënt] += 1

    return zetels


def sorteer_op_stemmen(kandidaat):
    """Het retourneert het aantal stemmen van een kandidaat."""
    return kandidaat.get_aantal_stemmen()

def ken_zetels_toe(lijst, aantal_zetels):
    """Het kent de zetels toe aan kandidaten binnen een lijst op basis van voorkeurstemmen."""
    kandidaten = lijst.kandidaten[:]
    kandidaten.sort(key=sorteer_op_stemmen, reverse=True)
    gekozen_kandidaten = []
    for i in range(aantal_zetels):
        gekozen_kandidaten.append(kandidaten[i])
    return gekozen_kandidaten

def genereer_html(lijsten, zetelverdeling, template_file, output_file):
    """Dit zal het html genereren met de verkiezingsuitslag."""
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_file)
    html_content = template.render(lijsten=lijsten, zetelverdeling=zetelverdeling)
    with open(output_file, 'w') as f:
        f.write(html_content)
    print(f"html bestand is succesvol gegenereerd: {output_file}") #als de code werkt dan komt dit op het einde in de terminal

def main():
    """ Hier gebeurt het hoofdproces, het gaat de simulatie van de verkiezingen met meerdere stemcomputers simuleren, de registratie van de kiezers en ook het verwerken van de stembiljetten """
    
    usb_stick = USBStick() 
    usb_stick.laad_opstartcodes("Opstartcode123") #Initialiseer de USB-stick met opstartcodes

    scanner = Scanner()
    stembus = Stembus(usb_stick)  #maakt een stembus aan en initialiseer het met de usb stick

    #hier maakt die drie stemcomputers aan en initialiseert het met de usb stick en scanner
    stemcomputers = [Stemcomputer(usb_stick, scanner, aantal_chipkaarten=20) for _ in range(3)]

    for stemcomputer in stemcomputers:
        stemcomputer.initialiseer_chipkaarten()

    kiezers_registratie = KiezersRegistratie()
    willekeurige_kiezers = genereer_willekeurige_kiezers(1200)  #Genereert 1200 willekeurige kiezers
    for kiezer in willekeurige_kiezers:
        kiezers_registratie.voeg_kiezer_toe(kiezer)

    lijsten = genereer_lijsten_en_kandidaten()

    for kiezer in kiezers_registratie.get_kiezers():
      
        stemcomputer = random.choice(stemcomputers)
        
        stembiljet = Stembiljet(kiezer)
        
        gekozen_lijst = random.choice(lijsten)
        gekozen_kandidaten = random.sample(gekozen_lijst.kandidaten, k=random.randint(1, 3))

        stemcomputer.stem_uitbrengen(kiezer, stembiljet, lijst=gekozen_lijst, voorkeursstemmen=gekozen_kandidaten)

        stembus.voeg_stembiljet_toe(stembiljet)
        
        for kandidaat in gekozen_kandidaten:
            kandidaat.ontvang_stem()

    stembus.verwerk_stembiljetten()

    totaal_zetels = 10  
    zetelverdeling = verdeel_zetels_dhondt(lijsten, totaal_zetels)

    #Dit zal de zetels toekennen aan de kandidaten binnen de lijsten
    for lijst in lijsten:
        gekozen_kandidaten = ken_zetels_toe(lijst, zetelverdeling[lijst.naam])
        print(f"Lijst {lijst.naam} heeft {zetelverdeling[lijst.naam]} zetels gekregen.")
        for kandidaat in gekozen_kandidaten:
            print(f"Kandidaat {kandidaat.voornaam} {kandidaat.achternaam} heeft een zetel gekregen.")

    genereer_html(lijsten, zetelverdeling, 'uitslag_template.html', 'uitslag.html')

if __name__ == "__main__":
    main()
