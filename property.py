class Property():
  def __init__(self, name, site, siteColor, house, house2, house3, house4, hotel, cost):
    self.name=name
    self.site=site
    self.siteColor=siteColor
    self.house=house
    self.house2=house2
    self.house3=house3
    self.house4=house4
    self.hotel=hotel
    self.costHouse=cost

MedAve = Property('Mediterranean Avenue', 2, 4, 10, 30, 90, 160, 250, 50)
BalAve = Property('Baltic Avenue', 4, 8, 20, 60, 180, 320, 450, 50)
OrAve = Property('Oriental Avenue', 6, 12, 30, 90, 270, 400, 550, 50)
VerAve = Property('Vermont Avenue', 6, 12, 30, 90, 270, 400, 550, 50)
ConAve = Property( 'Connecticut Avenue', 8, 16, 40, 100, 300, 450, 600, 50)
StChar = Property('St. Charles Place', 10, 20, 50, 150, 450, 625, 750, 100)
StaAve = Property( 'States Avenue', 10, 20, 50, 150, 450, 625, 750, 100)
VirAve = Property('Virginia Avenue', 12, 24, 60, 180, 500, 700, 900, 100)
StJames = Property('St. James Place', 14, 28, 70, 200, 550, 750, 950, 100)
TenAve = Property('Tennessee Avenue', 14, 28, 70, 200, 550, 750, 950, 100)
NewAve = Property('New York Avenue', 16, 32, 80, 220, 600, 800, 1000, 100)
KenAve = Property('Kentucky Avenue', 18, 36, 90, 250, 700, 875,	1050, 150)
IndAve = Property('Indiana Avenue', 18, 36, 90, 250, 700, 875, 1050, 150)
IllAve = Property('Illinois Avenue', 20, 40, 100, 300, 750, 925, 1100, 150)
AtlAve = Property('Atlantic Avenue', 22, 44, 110, 330, 800, 975, 1150, 150)
VenAve = Property('Ventnor Avenue', 22, 44, 110, 330, 800, 975, 1150, 150)
MarGar = Property('Marvin Gardens', 24, 48, 120, 360, 850, 1025, 1200, 150)
PacAve = Property('Pacific Avenue', 26, 52, 130, 390, 900, 1100, 1275, 200)
NorAve = Property('North Carolina Avenue', 26, 52, 130, 390, 900, 1100, 1275, 200)
PenAve = Property('Pennsylvania Avenue', 28, 56, 150, 450, 1000, 1200, 1400, 200)
ParkPlace = Property('Park Place', 35, 70, 175, 500, 1100, 1300, 1500, 200)
Boardwalk = Property('Boardwalk', 50, 100, 200, 600, 1400, 1700, 2000, 200)

properties = [MedAve, BalAve, OrAve, VerAve, ConAve, StChar, StaAve, VirAve, StJames, 
              TenAve, NewAve, KenAve, IndAve, IllAve, AtlAve, VenAve, MarGar, PacAve, 
              NorAve, PenAve, ParkPlace, Boardwalk]