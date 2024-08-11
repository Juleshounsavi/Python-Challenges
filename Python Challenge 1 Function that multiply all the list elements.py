#Fonction which multiply all the numbers of a list.

n=int(input("Enter the lengh of your list:"))
liste = []

for i in range(0, n):
    x=int(input(("Enter element:")))
    liste.append(x)
print(liste) 

def MultiplyListeElements(liste_x):
    result=1
    for i in liste_x:
        result=result*i
    return result  

print(MultiplyListeElements(liste))    
    
    
    
