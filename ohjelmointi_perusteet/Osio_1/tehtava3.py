#ohjelmointi perusteet tehävä 3
KkTulo = int(input("Moi! Paljonko keskimäärin kuukaudessa jää rahaa elämiseen?"))
PvKampuksella = int(input("Montako koulupäiviä viedät kampuksella kuukaudessa?"))
RuuanHinta = int(input("Paljonko maksaa koulussa ateria?"))
KkRuokaMenot = PvKampuksella*RuuanHinta
Budjetti = KkTulo-KkRuokaMenot
print("Siis kouluruokaan menee", KkRuokaMenot , "€/kk, ja budjettistä jää", Budjetti, "€")
MuutMenot = int(input("Paljonko menee  muihin elämiskustannuksiin?"))
SaastoMahdollisuus = (Budjetti-MuutMenot)*0.2
#desimaalit erotellan pisteella, ei pilkulla :D
print("Eli säästöpossuun voi laita", SaastoMahdollisuus, "€")
KkJaljella = int(input("Paljonko kuukautta vielä opiskeltava?"))
print("Koko opiskelun aikanan se tekisi", SaastoMahdollisuus*KkJaljella, "€ potti!")