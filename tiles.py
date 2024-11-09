import pygame

V = pygame.Vector2

class Tile():
  tileIdx = 0
  def __init__(self,tileType,name, color, value, position=V(0,0)):
    self.tileIdx = Tile.tileIdx
    Tile.tileIdx += 1
    self.tileType=tileType
    self.name = name
    self.color=color
    self.value=value
    self.houses=0
    self.hotel=0
    self.rent=0
    self.isMortgaged=False
    self.isOwned=False
    self.owner=None
    self.position = position
  def __repr__(self):
    return self.name

INJAILPOS = V(10, 435)
GO=Tile('Go', 'Go', None, 200, V(440, 450))
MA=Tile('Property','Mediterranean Avenue','Brown',60, V(382, 450))
CC=Tile('Community Chest', 'Community Chest', None, 0, V(342,450))
BA=Tile('Property', 'Baltic Avenue', "Brown", 60, V(300,450))
IT=Tile('Income Tax', 'Income Tax', None, 200,V(262,450))
RR=Tile('Property', 'Reading Railroad', 'Black', 200, V(222,450))
OA=Tile( 'Property', 'Oriental Avenue', 'Light Blue', 100, V(180,450))
CH=Tile('Chance', 'Chance', None, 0,V(140,450))
VA=Tile('Property', 'Vermont Avenue', 'Light Blue', 100, V(100,450))
CA=Tile('Property', 'Connecticut Avenue', 'Light Blue', 120, V(60,450))
JAIL=Tile('Jail', 'Jail', None, 0,V(-10,450))
SC=Tile('Property', 'St. Charles Place', 'Pink', 140, V(-10,385))
EC=Tile('Property', 'Electric Company', 'Utility', 150, V(-10,345))
SA=Tile('Property', 'States Avenue', 'Pink', 140, V(-10,305))
VirA=Tile('Property', 'Virginia Avenue', 'Pink', 160, V(-10,265))
PR=Tile('Property', 'Pennsylvania Railroad', 'Black', 200, V(-10,225))
JP=Tile('Property', 'St. James Place', 'Orange', 180, V(-10,185))
CC2=Tile('Community Chest', 'Community Chest', None, 0, V(-10,145))
TA=Tile('Property', 'Tennessee Avenue', 'Orange', 180,V(-10,105))
NYA=Tile('Property', 'New York Avenue', 'Orange', 200,V(-10,60))
FP=Tile( 'Free Parking', 'Free Parking', None, 0,V(0,0))
KA=Tile('Property', 'Kentucky Avenue', 'Red', 220, V(60,0))
CH2=Tile('Chance', 'Chance', None, 0, V(100,0))
IA=Tile('Property', 'Indiana Avenue', 'Red', 220,V(140,0))
IL=Tile('Property', 'Illinois Avenue', 'Red', 240,V(180,0))
BNO=Tile('Property', 'B. & O. Railroad', 'Black', 200,V(222,0))
AA=Tile('Property', 'Atlantic Avenue', 'Yellow', 260,V(260,0))
VET=Tile('Property', 'Ventnor Avenue', 'Yellow', 260,V(300,0))
WW=Tile('Property', 'Water Works', 'Utility', 150,V(342,0))
MG=Tile('Property', 'Marvin Gardens', 'Yellow', 280,V(382,0))
GOJail=Tile('Go To Jail', 'Go To Jail', None, 0,V(440,0))
PA=Tile('Property', 'Pacific Avenue', 'Green', 300,V(440,60))
NC=Tile('Property', 'North Carolina Avenue', 'Green', 300,V(440,105))
CC3=Tile( 'Community Chest', 'Community Chest', None, 0,V(440,145))
Penn=Tile('Property', 'Pennsylvania Avenue', 'Green', 320,V(440,185))
SL=Tile('Property', 'Short Line', 'Black', 200,V(440,225))
CH3=Tile('Chance', 'Chance', None, 0,V(440,265))
PP=Tile( 'Property', 'Park Place', 'Dark Blue', 350,V(440,305))
LT=Tile('Luxury Tax', 'Luxury Tax', None, 100,V(440,345))
B=Tile('Property', 'Boardwalk', 'Dark Blue', 400,V(440,385))

board =[GO,MA,CC,BA,IT,RR,OA,
        CH,VA,CA,JAIL,SC,EC,SA,
        VirA,PR,JP,CC2,TA,NYA,FP,KA,
        CH2,IA,IL,BNO,AA,VET,WW,MG,
        GOJail,PA,NC,CC3,Penn,SL,CH3,PP,LT,B]