#A function that display the transposition of a matrix given by the user.

def Transpo(A, row, col):
    B = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            B[j][i] = A[i][j]
    print("Affichage de ma matrice A:")
    for li in A:
        print(li)
    print("\nAffichage de ma matrice B transposee de A:")
    for li in B:
        print(li)  

"""
#Example:
Mat = [[1, 2, 3], 
       [4, 5, 6]]
Transpo(Mat, 2, 3)
"""
