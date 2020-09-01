'''
Write a Gauss Jordan code with partial pivoting and solve the follow problems –

Q1. Solve :
    x + 3y + 2z = 2
    2x + 7y + 7z = -1
    2x + 5y + 2z = 7
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
        b[r] = b[r]/pivot

        #make the other element in that column 0
        for r1 in range(n):
            #nothing to do for the diagonal element or if it already is 0
            if (r1 == r) or (mat_M[r1][r] == 0):
                continue
            else:
                factor = mat_M[r1][r]
                for c in range(r,n):
                    mat_M[r1][c] = mat_M[r1][c] - factor*mat_M[r][c]
                b[r1] = b[r1] - factor*b[r]

with open("q1.txt", 'r' ) as f:
    mat_M = [[int(num) for num in row.split(' ')] for row in f]

b = [2, -1, 7]

gauss_jordan(mat_M, b)

print("The solution of given system of linear equation is: ")
print("x = {} ; y = {}; z = {}".format(b[0], b[1], b[2]))


'''
Output:
The solution of given system of linear equation is:
x = 3.0 ; y = 1.0; z = -2.0
'''