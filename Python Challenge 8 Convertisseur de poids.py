#Un programme qui fait la conversion des poids du kg au mg.
poids=float(input("Entrer le poids que vous aimerez convertir:"))
unite_av=str(input("Enter l'unite de votre poids, sous la forme: 'kg', 'hg','dag','g','dg','cg','mg'."))
unite_ap=str(input("Enter l'unite vers laquelle vous voulez convertir votre poids, sous la forme: 'kg', 'hg','dag','g','dg','cg','mg'."))

conversion_en_g = {
        'kg': 1000,
        'hg': 100,
        'dag': 10,
        'g': 1,
        'dg': 0.1,
        'cg': 0.01,
        'mg': 0.001
    }
if unite_av not in conversion_en_g or unite_ap not in conversion_en_g:
    raise ValueError("Unités non reconnues. Utilisez 'kg', 'hg', 'dag', 'g', 'dg', 'cg' ou 'mg'.")
    

valeur_en_g = poids * conversion_en_g[unite_av]
valeur_finale = valeur_en_g / conversion_en_g[unite_ap]

print("Valeur finale: {}".format(valeur_finale))