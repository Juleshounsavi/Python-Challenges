#A function that count and return the unique values from a list

def NuniqueCounter(liste):
    unique=[]
    counter=0
    for i in liste:
        if i not in unique:
            counter=counter+1
            unique.append(i)      
    print("We have {} unique number in the list. Here they are:{}".format(counter, unique))    


l=[1,2,3,1,1,1,2,3,4,4,5,3,2,4,5,7,8,9,8,7,7,6,5,4,3,2,2,2,3,4,5,5,6,6]
NuniqueCounter(l)        