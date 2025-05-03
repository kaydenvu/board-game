import pygame

MA = pygame.image.load("property cards/Mediterranean Avenue.png")
BA = pygame.image.load("property cards/Baltic Avenue.png")
CA = pygame.image.load("property cards/Connecticut Avenue.png")
NYA = pygame.image.load("property cards/New York Avenue.png")
OA = pygame.image.load("property cards/Oriental Avenue.png")
SC = pygame.image.load("property cards/St Charles Place.png")
JP = pygame.image.load("property cards/St James Place.png")
SA = pygame.image.load("property cards/States Avenue.png")
TA = pygame.image.load("property cards/Tennessee Avenue.png")
VA = pygame.image.load("property cards/Vermont Avenue.png")
VirA = pygame.image.load('property cards/Virginia Avenue.png')

scale = pygame.transform.scale_by
scaleFactor = 0.3

MA = scale(MA, scaleFactor)
BA = scale(BA, scaleFactor)
CA = scale(CA, scaleFactor)
NYA = scale(NYA, scaleFactor)
OA = scale(OA, scaleFactor)
SC = scale(SC, scaleFactor)
JP = scale(JP, scaleFactor)
SA = scale(SA, scaleFactor)
TA = scale(TA, scaleFactor)
VA = scale(VA, scaleFactor)
VirA = scale(VirA, scaleFactor)

class Property():
  def __init__(self, name, siteColor, rent, house, house2, house3, house4, hotel, mortgage, cost, image=None):
    self.name=name
    self.siteColor=siteColor
    self.rent=[rent,rent*2,house,house2,house3,house4,hotel]
    self.mortgage = mortgage
    self.costHouse=cost
    self.upgrades = 0
    self.image = image

MedAve = Property('Mediterranean Avenue', "Brown", 2, 10, 30, 90, 160, 250, 30,50, MA)
BalAve = Property('Baltic Avenue',"Brown", 4, 20, 60, 180, 320, 450, 30, 50, BA)
ReadRail = Property("Reading Railroad", "Black", 25, 0, 0, 0, 0, 0, 100, 0)
OrAve = Property('Oriental Avenue', "Light Blue", 6, 30, 90, 270, 400, 550, 50, 50, OA)
VerAve = Property('Vermont Avenue', "Light Blue", 6, 30, 90, 270, 400, 550, 50, 50, VA)
ConAve = Property( 'Connecticut Avenue', "Light Blue", 8, 40, 100, 300, 450, 600,60, 50, CA)
StChar = Property('St. Charles Place', "Pink",10, 50, 150, 450, 625, 750,70, 100, SC)
EleComp = Property("Electric Company", "Utility", 0, 0, 0,0, 0,0,75,0)
StaAve = Property( 'States Avenue', "Pink", 10, 50, 150, 450, 625, 750, 70, 100, SA)
VirAve = Property('Virginia Avenue', "Pink", 12, 60, 180, 500, 700, 900, 80, 100, VirA)
PennRail = Property("Pennsylvania Railroad", "Black", 25, 0,0,0,0,0,100,0)
StJames = Property('St. James Place', "Orange", 14, 70, 200, 550, 750, 950, 90, 100,JP)
TenAve = Property('Tennessee Avenue', "Orange", 14, 70, 200, 550, 750, 950, 90, 100, TA)
NewAve = Property('New York Avenue', "Orange" ,16, 80, 220, 600, 800, 1000, 100, 100,NYA)
KenAve = Property('Kentucky Avenue', "Red", 18, 90, 250, 700, 875,	1050, 110, 150)
IndAve = Property('Indiana Avenue', "Red", 18,90, 250, 700, 875, 1050, 110, 150)
IllAve = Property('Illinois Avenue',"Red", 20,  100, 300, 750, 925, 1100, 120,150)
BNORail = Property("B. & O. Railroad", "Black", 25, 0, 0, 0, 0, 0, 100, 0)
AtlAve = Property('Atlantic Avenue',"Yellow", 22,  110, 330, 800, 975, 1150, 130,150)
VenAve = Property('Ventnor Avenue', "Yellow", 22, 110, 330, 800, 975, 1150, 130, 150)
WaterWorks = Property("Water Works", "Utility", 0, 0, 0,0, 0,0,75,0)
MarGar = Property('Marvin Gardens', "Yellow", 24, 120, 360, 850, 1025, 1200, 140, 150)
PacAve = Property('Pacific Avenue', "Green", 26, 130, 390, 900, 1100, 1275,150, 200)
NorAve = Property('North Carolina Avenue', "Green", 26, 130, 390, 900, 1100, 1275, 150, 200)
ShortLine = Property("Short Line", "Black", 25, 0, 0, 0, 0, 0, 100, 0)
PenAve = Property('Pennsylvania Avenue', "Green", 28, 150, 450, 1000, 1200, 1400, 160, 200)
ParkPlace = Property('Park Place', "Dark Blue", 35, 175, 500, 1100, 1300, 1500, 175, 200)
Boardwalk = Property('Boardwalk',"Dark Blue", 50, 200, 600, 1400, 1700, 2000, 200, 200)

properties = [MedAve, BalAve, ReadRail, OrAve, VerAve, ConAve, StChar, EleComp, StaAve, VirAve, PennRail, StJames, 
              TenAve, NewAve, KenAve, IndAve, IllAve, BNORail, AtlAve, VenAve, WaterWorks, MarGar, PacAve, 
              NorAve, ShortLine, PenAve, ParkPlace, Boardwalk]