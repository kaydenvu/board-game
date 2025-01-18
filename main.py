import random
import pygame
from tiles import board, INJAILPOS
from enum import Enum

# figure out git configs to work properly

pygame.init()

pieceSize = 50

boardImage=pygame.image.load("board.jpg")
boardImage=pygame.transform.scale(boardImage,(500,500))
battleshipImage=pygame.image.load("pieces/battle ship.png")
battleshipImage=pygame.transform.scale(battleshipImage,(pieceSize, pieceSize))
bootImage=pygame.image.load("pieces/boot.png")
bootImage=pygame.transform.scale(bootImage,(pieceSize, pieceSize))
dogImage=pygame.image.load("pieces/dog.png")
dogImage=pygame.transform.scale(dogImage,(pieceSize, pieceSize))
ironImage=pygame.image.load("pieces/iron.png")
ironImage=pygame.transform.scale(ironImage,(pieceSize, pieceSize))
raceCarImage=pygame.image.load("pieces/race car.png")
raceCarImage=pygame.transform.scale(raceCarImage,(pieceSize, pieceSize))
thimbleImage=pygame.image.load("pieces/thimble.png")
thimbleImage=pygame.transform.scale(thimbleImage,(pieceSize, pieceSize))
topHatImage=pygame.image.load("pieces/top hat.png")
topHatImage=pygame.transform.scale(topHatImage,(pieceSize, pieceSize))
wheelbarrowImage=pygame.image.load("pieces/wheelbarrow.png")
wheelbarrowImage=pygame.transform.scale(wheelbarrowImage,(pieceSize, pieceSize))
num2= pygame.image.load("numbers/2.png")
num3= pygame.image.load("numbers/3.png")
num4= pygame.image.load("numbers/4.png")
num5= pygame.image.load("numbers/5.png")
num6= pygame.image.load("numbers/6.png")
num7= pygame.image.load("numbers/7.png")
num8= pygame.image.load("numbers/8.png")
piece1 = pygame.image.load("monopoly pieces/1.png")
piece2 = pygame.image.load("monopoly pieces/2.png")
piece3 = pygame.image.load("monopoly pieces/3.png")
piece4 = pygame.image.load("monopoly pieces/4.png")
piece5 = pygame.image.load("monopoly pieces/5.png")
piece6 = pygame.image.load("monopoly pieces/6.png")
piece7 = pygame.image.load("monopoly pieces/7.png")
piece8 = pygame.image.load("monopoly pieces/8.png")
dice1 = pygame.image.load("dice/1.png")
dice2 = pygame.image.load("dice/2.png")
dice3 = pygame.image.load("dice/3.png")
dice4 = pygame.image.load("dice/4.png")
dice5 = pygame.image.load("dice/5.png")
dice6 = pygame.image.load("dice/6.png")
roll = pygame.image.load("roll.png")
buy = pygame.image.load("Buy button.png")
skip = pygame.image.load("Skip button.png")
confirm = pygame.image.load("Confirm Button.png")
pay = pygame.image.load("Pay button.png")
diePossiblities = [dice1, dice2, dice3, dice4, dice5, dice6]

screenWidth = 500
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
V = pygame.Vector2

pygame.display.set_caption("Monopoly")

playerAmount=0

PlayerNumUI = pygame.sprite.Group()
PlayerPiecesUI = pygame.sprite.Group()
BoardDisplay = pygame.sprite.Group()

