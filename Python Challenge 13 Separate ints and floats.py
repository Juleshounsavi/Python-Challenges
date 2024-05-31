#A function that receive a list of ints and floats and then separate them into two different lists, one for ints and one for floats.

def separate_int_float(liste):
    liste_int = []
    liste_float = []
    for i in liste:
        if isinstance(i, int):
            liste_int.append(i)
        elif isinstance(i, float):
            liste_float.append(i)
    print("Here are the integers: {}.".format(liste_int))
    print("Here are the floats: {}.".format(liste_float))

ls = [1,2,3,4,5,3.4, 5.5, 6.7, 2, 3, 4, 0.55, 9.78]
separate_int_float(ls)
