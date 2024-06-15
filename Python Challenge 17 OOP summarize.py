#Resumé Python OOP.

"""
-Classe : Un modèle définissant la structure et le comportement des objets. Elle encapsule les données (attributs) et les fonctions (méthodes) qui opèrent sur ces données.
-Objet : Une instance d'une classe. Chaque objet a son propre ensemble de données, défini par la classe.

"""
#Definition globale de la classe.
class NomDeClasse:
    def __init__(self, param1, param2):  #
        self.attribut1 = param1
        self.attribut2 = param2
    
    def methode(self):
        #opérations sur les attributs
        pass

valeur1 = 0
valeur2 = 0

#Creation d'un objet.
objet = NomDeClasse(valeur1, valeur2)

#Notion d'heritage.
class ClasseDeBase:
    #code de la classe de base
    pass
class ClasseDerivee(ClasseDeBase):
    #code supplémentaire pour la classe dérivée
    pass


#Exempe pratique.
class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
    
    def afficher_info(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}")

    def autre_fonction(self, param1, param2):
        pass


voiture1 = Voiture("Toyota", "Corolla")
voiture1.afficher_info()  #Sortie: Marque: Toyota, Modèle: Corolla


#Exemple d'héritage.
class Animal:
    def __init__(self, nom):
        self.nom = nom
    
    def parler(self):
        pass  #méthode abstraite

class Chien(Animal):
    def parler(self):
        print(f"{self.nom} dit Woof!")

chien1 = Chien("Rex")
chien1.parler()  #Sortie: Rex dit Woof!

