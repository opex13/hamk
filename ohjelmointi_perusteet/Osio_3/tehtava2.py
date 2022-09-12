#2. Ostoslista (Pakollinen)
ostoslista = []
seuraava = input("anna ensimmäinen listan kohde")
while seuraava != "valmis":
    ostoslista.append(seuraava)
    print("lisäsit listaan",seuraava)
    seuraava = input("anna seuraava listan kohde")
ostoslista.sort()
print(ostoslista)