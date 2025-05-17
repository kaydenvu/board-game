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
AA = pygame.image.load("property cards/Atlantic Avenue.png")
BNO = pygame.image.load("property cards/B. & O. Railroad.png")
B = pygame.image.load("property cards/Boardwalk.png")
EC = pygame.image.load("property cards/Electric Company.png")
IL = pygame.image.load("property cards/Illinois Avenue.png")
IA = pygame.image.load("property cards/Indiana Avenue.png")
KA = pygame.image.load("property cards/Kentucky Avenue.png")
MG = pygame.image.load("property cards/Marvin Gardens.png")
NC = pygame.image.load("property cards/North Carolina Avenue.png")
PA = pygame.image.load("property cards/Pacific Avenue.png")
PP = pygame.image.load("property cards/Park Place.png")
Penn = pygame.image.load("property cards/Pennsylvania Avenue.png")
PR = pygame.image.load("property cards/Pennsylvania Railroad.png")
RR = pygame.image.load("property cards/Reading Railroad.png")
SL = pygame.image.load("property cards/Short Line.png")
VET = pygame.image.load("property cards/Ventnor Avenue.png")
WW = pygame.image.load("property cards/Water Works.png")

scale = pygame.transform.scale_by
scaleFactor = 0.4

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
AA = scale(AA, scaleFactor)
BNO = scale(BNO, scaleFactor)
B = scale(B, scaleFactor)
EC = scale(EC, scaleFactor)
IL = scale(IL, scaleFactor)
IA = scale(IA, scaleFactor)
KA = scale(KA, scaleFactor)
MG = scale(MG, scaleFactor)
NC = scale(NC, scaleFactor)
PA = scale(PA, scaleFactor)
PP = scale(PP, scaleFactor)
Penn = scale(Penn, scaleFactor)
PR = scale(PR, scaleFactor)
RR = scale(RR, scaleFactor)
SL = scale(SL, scaleFactor)
VET = scale(VET, scaleFactor)
WW = scale(WW, scaleFactor)

class Property():
  def __init__(self, name, siteColor, rent, house, house2, house3, house4, hotel, mortgage, cost, image=None):
    self.name=name
    self.owner=None
    self.siteColor=siteColor
    self.rent=[rent,rent*2,house,house2,house3,house4,hotel]
    self.mortgage = mortgage
    self.costHouse=cost
    self.upgrades = 0
    if self.siteColor == "Utility":
      self.rent = [4, 10]
    self.image = image

MedAve = Property('Mediterranean Avenue', "Brown", 2, 10, 30, 90, 160, 250, 30,50, MA)
BalAve = Property('Baltic Avenue',"Brown", 4, 20, 60, 180, 320, 450, 30, 50, BA)
ReadRail = Property("Reading Railroad", "Black", 25, 0, 0, 0, 0, 0, 100, 0,RR)
OrAve = Property('Oriental Avenue', "Light Blue", 6, 30, 90, 270, 400, 550, 50, 50, OA)
VerAve = Property('Vermont Avenue', "Light Blue", 6, 30, 90, 270, 400, 550, 50, 50, VA)
ConAve = Property( 'Connecticut Avenue', "Light Blue", 8, 40, 100, 300, 450, 600,60, 50, CA)
StChar = Property('St. Charles Place', "Pink",10, 50, 150, 450, 625, 750,70, 100, SC)
EleComp = Property("Electric Company", "Utility", 0, 0, 0,0, 0,0,75,0,EC)
StaAve = Property( 'States Avenue', "Pink", 10, 50, 150, 450, 625, 750, 70, 100, SA)
VirAve = Property('Virginia Avenue', "Pink", 12, 60, 180, 500, 700, 900, 80, 100, VirA)
PennRail = Property("Pennsylvania Railroad", "Black", 25, 0,0,0,0,0,100, 0, PR)
StJames = Property('St. James Place', "Orange", 14, 70, 200, 550, 750, 950, 90, 100,JP)
TenAve = Property('Tennessee Avenue', "Orange", 14, 70, 200, 550, 750, 950, 90, 100, TA)
NewAve = Property('New York Avenue', "Orange" ,16, 80, 220, 600, 800, 1000, 100, 100,NYA)
KenAve = Property('Kentucky Avenue', "Red", 18, 90, 250, 700, 875,	1050, 110, 150,KA)
IndAve = Property('Indiana Avenue', "Red", 18,90, 250, 700, 875, 1050, 110, 150,IA)
IllAve = Property('Illinois Avenue',"Red", 20,  100, 300, 750, 925, 1100, 120,150,IL)
BNORail = Property("B. & O. Railroad", "Black", 25, 0, 0, 0, 0, 0, 100, 0,BNO)
AtlAve = Property('Atlantic Avenue',"Yellow", 22,  110, 330, 800, 975, 1150, 130,150,AA)
VenAve = Property('Ventnor Avenue', "Yellow", 22, 110, 330, 800, 975, 1150, 130, 150,VET)
WaterWorks = Property("Water Works", "Utility", 0, 0, 0,0, 0,0,75,0, WW)
MarGar = Property('Marvin Gardens', "Yellow", 24, 120, 360, 850, 1025, 1200, 140, 150,MG)
PacAve = Property('Pacific Avenue', "Green", 26, 130, 390, 900, 1100, 1275,150, 200,PA)
NorAve = Property('North Carolina Avenue', "Green", 26, 130, 390, 900, 1100, 1275, 150, 200,NC)
ShortLine = Property("Short Line", "Black", 25, 0, 0, 0, 0, 0, 100, 0,SL)
PenAve = Property('Pennsylvania Avenue', "Green", 28, 150, 450, 1000, 1200, 1400, 160, 200,Penn)
ParkPlace = Property('Park Place', "Dark Blue", 35, 175, 500, 1100, 1300, 1500, 175, 200,PP)
Boardwalk = Property('Boardwalk',"Dark Blue", 50, 200, 600, 1400, 1700, 2000, 200, 200,B)

properties = [MedAve, BalAve, ReadRail, OrAve, VerAve, ConAve, StChar, EleComp, StaAve, VirAve, PennRail, StJames, 
              TenAve, NewAve, KenAve, IndAve, IllAve, BNORail, AtlAve, VenAve, WaterWorks, MarGar, PacAve, 
              NorAve, ShortLine, PenAve, ParkPlace, Boardwalk]