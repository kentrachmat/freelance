class Machine :
    menthe = False
    cassis = False
    systeme = [1, 0.5, 0.2, 0.1]

    def __init__(self) :
        self.menthe = False
        self.cassis = False
        self.systeme = [1, 0.5, 0.2, 0.1]
    
    def get_menthe(self) :
        return self.menthe

    def get_cassis(self) :
        return self.cassis
    
    def get_systeme(self) :
        return self.systeme

    def appuyer_bouton(self, boisson) :
        # il faut inserer soit "MENTHE" soit "CASSIS"
        if boisson == "MENTHE" :
            self.menthe = not self.menthe
        if boisson == "CASSIS" :
            self.cassis = not self.cassis

    def servir(self, montant) :
        # montant est une liste de 4 valeurs

        print("Warning : veillez à n'avoir enfoncé qu'un seul bouton")
        print("Si vous n'inserez pas de piece de 0.50, ni de 1, je ne rends pas la monnaie")
        print("Si vous inserez plus de 2.20 euros avec au moins une piece de 0.50 ou de 1 euro, je rends 1.80 euros")

        somme = 0
        for element in montant :
            somme += element
        print("Vous avez introduit " + str(somme) + " euros")

        if (0.5 in montant or 1 in montant) and (not self.get_cassis() and not self.get_menthe()) :
            print("Pas de boisson demandee, je rends la monnaie introduite")
            return montant
        
        if (0.5 in montant or 1 in montant) and (self.get_cassis() and self.get_menthe()) :
            print("Plusieurs boissons en meme temps impossible, je rends la monnaie introduite")
            return montant

        prix = 0
        rendu = [0, 0, 0, 0]
        monnaies = self.get_systeme()
        boisson = ""
        if self.get_menthe() and not self.get_cassis() :
            prix = 0.2
            boisson = "MENTHE"

        if not self.get_menthe() and self.get_cassis() :
            prix = 0.4
            boisson = "CASSIS"
        if (0.5 in montant or 1 in montant) and somme < prix :
            print("Montant insuffisant, je rends la monnaie")
            return montant

        if somme > prix and somme <= 2.2:
            print("Vous avez choisi " + boisson)
            fin = somme - prix
            somme -= prix
            for i in range(len(monnaies)) :
                if monnaies[i]  <= somme + 0.001:
                    rendu[i] += 1
                    somme -= monnaies[i]
            for p in range(len(rendu)) :
                if p == 0 :
                    print("je rends " + str(rendu[p]) + " piece de 1 euro.")
                if p == 1 :
                    print("je rends " + str(rendu[p]) + " piece de 0.50 euro.")
                if p == 2 :
                    print("je rends " + str(rendu[p]) + " piece de 0.20 euro.")
                if p == 3 :
                    print("je rends " + str(rendu[p]) + " piece de 0.10 euro.")
            print("Je vous rends " + str(fin))
            print(rendu)
            return rendu

        if somme > 2.2 and (0.5 in montant or 1 in montant) :
            print("Je rends une piece de chaque, soit 1.80 euros")
            print([1, 1, 1, 1])
            return [1, 1, 1, 1]

Distributeur = Machine()

Distributeur.appuyer_bouton("CASSIS")

Distributeur.servir([0, 0.9, 0, 0])


