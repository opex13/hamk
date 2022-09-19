#2. Koodin refaktorointi (Haaste)
from random import randrange
import time
yritykset = 0
omatNumerot = [1,2,3,4,5,6,7]
arvonta = []
aloitusaika = time.time()
onnistu = False
def generateRandomAndAppend(arvonta, lottorivi):
    uusiNumero = randrange(1,41)
    while uusiNumero in arvonta:
        uusiNumero = randrange(1,41)
    lottorivi.append(uusiNumero)

def appendLinesToShare(arvonta, generateRandomAndAppend, lottoOsio):
    lottorivi = []
    for e in range(7):
        generateRandomAndAppend(arvonta, lottorivi)
    lottorivi.sort()
    lottoOsio.append(lottorivi)

def appendShareToPart(arvonta, generateRandomAndAppend, appendLinesToShare, lottoLohko):
    lottoOsio = []
    for z in range(500):
        appendLinesToShare(arvonta, generateRandomAndAppend, lottoOsio)
    lottoLohko.append(lottoOsio)

def appendPartToBlock(arvonta, generateRandomAndAppend, appendLinesToShare, appendShareToPart):
    lottoLohko =[]
    for y in range(100):
        appendShareToPart(arvonta, generateRandomAndAppend, appendLinesToShare, lottoLohko)
    arvonta.append(lottoLohko)

def ifLineInShare(yritykset, omatNumerot, osio):
    for rivi in osio:
        if(rivi == omatNumerot):
            onnistu = True
            break
        yritykset += 1

def ifShareInPart(yritykset, omatNumerot, ifLineInShare, lohko):
    for osio in lohko:
        ifLineInShare(yritykset, omatNumerot, osio)

def ifPartInBlock(yritykset, omatNumerot, arvonta, ifLineInShare, ifShareInPart):
    for lohko in arvonta:
        ifShareInPart(yritykset, omatNumerot, ifLineInShare, lohko)

while not onnistu:
    arvonta.clear()
    for x in range(10):
        appendPartToBlock(arvonta, generateRandomAndAppend, appendLinesToShare, appendShareToPart)
    ifPartInBlock(yritykset, omatNumerot, arvonta, ifLineInShare, ifShareInPart)
    #Ajastus setit
    aika = (time.time() - aloitusaika)
    keskimaara = 0
    try:
        keskimaara = yritykset/aika
    except ZeroDivisionError:
        print("Softa kippas surullinen")
    print(int(keskimaara), "arpaa sekunnissa yritys nro", yritykset)
print("Oikeat numerot vastaavat omiasi", yritykset, "yrityksellä")