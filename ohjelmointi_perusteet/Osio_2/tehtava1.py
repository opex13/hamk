#ohjelmointi perusteet osio 2 tehtävä 1
print("Moi! Annatko kaksi lukua?")
numeroA = input("Tässä tulee eka numero")
numeroB = input("Tässä tulee toka numero")
#print(numeroA.isnumeric())
#tarkistetaan että molemmat syötteet ovat numerisia:
if numeroA.isnumeric() != True or numeroB.isnumeric() != True:
    print("Osan tehdä laskut vain numeroilla, sorry!")
    exit()
else:
    print("No mitä teemme näillä?")
    plusOperator = "A. plus"
    print(plusOperator)
    miinusOperator = "B. miinus"
    print(miinusOperator)
    jakoOperator = "C. jakolasku"
    print(jakoOperator)
    kertoOperator = "D. kertolasku"
    print(kertoOperator)
    operaatio = input("Anna operaatio:")
    #print(operaatio) #debug
    #print(operaatio.upper()) #debug
    numeroA = int(numeroA)
    numeroB = int(numeroB)
    if operaatio.upper == "A" or operaatio.upper() == "PLUS" or operaatio == "+":
        print("Valitsit", plusOperator)
        print(numeroA, "+", numeroB, "=", numeroA+numeroB)
    elif operaatio.upper() == "B" or operaatio.upper() == "MIINUS" or operaatio == "-":
        print("Valitsit", miinusOperator)
        print(numeroA, "-", numeroB, "=", numeroA-numeroB)
    elif operaatio.upper() == "C" or operaatio == "/" or operaatio == ":" or operaatio.upper() == "JAKO":
        print("Valitsit", jakoOperator)
        print(numeroA, "/", numeroB, "=", numeroA/numeroB)
    elif operaatio.upper() == "D" or operaatio == "*" or operaatio.upper() == "KERTO":
        print("Valitsit", kertoOperator)
        print(numeroA, "*", numeroB, "=", numeroA*numeroB)
    else:
        print("Valittu väärä operaatio, ehkä näppisvirhe?")
