import random


def exo1():
    prenom = "Pierre"
    age = 20
    majeur = True
    compte_en_banque = 20135.384
    amis = ["Marie", "Julien", "Adrien"]
    parents = ("Marc", "Caroline")

    print(prenom)
    print(age)
    print(majeur)
    print(compte_en_banque)
    print(amis)
    print(parents)


def exo2():
    a = str(15)
    print("Le nombre est " + a)

def exo3():
    a = 2
    b = 6
    c = 3
    print(f"{a} + {b} + {c}")
    """
    OU 
    print(a, b, c, sep=" + ")
    """

def exo4():
    list1 = range(3)
    list2 = range(5)

    print(list(list2))

def exo5():
    a = str("Pierre")
    while type(a) == str:
        print("La variable a est une chaîne de caractère")
        a = int(0)
    print("Fin")

    """
    OU
    if isinstance(item, str):
        print(item + " is a string.")
    firstName = 'Pierre';
    checkIfItemIsString(firstName);
    firstName = 0;
    checkIfItemIsString(firstName);
    """
def exo6():
    phrase = "Bonjour"
    nouvelle_phrase = phrase.replace("Bonjour", "Bonsoir")
    print(nouvelle_phrase)

def exo7():
    chaine = "Pierre, Julien, Anne, Marie, Lucien"
    chaine_liste = chaine.split(", ")
    chaine_liste.sort()
    chaine_en_ordre = ", ".join(chaine_liste)
    print(chaine_en_ordre)

def exo_8():
    phrase = "Bonjour tout le monde. Je répéte Bonjour"
    newPhrase = phrase.replace("Bonjour", "Bonsoir", 1)
    print(newPhrase)
#exo_8()

def exo_9():
    chaine = "Pierre, Julien, Anne, Marie, Lucien"
    chaine_split = chaine.split(', ')
    chaine_split.sort()
    print(chaine_split)

# maListe1 = ["Pierre","Hugo"]
# maListe2 = ["Anne","Marie"]
# maListe1.extend(maListe2)
# print(maListe1)
# maListe1.pop(1)
# print(maListe1)
#maListe1.pop() #supprimer le dernier élément de la liste

def exo_10():
    Ma_spehre_rayon = float(input('Quel est le rayon de votre sphere en cm : '))
    #Volume_sphere = (4(math.pi)/3)Ma_spehre_rayon**3
    print('Le volume de votre sphere de ', Ma_spehre_rayon, 'centimétre est de : ',Volume_sphere,' centimétre cube')

def exo_11():
    try:
        P_Nombre= int(input('Veuillez entrez un nombre pour le comparer : '))
    except:
        print('Veuillez entrez un nombre !')
        exo_11()
    if P_Nombre > 10:
            print('Votre nombre est supérieur a 10 ! ')
    elif P_Nombre ==10 :
            print('Votre nombre est égal a 10 !')
    elif P_Nombre <10 :
            print('Votre nombre est inférieur a 10 !')


#Exercice Bonus
#Construire un code qui affiche une liste des nombre pairs de 1 à 100
def Afficher_Nombre_Pair():
    Liste_Pair = []
    x = 1
    while x < 101:
        if x % 2 == 0:
            Liste_Pair.append(x)
        x = x + 1
    print(Liste_Pair)

    #OU liste_nombres_pairs = range(2, 101, 2)
    #print(list(liste_nombres_pairs))

#Afficher_Nombre_Pair()

#Construire un code qui affiche le lancé de 6 dés aléatoire
def Lance_De_Des_Aleatoire():
    #import random déjà réalisé
    Ma_Liste_De_Des = []
    x = 0
    while x<6:
        Ma_Liste_De_Des.append(random.randrange(1,7))
        x += 1
    print(Ma_Liste_De_Des)

#Lance_De_Des_Aleatoire()

#Construire un code qui génère un nombre de lancé de dés choisi par l'utilisateur et
#afficher la moyenne en flottant de l'ensemble de ces lancés
def Lance_De_Des_Aleatoire_User():
    Nombre_De_Lances = int(input("Combien de lancés voulez-vous avoir ?"))
    Ma_Liste_De_Des = []
    i = 0
    Moyenne = 0
    while i < Nombre_De_Lances :
        Ma_Liste_De_Des.append(random.randrange(1,7))
        Moyenne += Ma_Liste_De_Des[i]
        i += 1
    Moyenne = Moyenne / Nombre_De_Lances
    print(Ma_Liste_De_Des)
    print(Moyenne)

#Lance_De_Des_Aleatoire_User()

def Compteur_Occurence_Lettre():
    Phrase = input("Saisissez votre texte ")
    Lettre = input("Quelle lettre voulez vous compter ? ")
    Compteur = 0
    if (len(list(Lettre))) < 2:
        i = 0
        while i < len(list(Phrase)):
            if Phrase[i] == Lettre or Phrase[i] == Lettre.upper():
                Compteur += 1
            i += 1
        print(f"Il y a {Compteur} de lettre {Lettre} dans votre texte")
    else:
        print("Désolé, vous avez rentré une valeur incorrecte")

    #OU lettre = "a"
    #phrase ="Salut ça va ?"
    #print(phrase.lower().count(lettre))

def Compteur_Occurence_Lettre_V2()



