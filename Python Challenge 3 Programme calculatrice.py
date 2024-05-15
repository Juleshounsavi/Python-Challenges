#Simple calcutor with python.

a=int(input("Entrer le premier nombre:"))
b=int(input("Entrer le second nombre:"))
operator=str(input("Choisis un operateur entre '+', '-', '*', '/':"))
if operator == '+':
    print("La somme de {} et {} est: {}.".format(a, b, a+b))
elif operator == '-':
    print("La soustraction de {} dand {} est: {}.".format(b, a, a-b))
elif operator == '*':
    print("La multiplication de {} et {} est: {}.".format(a, b, a*b))
elif operator == '/':
    print("La division de {} par {} est: {}.".format(a, b, a/b))
                
