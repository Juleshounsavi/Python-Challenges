#A function that print the second largest number of a list.

def Second_large_number_finder(liste):    
    liste_cp = liste.copy()
    x = max(liste_cp)
    liste.remove(x)
    y = max(liste_cp)
    print("The second largest number is: {}".format(y))


li = [10, 20, 5]
Second_large_number_finder(li)
