#Fibonacci series
#Enter an integer greter or equal to 2
def Fibonnacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonnacci(n-1) + Fibonnacci(n-2)

print(Fibonnacci(0))