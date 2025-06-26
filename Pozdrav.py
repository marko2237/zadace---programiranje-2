def pozdrav1(ime):
    return "Pozdrav " + ime + "!"

pozdrav2 = lambda ime: "Dobrodošao " + ime + "!"

def pozovi_funkciju(funkcija, ime):
    print(funkcija(ime))