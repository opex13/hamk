#1. Tili (Pakollinen)

from tili import tili

omaTili = tili()
omaTili.tiliote()
omaTili.talleta(float(input("paljonko laitetaan tilille?")))
omaTili.nosta(float(input("paljonko otetaan käteisenä?")))
omaTili.korkoaKorolle(float(input("paljonko on korkotasoa nyt?")),int(input("kuinka moneksi vuodeksi sijoitat?")))
#omaTili.tiliote()