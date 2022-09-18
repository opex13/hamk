#1. Numeroiden laskentaa (Pakollinen)
numeroA = int(input("Annatko numero A?"))
numeroB = int(input("Annatko numero B?"))
vastauksienLista = []
def numeroidenLaskenta(a,b):
    vastauksienLista.append(a+b)
    vastauksienLista.append(a-b)
    vastauksienLista.append(a/b)
    vastauksienLista.append(a*b)
    return vastauksienLista
def vastauksienTulostus(z):
    print(z)
numeroidenLaskenta(numeroA,numeroB)
vastauksienTulostus(vastauksienLista)