import mylibrary as ml

def forward_backaward_substitution(mat_L, mat_U, vec_B):

    #initialize two vectors to store the solution
    x = [0] * len(mat_U[0])
    y = [0] * len(mat_L[0])
    
    #forward substitution    
    for i in range(len(mat_L)):
        sum = 0
        for j in range(i):
            sum += mat_L[i][j]*y[j]
        y[i] = vec_B[i] - sum

    #backward substitution (loop should run in reverse)
    for i in reversed(range(len(mat_U))):
        sum = 0
        for j in reversed(range(i, len(mat_U[0]))):
            sum += mat_U[i][j]*x[j]
        x[i] = (y[i] - sum)/mat_U[i][i]

    return x

def LU_decomposition(mat_A):

    n = len(mat_A)

    #initialize empty matrix to store decomposed matrices
    L = [[0 for x in range(n)] for y in range(n)] 
    U = [[0 for x in range(n)] for y in range(n)]

    #loop through every columns of A 
    for i in range(len(mat_A)):

        #Diagonal entries of L matrix are all 1
        L[i][i] = 1

        #Upper triangular matrix
        for k in range(i, len(mat_A[0])):
            sum = 0
            for j in range(i): 
                sum += (L[i][j] * U[j][k])
  
            U[i][k] = mat_A[i][k] - sum

        #Lower triangular matrix
        for k in range(i+1, len(mat_A[0])):             
            sum = 0 
            for j in range(i): 
                sum += (L[k][j] * U[j][i]) 
            
            #The order of element is reversed from i,k to k,i
            L[k][i] = (mat_A[k][i] - sum) / U[i][i] 
  
    return L,U

def check_inverse(mat_U):
    #initialize variable to store determinant
    det = 1
    for i in range(len(mat_U)):
        det = det*mat_U[i][i]

    #raise error if determinant is zero, return False
    if det == 0:
        raise Warning("Inverse of the matrix does not exist")
        return False
    
    else:
        return True


def matrix_inverse(mat_A):

    n = len(mat_A)

    #initialize empty matrix to store inverse
    inverse_mat = [[0 for x in range(n)] for y in range(n)] 

    #Decompose the matrix
    L,U = LU_decomposition(mat_A)

    #Check if the inverse exist
    if check_inverse(U) == True:

        for i in range(n):

            #initialize vector with ith value 1, rest 0
            B = [0 for x in range(n)]
            B[i] = 1

            column = forward_backaward_substitution(L, U, B)

            #Store the solution column wise
            for j in range(n):
                inverse_mat[j][i] = round(column[j], 3)

        return inverse_mat

    else:
        return None


#load the matrix
mat_A = ml.load_matrix('q2.txt')
mat_A = ml.partial_pivot(mat_A)

print("Matrix A is:")
ml.print_matrix(mat_A)

#call the inverse function
inv = matrix_inverse(mat_A)

print("Inverse of matrix A is:")
ml.print_matrix(inv)

'''
Output
Matrix A is:
[3, 7, 1, 0]
[0, 2, 8, 6]
[0, 0, 1, 2]
[0, 1, 0, 1]
Inverse of matrix A is:
[0.333, -0.25, 1.667, -1.833]
[0.0, 0.083, -0.667, 0.833]
[0.0, 0.167, -0.333, -0.333]
[0.0, -0.083, 0.667, 0.167]
'''