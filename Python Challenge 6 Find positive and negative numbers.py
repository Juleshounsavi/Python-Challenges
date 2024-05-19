#A function that print the n=positive and the negative numbers separately from a list

def Find_Positive_and_Negative_Num(liste):
    Positive=[]
    Negative=[]
    for x in liste:
        if x>0:
            Positive.append(x)
        else:
            Negative.append(x)
    print("Here are the {} positive numbers in the list:".format(len(Positive))) 
    print(Positive)
    print("Here are the {} negative numbers in the list:".format(len(Positive)))
    print(Negative)       
    
ls=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]    
Find_Positive_and_Negative_Num(ls) 
