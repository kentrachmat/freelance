# 1 Somme

def a100() :
    somme = 0
    for n in range(1,101) :
        somme += n
    return somme

#print(a100()) # Le résultat est 5050

# 2 Somme paire

def sum_paire() :
    somme = 0
    for n in range(1,101) :
        if n % 2 == 0 :
            somme += n
    return somme

#print(sum_paire()) # Le résultat est 2550

# 3. Somme table de 7

def somme_tab7() :
    somme = 0
    for n in range(1, 11) :
        somme += n * 7
    return somme

#print(somme_tab7()) # Le résultat est 385

# 4. Tables de multiplication

def table10() :
    for x in range(1, 11) :
        for y in range(1, 11) :
            print(str(x) + " * " + str(y) + " = " + str(x * y))

#table10()

# 5. Horloge digitale

def horloge() :
    for h in range(24) :
        for m in range(60) :
            for s in range(60) :
                print(str(h) + " : " + str(m) + " : " + str(s))

#horloge()

# 6. Nombre premier

def est_premier(x) :
    for k in range(2, x) :
        if x % k == 0 :
            print(False)
            return False
    print(True)
    return True
    
# est_premier(1879) # 1879 donne True, par exemple