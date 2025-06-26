def pozdrav1(ime):
    return "Pozdrav " + ime + "!"

pozdrav2 = lambda ime: "Dobrodošao " + ime + "!"

def pozovi_funkciju(funkcija):
    ime = "Marko"
    print(funkcija(ime))

pozovi_funkciju(pozdrav1)
pozovi_funkciju(pozdrav2)