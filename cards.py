import tiles
class Card():
  def __init__(self, description, value, effect):
    self.description=description
    self.value=value
    self.effect=effect
  def __repr__(self):
    return self.description

advBoard = Card('Advance to Boardwalk.', tiles.B.tileIdx, 'advance')
advGo = Card('Advance to Go (Collect $200).', tiles.GO.tileIdx, 'advance')
advIll = Card( 'Advance to Illinois Ave. (If you pass Go, collect $200).', tiles.IA.tileIdx, 'advance')
advStCharles = Card('Advance to St. Charles Place. (If you pass Go, collect $200),', tiles.SC.tileIdx, 'advance')
advRail = Card('Advance to nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled.', 0, 'railroad')
advUtil = Card('Advance to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.', 0, 'utility')
bankDiv = Card("Bank pays you dividend of $50.", 50, 'collect')
getOutOfJail = Card('Get out of Jail Free.', 0, 'getOutOfJail')
goback = Card('Go back 3 spaces.', 3, 'goback')
goToJail = Card('Go directly to Jail, do not pass Go, do not collect $200.', tiles.JAIL.tileIdx, 'goToJail')
Genrepairs = Card( 'Make general repairs on all your property. For each house pay $25. For each hotel pay $100.', 0, 'repairs')
Speeding = Card('Speeding fine $15.', 15, 'fine')
advReading = Card( 'Take a trip to Reading Railroad. If you pass Go, collect $200' , tiles.RR.tileIdx, 'advance')
Chairman = Card('You have been elected Chairman of the Board. Pay each player $50', 0, 'chairman')
buildLoan = Card('Your building loan matures. Collect $150.', 150, 'collect')
BankError = Card('Bank error in your favor. Collect $200.', 200, 'collect')
doctorsFees = Card('Doctor’s fees. Pay $50.', 50, 'fine')
StockSale = Card('From sale of stock you get $50', 50, 'collect')
HolidayFund = Card('Holiday fund matures. Receive $100' , 100, 'collect')
TaxRefund = Card('Income tax refund. Collect $20.', 20, 'collect')
Birthday = Card('It’s your birthday. Collect $10 from every player.', 0, 'birthday')
LifeInsure = Card('Life insurance matures. Collect $100.', 100, 'collect')
HospitalFee = Card('Hospital fees. Pay $100.', 100, 'fine')
SchoolFee = Card('Pay school fees of $50', 50, 'fine')
ConFee = Card('Receive $25 consultancy fee', 25, 'collect')
StreetRep = Card('You are assessed for street repairs. Pay $40 per house. $115 per hotel.', 0, 'streetRepair')
BeautyCon = Card('You have won second prize in a beauty contest. Collect $10.', 10, 'collect')
Inherit = Card('You inherit $100.', 100, 'collect')
CCcards=[advGo, BankError, doctorsFees, StockSale, getOutOfJail, goToJail, HolidayFund, TaxRefund, Birthday, LifeInsure, HospitalFee, SchoolFee, ConFee, StreetRep, BeautyCon, Inherit]
CHcards=[advBoard, advGo, advIll, advStCharles, advRail, advRail, advUtil, bankDiv, getOutOfJail, goback, goToJail, Genrepairs, Speeding, advReading, Chairman, buildLoan]
