vec_A = [1,2,3]

with open("m.txt", 'r' ) as f:
    mat_M = [[int(num) for num in row.split(' ')] for row in f]
with open("n.txt", 'r' ) as f:
    mat_N = [[int(num) for num in row.split(' ')] for row in f]


print("Vector A is", vec_A)
print("Marix M is: ")
for i in mat_M:
    print(i)
print("Matrix N is: ")
for i in mat_N:
    print(i)

# Matrix operation on vector 
vec_B = [0,0,0]

for i in range(len(mat_M)):
    for j in range(len(mat_M[i])):
        vec_B[i] += mat_M[i][j]*vec_A[j]

print("The vector B = M x A =", vec_B)


# Product of matrix
mat_C = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(mat_M)):
    for j in range(len(mat_N)):
        for k in range(len(mat_N[j])):
            mat_C[i][j] += mat_N[k][j] * mat_M[i][k]

print("Matrix C = M x N is: ")
for i in mat_C:
    print(i)

'''
Output
Vector A is [1, 2, 3]
Marix M is:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
Matrix N is:
[2, 1, 1]
[1, 2, 1]
[1, 1, 2]
The vector B = M x A = [14, 32, 50]
Matrix C = M x N is:
[7, 8, 9]
[19, 20, 21]
[31, 32, 33]
'''