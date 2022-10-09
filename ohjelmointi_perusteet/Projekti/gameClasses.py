# tässä tiedostossa ovat pelin käyttämät luokkaat
from random import randint


class player:
    money = 0
    energy = 0
    name = ""
    weeks = 0
    playerId = 0
    
    def __init__(self):
        self.money = 0
        self.energy = 10
        name = "player1"
    
    def stats(self): #tulosta pelaajan tiedot
        print("pelajan",self.name, "energiaa:", self.energy, "rahaa:", self.money, "viikko", self.weeks)
        
    def setName(self, givenName): #aseta uuden nimen
        self.name = givenName
    
    def newRound(self): #uusi kierros
        self.energy = 10
        self.stats
        self.weeks += 1
        
    def work(self, earnedMoney, spendEnergy): #työn tekeminen
        if self.energy < spendEnergy:
            print("sinulla ei ole riittävästi energiaa, täytyy levätä")
        else:
            self.money += earnedMoney
            self.energy -= spendEnergy
        return(earnedMoney, spendEnergy)
        self.stats
        
    def spendMoney(self, x): #ostaminen
        if(x > self.money):
            print("ei ole rahaa ostoksille")
        else: 
            self.money -= x
            print("Teit ostoksen", x, "summalla, tililläsi", self.money, "rahaa")
            
    def spendEnergy(self, x): #energian käyttö
        if(x > self.energy):
            print("ei ole riitävästi energiaa")
        else: 
            self.energy -= x
            print("Sinulla on", x, "energiaa jäljellä")


    def lotto(self, ticketsToBuy): #lottoa
        if ticketsToBuy > self.money:
            print("ei ole rahaa pelamiseen")
        else:
            self.money -= ticketsToBuy
            if randint(1,100) > 95:
                ticketWon = randint(1,100)
                self.money += ticketWon
                print("olet voittanut", ticketWon)
            else:
                print("tuhlasit", ticketsToBuy,"rahaa")
            player.stats
    