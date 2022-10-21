# maListe1 = ["Pierre","Hugo"]
# maListe2 = ["Anne","Marie"]
# maListe1.extend(maListe2)
# print(maListe1)
# maListe1.pop(1)
# print(maListe1)
#maListe1.pop() #supprimer le dernier élément de la liste

# laliste=["fraise", "banane", "orange", "cerise"]
# laliste.sort()
# print(laliste)
#
# laliste2 = [1, 3, 41, 2, 1293, 23]
# laliste2.sort()
# print(laliste2)
#
# laliste3 = laliste2.sort(reverse=True)
# print(laliste3)

# def myfunc(x):
#     return abs(x - 50)
#
# laliste = [100, 50, 65, 82, 23]
# laliste.sort(key = myfunc)
# print(laliste)

#attention à la casse, elle compte aussi sur sort

#faire une copie d'une liste
#
# laliste2 = [100, 50, 65, 82, 23]
# laliste2_bis = laliste2.copy()
# print(laliste2_bis)

#faire une jointure de liste
# liste1 = ["x", "y", "z"]
# liste2 = [1,2,3]
# liste3 = liste1 + liste2
# print(liste3)

#autre méthode
# liste1 = ["x", "y", "z"]
# liste2 = [1,2,3]
# for x in liste2:
#     liste1.append(x)
# print(liste1)

#méthode 3
# liste1 = ["x", "y", "z"]
# liste2 = [1,2,3]
# liste1.extend(liste2)
# print(liste1)

#vider la liste
# liste1 = ["x","y","z"]
# liste1.clear()
# print(liste1)

#Les tuples
# montuple = ("Pomme", "Kiwi", "Citron")
# print(montuple)
# print(type(montuple))
# print(len(montuple))

#créer un tuple avec un objet
# montuple = ("poire",) # tuple avec la , sinon un str
# print(type(montuple))

#On peut mélanger les types et avoir des tuples constitués de booléens,d e chaines, d'entiers etc...
#le tuple est une classe comme les autres types en python
#faire appel au constructeur du tuple

# montuple=tuple(("pomme", "poire", "kiwi"))
# print(montuple)
# print(montuple[1])
# print(montuple[-1])

# montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon", "Banane", "Fraise")
# print(montuple[2:5]) #5 exclu
#
# montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon", "Banane", "Fraise")
# print(montuple[:3]) #3 exclu
#
# montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon", "Banane", "Fraise")
# print(montuple[2:]) #jusqu'au 3eme élément
#
# montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon", "Banane", "Fraise")
# print(montuple[-4:-1])

# if "Citron" in montuple:
#     print("Oui il y a un Citron dans le panier")

#modification dans le tuple
# montuple = ("Pomme", "Kiwi", "Citron")
# a = list(montuple)
# a[1] = "Fraise"
# montuple = tuple(a)
# print(montuple)

# montuple = ("Pomme", "Kiwi", "Citron")
# a = list(montuple)
# a.append("Pastèque")
# montuple = tuple(a)
# print(montuple)

#ajouter un tuple à un tuple
# montuple = ("Pomme", "Kiwi", "Citron")
# a = ("Fraise",)
# montuple += a
# print(montuple)

#supprimer un élément
# montuple = ("Pomme", "Kiwi", "Citron")
# a = list(montuple)
# a.remove("Pomme")
# montuple = tuple(a)
# print(montuple)

#supprimer le tuple
# montuple = ("Pomme", "Kiwi", "Citron")
# del montuple
# print(montuple)

#récuperer les éléments du tuple dans des variables
# montuple = ("Pomme", "Kiwi", "Citron", "Pommme")
# (a,b,*c) = montuple #* = liste
# print(a)
# print(b)
# print(c)

# montuple = ("Pomme", "Kiwi", "Citron" )
# for x in montuple:
#     print(x)

#Parcourir un tuple en utilisant le numéri d'index et la longueur du tuple (len, range et une boucle for ?)
# montuple = ("Pomme", "Kiwi", "Citron", "Fraise")
# for x in range(len(montuple)):
#     print(montuple[x])

# x=0
# while x<len(montuple):
#     print(montuple[x])
#     x += 1

# montuple1 = ("Pomme", "Kiwi", "Citron")
# montuple2 = (4, 16, 12)
# montuple3 = montuple1 + montuple2
# print(montuple3)
# montuple4 = montuple1 * 1000
# print(montuple4)


# import code
# OU
# import importlib
# file = importlib.import_module("Code")
# obj = file.Codeclass()
# obj.show()
# OU
# from Code import CodeClass
# var1 = CodeClass()
# var1.show()