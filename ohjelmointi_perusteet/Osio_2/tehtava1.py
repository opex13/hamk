#ohjelmointi perusteet osio 2 tehtävä 1
print("Moi! Annatko kaksi lukua?")
numeroA = int(input("Tässä tulee eka numero"))
numeroB = int(input("Tässä tulee toka numero"))
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
if operaatio.upper == "A" or "PLUS" or "+":
    print("Valitsit", plusOperator)
    print(numeroA, "+", numeroB, "=", numeroA+numeroB)
elif operaatio.upper == "B" or "MIINUS" or "-":
    print("Valitsit", miinusOperator)
    print(numeroA, "-", numeroB, "=", numeroA-numeroB)
elif operaatio.upper == "C" or "/" or ":" or "JAKO":
    print("Valitsit", jakoOperator)
    print(numeroA, "/", numeroB, "=", numeroA/numeroB)
elif operaatio.upper == "D" or "*" or "KERTO":
    print("Valitsit", kertoOperator)
    print(numeroA, "*", numeroB, "=", numeroA*numeroB)
else:
    print("Valittu väärä operaatio, ehkä näppisvirhe?")
