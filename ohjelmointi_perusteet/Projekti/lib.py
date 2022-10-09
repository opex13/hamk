# tässä tiedostossa ovat pelin käyttämät luokkaat
from unicodedata import name


class player:
    money = 0
    energy = 0
    name = ""
    
    def __init__(self):
        self.money = 0
        self.energy = 10
        name = "player1"
    
    def newRound():
        self.energy = 10
        
    def earned(x):
        self.money += x
        
    def spendMoney(x):
        if(x > self.money):
            print("ei ole rahaa ostoksille")
        else: 
            self.money -= x
            print("Teit ostoksen", x, "summalla, tililläsi", self.money, "rahaa")
            
    def spendEnergy(x):
        if(x > self.energy):
            print("ei ole riitävästi energiaa")
        else: 
            self.energy -= x
            print("Sinulla on", x, "energiaa jäljellä")

    def stats():
        print("energiaa:", self.energy, "rahaa:", self.money)
    