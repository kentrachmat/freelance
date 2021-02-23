#1. Plus petit, plus grand

def plus_grand(nombre1, nombre2) :
    if nombre1 != nombre2 :
        print(max(nombre1, nombre2))
    else :
        print("Ils sont égaux !")
    
#plus_grand(6,6)
#plus_grand(6,8)
        
        
# 2. Monnaie
system = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

# il y a un soucis de précision avec les floats <= 0.02, j'ai fait au mieux
def rendu_monnaie(montant, systeme) :
    n = len(systeme)
    rendu = [0] * n 
    for i in range(n):
        while montant >= systeme[i]: 
            montant -= system[i] 
            rendu[i] += 1
            if montant == 0.019999999999981796 or montant == 0.019999999999963606 :
                montant = 0.02
            if montant == 0.009999999999990891 or montant == 0.0099999999999727 :
                montant = 0.01
            print(montant)
    phrase = ""
    for x in range(len(rendu)) :
        if rendu[x] > 0 :
            if systeme[x] >= 5 :
                phrase += str(rendu[x]) + " billet(s) de " + str(systeme[x]) + "\n"
            if systeme[x] < 5 :
                phrase += str(rendu[x]) + " pièce(s) de " + str(systeme[x]) + "\n"
    print(phrase)
    return rendu
        

#rendu_monnaie(1066.79, system)

# 3. Calcul de l'IMC
from decimal import Decimal

def status_imc(masse, taille) :
    indice = masse / taille**2
    if indice >= 40 :
        print("obésité morbide ou massive")
    elif indice >= 35 :
        print("obésité sévère")
    elif indice >= 30 :
        print("obésité modérée")
    elif indice >= 25 :
        print("surpoids")
    elif indice >= 18.5 :
        print("poids normal")
    elif indice >= 16.5 :
        print("maigreur")
    elif indice < 16.5 :
        print("dénutrition ou anorexie")
        
#status_imc(75, 1.85)    
#status_imc(55, 1.80)
        
# 4. Echelle de beaufort

def beaufort(vitesse) :
    if vitesse >= 188 :
        print("Ouragan ou bombe météorologique")
    elif vitesse >= 103 :
        print("Violente tempête")
    elif vitesse >= 89 :
        print("Tempête")
    elif vitesse >= 75 :
        print("Fort coup de vent")
    elif vitesse >= 62 :
        print("Coup de vent")
    elif vitesse >= 50 :
        print("Grand frais")
    elif vitesse >= 39 :
        print("Vent frais")
    elif vitesse >= 29 :
        print("Bonne Brise")
    elif vitesse >= 20 :
        print("Jolie brise")
    elif vitesse >= 12 :
        print("petite brise")
    elif vitesse >= 6 :
        print("Légère brise")
    elif vitesse >= 1:
        print("Très légère brise")
    elif vitesse < 1 :
        print("Calme")
        
#beaufort(75)