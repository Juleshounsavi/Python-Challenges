#A function that print the second largest number of a list.

def Second_large_number_finder(liste):    
    x = max(liste)
    liste.remove(x)
    y = max(liste)
    print("The second largest number is: {}".format(y))


li = [10, 20, 5]
Second_large_number_finder(li)
