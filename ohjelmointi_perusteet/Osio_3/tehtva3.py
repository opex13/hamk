#3. Lottoamisen kannattavuus (Pakollinen)
from random import randrange
seitsemanOikea = [4,5,9,10,15,31,40] #no... seitsemän oikein lista
generoituLista = []
rivit = 0
def tuplatPois(x):
    return list(dict.fromkeys(x))
while seitsemanOikea not in generoituLista:
#for rivit in range(10000):
    generoituLista.clear()
    for x in range(7):
        lottonumero = randrange(1,41)
        generoituLista.append(lottonumero)
        generoituLista.sort()
        generoituLista = tuplatPois(generoituLista)
        #print(generoituLista)
    print(generoituLista)
    print(rivit)
    #print(lottonumero)
    rivit += 1
print(generoituLista)
print(lottonumero)
print(rivit)
set(generoituLista)