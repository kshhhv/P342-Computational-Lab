A = [1,2,3]
B = [2,4,6]

dim = len(A)

# Vector addition
add = []
for i in range(dim):
	add.append(A[i] + B[i])

print("The new vector is ", add)

# Inner product of vectors
in_pro = 0
for i in range(dim):
	pro = A[i]*B[i]
	in_pro += pro

print("The dot product is", in_pro)

