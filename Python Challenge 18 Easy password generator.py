#A function that generate eight random integers stored in a list.
import random

def EasyGenerate():
    passw = []
    for i in range(0,8):
        passw.append(str(random.randint(0,9)))
    return passw
    
one = EasyGenerate()
two = EasyGenerate()

print(one)
print(two)
