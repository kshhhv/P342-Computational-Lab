'''
Write a Gauss Jordan code with partial pivoting and solve the follow problems –

Q3.Find the inverse of the matrix (FYI inverse exists) and check A A-1 = I :
          1   -3    7
    A =  -1    4   -7
         -1    3   -6
'''

def par_pivot(mat_M, b):
    n = len(mat_M)
    for r in range(n-1):
        if mat_M[r][r] == 0:
            for r1 in range(r+1,n):
                if mat_M[r1][r] > mat_M[r][r]:
                    mat_M[r], mat_M[r1] = mat_M[r1], mat_M[r]
                    b[r], b[r1] = b[r1], b[r]


def gauss_jordan(mat_M, b):
    n = len(mat_M)
    #do partial pivoting
    par_pivot(mat_M, b)

    for r in range(n):
        #make the diagonal element 1
        pivot = mat_M[r][r]
        for c in range(r,n):
            mat_M[r][c] = mat_M[r][c]/pivot
        for k in range(n):
            b[r][k] = b[r][k]/pivot

        #make the other element in that column 0
        for r1 in range(n):
            #nothing to do for the diagonal element or if it already is 0
            if (r1 == r) or (mat_M[r1][r] == 0):
                continue
            else:
                factor = mat_M[r1][r]
                for c in range(r,n):
                    mat_M[r1][c] = mat_M[r1][c] - factor*mat_M[r][c]
                for l in range(n):
                    b[r1][l] = b[r1][l] - factor*b[r][l]

def mat_prod(mat_A, mat_B):
    mat_C = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(mat_A)):
        for j in range(len(mat_B)):
            for k in range(len(mat_B[j])):
                mat_C[i][j] += mat_B[k][j] * mat_A[i][k]
    return mat_C


with open("q3.txt", 'r' ) as f:
    mat_M = [[int(num) for num in row.split(' ')] for row in f]

with open("q3.txt", 'r' ) as f:
    matrix_M = [[int(num) for num in row.split(' ')] for row in f]


b = [[1,0,0],[0,1,0],[0,0,1]]

gauss_jordan(mat_M, b)

print("Inverse of the given matrix is: ")
for row in b:
    print(row)

product = mat_prod(matrix_M, b)
print("The matrix product with its inverse is: ")
for row in product:
    print(row)

'''
Output:
Inverse of the given matrix is:
[-3.0, 3.0, -7.0]
[1.0, 1.0, 0.0]
[1.0, 0.0, 1.0]
'''