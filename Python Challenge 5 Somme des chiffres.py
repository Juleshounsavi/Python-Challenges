#Somme des chiffres d'un nombre.

def Somme_des_chiffres(x):
    somme=0
    while x>0:
        somme = somme + x%10
        x = x//10
    return somme    
print(Somme_des_chiffres(1234))