class Button(pygame.sprite.Sprite):
  mouseDown = False
  showAlert = False
  def __init__(self, image, pos, scale, actionType, value = None, *groups):
    super().__init__(*groups)
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(image, (int(width) * scale, int(height) * scale))
    self.rect = self.image.get_rect()
    self.rect.topleft = pos
    self.clicked = False
    self.actionType = actionType
    self.value = value
  def resetButton(self):
    global gameState
    gameState = STATE.PLAY
    self.clicked = False
    Button.showAlert = False
    buyButton.clicked = False
  def draw(self):
    action = False
    pos = pygame.mouse.get_pos()
    if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
        self.clicked = True
        action = True
        Button.mouseDown = True
    screen.blit(self.image, self.rect)
    return action
  def update(self):
    global playerAmount, gameState, lastPlayer, tile
    if self.actionType == "num players":
      if self.draw():
        playerAmount = self.value
      if self.clicked and not Button.mouseDown:
        gameState = STATE.START_PIECES
    if self.actionType == "players pieces":
      if self.draw():
        tempPlayer = Player()
        tempPlayer.piece = self.value
        players.append(tempPlayer)
        self.kill()
        if len(players) == playerAmount:
          gameState = STATE.PLAY
          print(players)
    if self.actionType == "roll dice":
      global diceRolling
      if self.draw():
        diceRolling = True
        pygame.time.set_timer(rollingDice, Die.rollTime)  
        self.resetButton()
    if self.actionType == "buy":
      self.draw()
      if self.clicked and not Button.mouseDown:
        if lastPlayer.money>= tile.value:
          lastPlayer.money -= tile.value
          self.resetButton()
        else:
          Button.showAlert = True
        if Button.showAlert:
          drawText("Not enough money", V(250, 300))
    if self.actionType == "skip":
      self.draw()    
      if self.clicked and not Button.mouseDown:
        self.resetButton()
    if self.actionType == "confirm":
      self.draw()
      if self.clicked and not Button.mouseDown:
        if tile.tileType == "Go To Jail":
          lastPlayer.position = 10
          lastPlayer.inJail = True
        self.resetButton()
    if self.actionType == "pay":
      self.draw()
      if self.clicked and not Button.mouseDown:
        if lastPlayer.money >= 50:
          lastPlayer.money -= 50
          lastPlayer.inJail = False
          lastPlayer.jailTime = 0
          self.resetButton()
        else:
          Button.showAlert = True
        if Button.showAlert:
          drawText("Not enough money", V(250, 300))

for idx, num in enumerate([num2, num3, num4, num5], 2):
  Button(num, V(5 + (idx - 2) * 125 ,100), 0.5, "num players", idx, PlayerNumUI)
for idx, num in enumerate([num6,num7,num8], 6):
  Button(num, V(65 + (idx - 6) * 125 ,300), 0.5, "num players", idx, PlayerNumUI)

class Piece():
  def __init__(self, name, image):
    self.name = name
    self.image=image
  def __repr__(self):
    return self.name

class Player():
  def __init__(self):
    self.piece=Piece("temp", boardImage)
    self.position=0
    self.money=1500
    self.properties=[]
    self.inJail = False
    self.jailTime= 0
  def __repr__(self):
    return self.piece.name
    
battleship = Piece("battleship", battleshipImage)
raceCar=Piece("race car", raceCarImage)
wheelbarrow=Piece("wheelbarrow", wheelbarrowImage)
iron=Piece("iron", ironImage)
boot=Piece('boot', bootImage)
tophat=Piece('top hat', topHatImage)
dog=Piece('dog', dogImage)
thimble=Piece('thimble', thimbleImage)
pieces=[battleship, raceCar, wheelbarrow, iron, boot, tophat, dog, thimble]

for idx, item in enumerate([piece1, piece2, piece3, piece4]):
  Button(item, V(5 + (idx) * 125 ,150), 0.3, "players pieces", pieces[idx], PlayerPiecesUI)

for idx, item in enumerate([piece5, piece6, piece7, piece8], 4):
  Button(item, V(5 + (idx - 4) * 125 ,350), 0.3, "players pieces", pieces[idx], PlayerPiecesUI)

def printPieces():
  print("Choose a piece:")
  for piece in pieces:
    print("\t", piece)

players=[]
player = None
lastPlayer = None
tile = board[0]
    
random.shuffle(players)
print("Order:", players)


class Die():
  rollTime=150
  def __init__(self, pos):
    self.pos = V(pos)
    self.value = 0
    self.stopDieValue = random.randint(1, 10000)
    self.images = diePossiblities
    self.image = dice1
    self.rect = self.image.get_rect(center = self.pos)
  def roll(self):
    self.value = random.randint(1,6)
    self.stopDieValue = random.randint(1,10)
  def draw(self):
    self.image = self.images[self.value - 1]
    self.image = pygame.transform.smoothscale(self.image, (175, 175))
    self.rect = self.image.get_rect(center = self.pos)
    screen.blit(self.image, self.rect)

die1 = Die((170, 170))
die2 = Die((330, 330))
rollButton = Button(roll, V(215, 215), 0.5, "roll dice")
buyButton = Button(buy, V(125,200), 0.5, "buy")
skipButton = Button(skip, V(300, 200), 0.5, "skip")
confirmButton = Button(confirm, V(195,215), 0.5, "confirm")
payButton = Button(pay, V(300,215), 0.5, "pay")

