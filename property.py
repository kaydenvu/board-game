class Property():
  def __init__(self, name, siteColor, rent, house, house2, house3, house4, hotel, mortgage, cost):
    self.name=name
    self.siteColor=siteColor
    self.rent= rent
    self.house=house
    self.house2=house2
    self.house3=house3
    self.house4=house4
    self.hotel=hotel
    self.mortgage = mortgage
    self.costHouse=cost

MedAve = Property('Mediterranean Avenue', "Brown", 2, 10, 30, 90, 160, 250, 30,50)
BalAve = Property('Baltic Avenue',"Brown", 4, 20, 60, 180, 320, 450, 30, 50)
ReadRail = Property("Reading Railroad", "Black", 25, 0, 0, 0, 0, 0, 100, 0)
OrAve = Property('Oriental Avenue', "Light Blue", 6, 30, 90, 270, 400, 550, 50, 50)
VerAve = Property('Vermont Avenue', "Light Blue", 6, 30, 90, 270, 400, 550, 50, 50)
ConAve = Property( 'Connecticut Avenue', "Light Blue", 8, 40, 100, 300, 450, 600,60, 50)
StChar = Property('St. Charles Place', "Pink",10, 50, 150, 450, 625, 750,70, 100)
EleComp = Property("Electric Company", "Utility", 0, 0, 0,0, 0,0,75,0)
StaAve = Property( 'States Avenue', "Pink", 10, 50, 150, 450, 625, 750, 70, 100)
VirAve = Property('Virginia Avenue', "Pink", 12, 60, 180, 500, 700, 900, 80, 100)
PennRail = Property("Pennsylvania Railroad", "Black", 25, 0,0,0,0,0,100,0)
StJames = Property('St. James Place', "Orange", 14, 70, 200, 550, 750, 950, 90, 100)
TenAve = Property('Tennessee Avenue', "Orange", 14, 70, 200, 550, 750, 950, 90, 100)
NewAve = Property('New York Avenue', "Orange" ,16, 80, 220, 600, 800, 1000, 100, 100)
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

properties = [MedAve, BalAve, OrAve, VerAve, ConAve, StChar, StaAve, VirAve, StJames, 
              TenAve, NewAve, KenAve, IndAve, IllAve, AtlAve, VenAve, MarGar, PacAve, 
              NorAve, PenAve, ParkPlace, Boardwalk]