# Python projekti vanhan pelin inspioimana - https://jonesinthefastlane.com/
from gameClasses import player
from random import randrange

#tässä yritetty luoda dynaaminen pelaajien luonti
#playersInGame = int(input("Tervetuloa peliin! Paljonko pelaajia?"))
#
#PlayersDict = {}
#
#for x in range(playersInGame):
#    PlayersDict[x] = str("player",str(x+1))
#    print(PlayersDict)

player1 = player()
player1.setName(input("kuka on ensimmäinen pelaja?"))
player2 = player()
player2.setName(input("kuka on toinen pelaja?"))
player1.stats()
player2.stats()

playersList = []
playersList.append(player1)
playersList.append(player2)
#print(playersList)

winGoal = int(input("Paljonko rahaa pitää kerätä voittamiseen?"))
for playerIsPlaying in playersList:                  #silmukka pelaajin listalle pyörimiseen
    while winGoal > playerIsPlaying.money:           #tarkistus onko rahat kerätty riitävästi
        for playerIsPlaying in playersList:          #silmukka pellajin
            print("Mitä", playerIsPlaying.name, "tänään voisi tehdä?")
            roundInput = int(input("1. Tehdä töitä. 2. Levätä 3. Pelata lottoa"))
            if roundInput == 1:
                playerIsPlaying.work(randrange(1,5),randrange(1,5))
                playerIsPlaying.stats()
            elif roundInput == 3:
                playerIsPlaying.lotto(int(input("paljonko rivia ostetaan?")))
            else:
                playerIsPlaying.newRound()
print(playerIsPlaying.name, "voitti")