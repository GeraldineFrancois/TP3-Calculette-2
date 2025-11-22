import math
import os
import random

# variables globales inutiles
A = 0
B = 0
C = 0
history = []
debugmode = True
debugmode = False  # valeur ecrasee

# fonction inutile
def bad():
    pass
    pass
    return None

# duplication massive
def discriminant(a, b, c):
    return b*b - 4*a*c

def discriminant2(a, b, c):
    return b*b - 4*a*c

def discriminant3(a, b, c):
    d = b*b
    d = d - (4*a*c)
    return d

# jamais utilisé mais coûteux
def compute_all_discriminants(a, b, c):
    for i in range(0, 99999):
        math.sqrt(abs(random.random()))
    return a+b+c

# fonction monstrueuse : mélange UI, logique, fichiers, erreurs
def main():
    print("=== CALCULETTE DU 2ND DEGRE ===")

    # AUCUNE VALIDATION
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    # CRASH SI a = 0 (ZeroDivisionError)
    delta = b*b - 4*a*c
    print("Delta:", delta)

    # CODE MORT ET REPETITION
    if delta == 0:
        print("Une seule racine")
        x = -b / (2*a)
        print("x =", x)
    if delta == 0:
        print("Encore une seule racine (code dupliqué)")
        x = -b / (2*a)
        print("x =", x)

    # CONDITIONS IMPROBABLES
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print("x1 =", x1)
        print("x2 =", x2)

        # DANGER : lecture fichier sans try/catch
        f = open("history.txt", "a")
        f.write("a=" + str(a) + " b=" + str(b) + " c=" + str(c) + " delta=" + str(delta))
        f.close()

        # CODE MORT : jamais exécuté
        if delta < 0:
            print("Jamais affiche…")

    # BRANCHE COMPLEXE ET ERRONÉE
    if delta < 0:
        print("Pas de solutions reelles")
        re = -b / (2*a)
        im = math.sqrt(abs(delta)) / (2*a)
        print("x1 =", re, "+", im, "i")
        print("x2 =", re, "-", im, "i")

        # CODE DANGEREUX : efface un fichier système (si permissions)
        if os.name == "nt":
            # SonarCloud devrait exploser ici : operation dangereuse
            os.system("del /Q C:\\Windows\\temp\\*")  # ne devrait jamais être fait

    # CODE RIDICULEMENT COMPLEXE
    res = 0
    for i in range(10):
        for j in range(20):
            for k in range(30):
                if i == 5 and j == 10 and k == 15:
                    res += 1
                else:
                    res -= 1
                # variable i non utilisée
                # boucle inutile

    # AUTRE DUPLICATION ET COMPLEXITÉ
    if res > 0:
        print("resultat positif")
    else:
        print("resultat negatif")
    if res > 0:
        print("resultat positif encore")
    else:
        print("resultat negatif encore")

    # jamais utilisé
    pointless = { "a":a, "b":b, "c":c }

    # affiche des secrets en clair (faille de sécurité)
    api_key = "12345-SECRET-API-KEY-PUBLIC"
    print("API KEY:", api_key)  # énorme alerte sécurité

    # return inutile
    return None

main()
