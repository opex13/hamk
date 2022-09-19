#1. Numeroiden laskentaa (Pakollinen)
def tulo(a, b):
    vastauksienLista.append(a*b)

def osamaara(a, b):
    vastauksienLista.append(a/b)

def erotus(a, b):
    vastauksienLista.append(a-b)

def summa(a, b):
    vastauksienLista.append(a+b)
    
def numeroidenLaskenta(a,b):
    summa(a, b)
    erotus(a, b)
    osamaara(a, b)
    tulo(a, b)
    return vastauksienLista

def vastauksienTulostus(z):
    print("numeroiden summa on",z[0],"erotus on",z[1],"osamäärä",z[2],"ja tulo on",z[3])
    
#actual code starts here
numeroA = int(input("Annatko numero A?"))
numeroB = int(input("Annatko numero B?"))
vastauksienLista = []
numeroidenLaskenta(numeroA,numeroB)
vastauksienTulostus(vastauksienLista)