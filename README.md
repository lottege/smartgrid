# smartgrid

Smartgrid is een project waarbij groene energie wordt geproduceerd door huizen, maar er is sprake van overproductie van groene energie. Deze overproductie kan worden opgeslagen in batterijen. Er zijn drie dummywijken, met elk vijf batterijen. 

# The assignment
Het doel van dit project is het verbinden van de huizen met de batterijen op de meest optimale manier. De meest optimale manier moet wel de minste kosten hebben. De opdracht bestaat uit 4 delen: 

a)  Verbind alle huizen in de drie wijken aan een batterij. De maximumcapaciteit van de huizen mag die van de batterijen uiteraard niet overschrijden. 

De batterijen kosten 5000 per stuk. De kabels kosten 9 per grid-segment. De kabels liggen op de gridlijnen, mogen ook gridpunten met een huis passeren, en de afstand van een huis tot een batterij wordt berekend volgens de manhattan distance. 

b) Bereken de kosten voor de in a) geconfigureerde wijk. Probeer je grid te optimaliseren en vind een zo goed mogelijke configuratie van kabels.

Nu is het zo, dat de batterijen misschien niet op de best mogelijke plaatsen staan. Het verplaatsen van batterijen vercompliceert de zaak enorm, maar de opdrachtgever wil het toch proberen, om inzicht in het probleem te krijgen. 

c) Relocate the batteries and try to realise a better result. 

Verplaats de batterijen, en probeer een beter resultaat te realiseren.

Het bedrijf SmartBatteryCompany heeft recentelijk drie types batterijen ontwikkeld, met verschillende capaciteiten en verschillende prijzen. 

| Batterytype  | Capaciteit | Prijs |
| -----------  | :--------: | :---: |
| PowerStar 	 |    450 	  |  900  |
| Imerse-II 	 |    900 	  | 1350  |
| Imerse-III 	 |   1800 	  | 1800  |

T Probeer een betere configuratie voor de wijk te vinden met deze batterijen, je mag er zoveel gebruiken als je wil en kunnen op ieder gridpunt zonder huis geplaatst worden. 

d) Optimaliseer het smartGrid voor de drie wijken. 

# Installation
Het project kan worden verkregen door de code the kopiëren in de files en de benodigde packages te installeren. 

## Prerequisites
De packages die in dit project gebruikt worden zijn:

- mathplotlib.pyplot, is een library welke figuren produceert in verschillende formats. Het helpt bij de representatie van de manier waarop de huizen met de batterijen verbonden zijn, door het weer te geven in een plot. Om matplotlib.pyplot te installeren, typ je het volgende in de terminal:

   - python -mpip install -U pip
   - python -mpip install -U matplotlib
   
- cycler
- numpy
- pyparsing
- pytz
- six
- python-dateutil


# Algorithms
De volgende algoritmes worden gebruikt om de meest optimale oplossing te vinden:
- Door het plaatsen van kabels op de grid:

   - Cable list
   - Cable list sneller en korter
   - Verre huizen eerst
   - Buiten naar binnen
   - Hillclimber nieuw
   
- Door het verplaatsen van de batterijen en toevoegen van batterijen:

   - Batterijen plaatsen met random start
   - Batterijen plaatsen mbv hillclimber
   - Batterijen plaatsen met combinatie van random restart en hillclimber
   - Batterij allerlei
   
## cable_list.py
Cable list verbindt huizen met batterijen. Hierbij wordt er bij het eerste huis in de lijst begonnen, dit huis wordt verbonden met de eerste batterij uit de lijst. De huizen en batterijen staan op dezelfde volgorde in de lijst als dat ze worden aangeleverd. De lijst met huizen wordt afgewerkt, wanneer de batterij zijn volledige capaciteit heeft bereikt, wordt er overgestapt naar de volgende batterij in de lijst.

## cable_list_sneller_korter.py
Dit is een code die de huizen met de batterijen verbindt op een effectievere manier. Met de functie distance_sort wordt de afstand tussen de batterijen en de huizen berekend. Vervolgens wordt per batterij gekeken welk huis de kortste afstand heeft tot de betreffende batterij. Het huis dat het dichtste bij de batterij staat wordt verbonden, hierna het huis met de een na kleinste afstand tot de batterij enz enz. 

## verre_huizen_eerst.py
De afstand van de batterijen tot de huizen wordt berekend, en vervolgens wordt er begonnen bij het huis wiens kortste afstand tot de batterij het grootste is. Het beginnen met deze grootste afstanden zou voordelig zijn omdat deze een groter verschil kunnen maken.

## buiten_naar_binnen.py
In dit algoritme is de aanpak als volgt: de huizen die het verste weg staan van het middelpunt van de wijk, verbinden we als eerst met de dichtstbijzijnde batterij. Net zoals bij het verre_huizen_eerst.py algoritme zou dit voordeliger zijn omdat deze verre huizen het grootste verschil kunnen maken.  

## hillclimber_nieuw.py
Dit algoritme zorgt ervoor dat er op een optimale manier kabels worden gelegd met behulp van een hillclimber. Er wordt gehillclimbed door vanuit een standaardsetup, van huizen gelinkt aan batterijen, random twee huizen van batterij te switchen en te kijken of dat een betere score oplevert. Het totaal aantal scoreberekeningen kan worden gemanipuleerd. Onderin het bestand worden de kabels voor de beste huis-batterij combinatie gelegd. 

## hillclimber_nieuw_reserve.py
Dit algoritme zorgt ervoor dat er op een optimale manier kabels worden gelegd. Het is een combinatie van een random restart en een hillclimber. Op deze manier wordt de random restart geoptimaliseerd door er een hillclimber op toe te passen. Er wordt gehillclimbed door vanuit een random standaardsetup, van huizen gelinkt aan batterijen, random twee huizen van batterij te switchen en te kijken of dat een betere score oplevert. Er kan worden gemanipuleerd hoe vaak er een random restart wordt toegepast en het totaal aantal scoreberekeningen kan worden gemanipuleerd. Onderin het bestand worden de kabels voor de beste huis-batterij combinatie gelegd. 

## batterij_plaatsen.py
Met dit algoritme worden de batterijen random in de wijk geplaatst. Dit wordt een aantal keer uitgevoerd en de beste optie wordt opgeslagen. 

## batterijen_plaatsen_hillclimber.py
Hierbij worden de batterijen willekeurig in de wijk gezet. Vervolgens wordt er de hillclimber op toegepast en wordt de plaats van de batterijen geoptimaliseerd. Dit algoritme gebruiken we ook om een combinatie van “random restart” en de hillclimber te testen. 

## batterij_allerlei.py
In batterij_allerlei.py worden meerdere batterijen in de wijk geplaatst. Hierbij gaan we niet meer uit van de standaard batterij maar worden negen exemplaren “PowerStar” in de wijk geplaatst. Dit gebeurt met “random restart”, de beste optie wordt onthouden en is het eindresultaat.

## brute_force_batterijen.py
In deze code worden de batterijen op elke plek van het grid geplaatst en de scores worden met elkaar vergeleken. Dit leidt tot een aantal mogelijkheden van 2500 ^ 5. Om de run-tijd te verkleinen berekenen we de score eerst zonder kabel  objecten aan te maken maar door de afstand te berekenen tussen een batterij en het bijbehorende huis. Pas als de score lager is dan een eerder behaalde score worden de kabel objecten aangemaakt. Pas wanneer er een kabel lijst is die korter is dan de bestaande kabel lijst, wordt deze kabel lijst overschreven.

 
  
  
 
   

   
  
   
  
 
 
  
