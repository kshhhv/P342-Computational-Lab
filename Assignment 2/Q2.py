vec_A = [1,2,3]
vec_B = [2,4,6]

print("First vector is", vec_A)
print("Second vector is", vec_B)


dim = len(vec_A)

# Vector addition
add = []
for i in range(dim):
	add.append(vec_A[i] + vec_B[i])

print("The vector sum is", add)

# Inner product of vectors
in_pro = 0
for i in range(dim):
	in_pro += vec_A[i]*vec_B[i]

print("The dot product is", in_pro)

'''
Output:
First vector is [1, 2, 3]
Second vector is [2, 4, 6]
The vector sum is [3, 6, 9]
The dot product is 28
'''