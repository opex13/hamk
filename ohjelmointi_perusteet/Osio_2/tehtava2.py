#ohjelmointi perusteet osio 2 tehtävä 2
#ensiksi määritellään tekstit
#tarinan kirjoitus Olivia 10v ja Nicole 6v
tehvehdys = "Moi! tervetuloa tekstiseikkailuun!"
kysymysA = "Olet kotona pelaamassa pleikkaria, ja huomaat että lentävä koira lensi ikkunasta sisään ja nappasi pleikkaria, mitä teet?"
vaihtoehtoA1 = "1. Koiran on saatava kiini! Äkkiä, ulos!"
vaihtoehtoA2 = "2. Itket hetken kotona, ja sitten menet ulos."
kysymysA1 = "Lentävä koira lentää nopeasti, millä meinaat saavutta sen?"
vaihtoehtoA11 = "1. Olen koulun nopein juoksija!"
vaihtoehtoA12 = "2. Hyppään polkupyörän selälle."
tulosA11 = "Juokset niin kova, kun et ikinä ennen, mutta lentävä koira on nopeampi, joudut palamaan kotiin ilman pleikkaria"
tulosA12 = "Kukapa uskoisi, että lentävä koira pelkää polkupyöriä, pleikkari putosi maahan, noudat sen ja menet kotiin"
KysymysA2 = "Sun itkua kuuli koko talon, ja myös vanhemmat. He kysyvät miksi itkit. Mitä sanot heille?"
vaihtoehtoA21 = "1. Kerrot totuuden koirasta ja pleikkarista"
vaihtoehtoA22 = "2. Sanot, että on kiiretta ja selität myöhemin"
tulosA21 = "Äiti sanoi iskälle asian hoidettavaksi, ja sun iskä soitti koiran iskälle, ja hän toi pleikkari takaisin."
tulosA22 = "Lipsahdat ulos, ja kun tulit takaisin illalla vanhemmat huomasivat pleikkarin puuttuvan, ja nyt olet kotiarestilla jouluun saakkaa."
#tästä alkaa if else logiikka
print(tehvehdys)
print(kysymysA)
print(vaihtoehtoA1)
print(vaihtoehtoA2)
vastaus = int(input("1 tai 2?"))
if vastaus == 1:
    print(kysymysA1)
    print(vaihtoehtoA11)
    print(vaihtoehtoA12)
    vastaus2taso = int(input("1 tai 2?"))
    if vastaus2taso == 1:
        print(tulosA11)
    elif vastaus2taso == 2:
        print(tulosA12)
    else: print("voi valita 1 tai 2, aloita uudestaan")
elif vastaus == 2:
    print(KysymysA2)
    print(vaihtoehtoA21)
    print(vaihtoehtoA22)
    vastaus2taso = int(input("1 tai 2?"))
    if vastaus2taso == 1:
        print(tulosA21)
    elif vastaus2taso == 2:
        print(tulosA22)
    else: print("voi valita 1 tai 2, aloita uudestaan")
else: print("voi valita 1 tai 2, aloita uudestaan")