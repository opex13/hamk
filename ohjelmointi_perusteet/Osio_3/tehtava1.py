#1. Arvaa käyttäjän ikä (Pakollinen)
minunIka = 34
arvoitus = int(input("arvatko mikä ikäinen olen?"))
while arvoitus != minunIka:
    arvoitus = int(input("kokeile vielä kerran"))
print("olet oikeassa!")