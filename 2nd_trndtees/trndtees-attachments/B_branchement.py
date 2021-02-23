# 1 IMPRESSION

# 1.

def add_carre(x, y) :
    resultat = (x**2 + y**2)/(x + y)
    print(resultat)
    return resultat

# add_carre(3,4)

# 2.

def sum_par_diff(x, y) :
    """
    La fonction va diviser la somme de ses paramètres par la différences de ces derniers
        
        Parameters :
            x (int or float) : a number
            y (int or float) : another number
            
        Return :
            res (int or float) : the result of the calculus, if x != y    
        
    """
    if x != y :
        res = (x + y) / (x - y)
        print(res)
        return res
    else :
        print ("Division par zéro : x et y sont les meme, calcul impossible")

#sum_par_diff(3,4)

# 3.
# La question ici n'est pas claire

# Dans le cas où on veut savoir si la somme est inferieure ou egale au produit :
def is_sum_sup_prod(x, y) :
    res = ((x + y) <= (x * y))
    print(res)
    return res

#is_sum_sup_prod(3, 4)
# Dans le cas où la somme est inférieure ou égale au produit, et qu'on veut le résultat de la somme et du produit:

def sum_sup_prod(x, y) :
    if (x + y) <= (x * y) :
        somme = x + y
        produit = x * y
        print("La somme vaut : " + str(somme) + " et le produit vaut : " + str(produit))
    return somme, produit

#sum_sup_prod(3,4) 

# 2 ECHANGE

"""
Pseudo-code :
ECRIRE premiere variable et sa valeur
ECRIRE deuxieme variable et sa valeur
ECRIRE troisieme variable avec la meme valeur que la premiere
DONNER la premiere variable la valeur de la deuxieme
DONNER la deuxieme variable la valeur de la 3eme

"""

# code :

v1 = 10
v2 = 3
print(v1,v2)
v_change = 10
v1 = v2
v2 = v_change
print(v1,v2)