rollDoubles = False

def diceRoll():
  return (random.randint(1,6), random.randint(1,6))
  
def move(player, d1, d2):
  roll = d1 + d2
  if player.inJail:
    if d1 == d2:
      player.inJail = False
      player.position+=roll
      player.jailTime = 0
    player.jailTime += 1
    if player.jailTime == 3:
      player.money -= 50
      player.position += roll
      player.inJail = False
      player.jailTime = 0
  else: player.position += 10
  if player.position >= 40:
    player.position -= 40
    player.money+=200
  return player.position

font = pygame.font.Font('Rubik.ttf', 32)

def drawText(text, pos, color=(0,0,0)):
  textSurface = font.render(text, True, color)
  textRect = textSurface.get_rect(center = pos)
  screen.blit(textSurface, textRect)

def printBoard():
  for tile in board:
    print(tile.name, end=" ")
    if tile.isOwned:
      print(tile.owner)
    else:
      print()

def updateBoard():
  global player, gameState, lastPlayer, tile
  lastTurn = turn - 1
  lastPlayer = players[lastTurn]
  tile = board[lastPlayer.position]
  screen.blit(boardImage,(0,0))
  if len(players)>=1 and not firstTurn:
    drawText(lastPlayer.piece.name,V(350,100))
    drawText("$" + str(lastPlayer.money), V(350, 150))
    # if player.inJail:
    #   drawText(lastPlayer.piece.name + " has been in jail for " + str(lastPlayer.jailTime) + " turns.", (250, 350))
    drawText(lastPlayer.piece.name + " landed on ", (250, 350))
    drawText(tile.name, (250, 400))
  for player in players:
    if board[player.position].name == "Jail" and player.inJail: 
      screen.blit(player.piece.image, INJAILPOS)
    else:
      screen.blit(player.piece.image, board[player.position].position)
  if diceRolling:
    die1.draw()
    die2.draw()
  elif gameState == STATE.PLAY:
    rollButton.update()
    if lastPlayer.inJail:
      payButton.update()
  elif gameState == STATE.PLAY_CHOOSE:
    if tile.tileType == "Property":
      drawText("$" + str(tile.value), V(160, 185))
      buyButton.update()
      skipButton.update()
    else:
      confirmButton.update()
  pygame.display.update()
  
GameRunning=True
firstTurn = True

class STATE(Enum):
  START_NUM_PLAYERS = 0
  START_PIECES = 1
  PLAY = 2
  PLAY_CHOOSE = 3
  END = 4

gameState = STATE.START_NUM_PLAYERS
rollingDice = pygame.USEREVENT + 1
diceRolling = False
turn = 0

while GameRunning:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
        Button.mouseDown = False
    if event.type == pygame.QUIT:
      GameRunning = False
    if event.type == rollingDice:
      die1.roll()
      die2.roll() 
      if die1.stopDieValue == die2.stopDieValue and diceRolling:
        die1.draw()
        die2.draw()
        pygame.display.update()
        pygame.time.wait(500)
        pygame.time.set_timer(rollingDice, 0)
        diceRolling = False
        rollButton.clicked = False
        firstTurn = False
        move(player, die1.value, die2.value)
        print(player.piece.name, die1.value, die2.value, board[player.position].name)
        updateBoard()
        gameState = STATE.PLAY_CHOOSE
        # do double skip turn here
        if turn < len(players)-1:
          turn+=1
        else:
          turn = 0
      elif diceRolling:
        pygame.time.set_timer(rollingDice, Die.rollTime)
  if gameState == STATE.START_NUM_PLAYERS:
    screen.fill("white")
    drawText("Pick the number of players", V(250,25))
    drawText("in the game", V(250,75))
    PlayerNumUI.update()
  if gameState == STATE.START_PIECES:
    screen.fill("white")
    drawText("Pick the pieces", V(250,75))
    PlayerPiecesUI.update()
    random.shuffle(players)
  if gameState == STATE.PLAY:
    player = players[turn]
    updateBoard()
    player = players[turn]
  if gameState == STATE.PLAY_CHOOSE:
    updateBoard()
  pygame.display.update()
    