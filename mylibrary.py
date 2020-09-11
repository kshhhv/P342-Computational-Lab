def vector_sum(vec_A, vec_B):
    if len(vec_A) == len(vec_B):
        dim = len(vec_A)
    else:
        raise IndexError("Length of vectors are not same.")
    
    add = []
    for i in range(dim):
        add.append(vec_A[i] + vec_B[i])

    return add

def vector_product(vec_A, vec_B):
    if len(vec_A) == len(vec_B):
        dim = len(vec_A)
    else:
        raise IndexError("Length of vectors are not same.")

    in_pro = 0
    for i in range(dim):
        in_pro += vec_A[i]*vec_B[i]

    return in_pro

def load_matrix(file):
    with open(file, 'r' ) as f:
        mat_M = [[int(num) for num in row.split(' ')] for row in f]
    return mat_M

def print_matrix(mat_M):
    for i in mat_M:
        print(i)

def matrix_operation(mat_M, vec_A):
    if len(mat_M[0]) != len(vec_A):
        raise IndexError("Columns of matrix is not equal to vector elements.")

    vec_B = [0,0,0]
    for i in range(len(mat_M)):
        for j in range(len(mat_M[i])):
            vec_B[i] += mat_M[i][j]*vec_A[j]
    return vec_B

def matrix_product(mat_M, mat_N):
    if len(mat_M[0]) != len(mat_N):
        raise IndexError("Columns of first matrix is not equal to rows of second matrix.")

    mat_C = []
    for i in range(len(mat_M)):
        row = []
        for j in range(len(mat_M[0])):
            element = 0
            for k in range(len(mat_N[j])):
                element += mat_N[k][j] * mat_M[i][k]
            row.append(element)
        mat_C.append(row)

    return mat_C


def partial_pivot(mat_M, mat_N = None):
    n = len(mat_M)
    for r in range(n-1):
        if mat_M[r][r] == 0:
            for r1 in range(r+1,n):
                if mat_M[r1][r] > mat_M[r][r]:
                    mat_M[r], mat_M[r1] = mat_M[r1], mat_M[r]
                    if mat_N == None:
                    	continue
                    mat_N[r], mat_N[r1] = mat_N[r1], mat_N[r]

    if mat_N == None:
    	return mat_M
    	
    return mat_M, mat_N

def gauss_jordan(mat_M, mat_N):
    n = len(mat_M)
    #do partial pivoting
    partial_pivot(mat_M, mat_N)

    for r in range(n):
        #make the diagonal element 1
        pivot = mat_M[r][r]
        for c in range(r,n):
            mat_M[r][c] = mat_M[r][c]/pivot
        if type(mat_N[0]) == list:
            for k in range(n):
                mat_N[r][k] = mat_N[r][k]/pivot
        else:
            mat_N[r] = mat_N[r]/pivot

        #make the other element in that column 0
        for r1 in range(n):
            #nothing to do for the diagonal element or if it already is 0
            if (r1 == r) or (mat_M[r1][r] == 0):
                continue
            else:
                factor = mat_M[r1][r]
                for c in range(r,n):
                    mat_M[r1][c] = mat_M[r1][c] - factor*mat_M[r][c]
                if type(mat_N[0]) == list:
                    for l in range(n):
                        mat_N[r1][l] = mat_N[r1][l] - factor*mat_N[r][l]
                else:
                    mat_N[r1] = mat_N[r1] - factor*mat_N[r]
    return mat_N


