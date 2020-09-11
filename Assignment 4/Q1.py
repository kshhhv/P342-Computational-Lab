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
        for k in range(i, len(mat_A[0])):             
            sum = 0 
            for j in range(i): 
                sum += (L[k][j] * U[j][i]) 
  			#The order of element is reversed from i,k to k,i
            L[k][i] = (mat_A[k][i] - sum) / U[i][i] 
  
    return L,U

#Load the matrix
mat_A = ml.load_matrix('a.txt')
#Declare the RHS vector
B = [6, -3, -2, 0]

print("Matrix A is:")
ml.print_matrix(mat_A)
print("Vector B is: ", B)

#Call decomposition function
L,U = LU_decomposition(mat_A)
print("Matrix L is:")
ml.print_matrix(L)
print("Matrix U is:")
ml.print_matrix(U)

#Pass the decomposed value to substitution function
sol = forward_backaward_substitution(L,U,B)
print("Solution vector is:", sol)

'''
Output:
Matrix A is:
[1, 0, 1, 2]
[0, 1, -2, 0]
[1, 2, -1, 0]
[2, 1, 3, -2]
Vector B is:  [6, -3, -2, 0]
Matrix L is:
[1.0, 0, 0, 0]
[0.0, 1.0, 0, 0]
[1.0, 2.0, 1.0, 0]
[2.0, 1.0, 1.5, 1.0]
Matrix U is:
[1, 0, 1, 2]
[0, 1.0, -2.0, 0.0]
[0, 0, 2.0, -2.0]
[0, 0, 0, -3.0]
Solution vector is: [1.0, -1.0, 1.0, 2.0]
'''

