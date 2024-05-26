#Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.

def convert(list):
    new=[]
    for i in list:
        new.append(str(i))
    return new

li=[1,2,3]
print("list: {}.\nConvert list: {}.".format(li, convert(li)))