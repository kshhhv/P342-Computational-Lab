vec_A = [1,2,3]
vec_B = [2,4,6]

print("First vector is ", vec_A)
print("Second vector is ", vec_B)


dim = len(vec_A)

# Vector addition
add = []
for i in range(dim):
	add.append(vec_A[i] + vec_B[i])

print("The sum vector is ", add)

# Inner product of vectors
in_pro = 0
for i in range(dim):
	pro = vec_A[i]*vec_B[i]
	in_pro += pro

print("The dot product is", in_pro)

