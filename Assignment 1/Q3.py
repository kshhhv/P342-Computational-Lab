#Sum over 1+1/2+1/3+... till the sume does not change by more than 0.001

sum = 0
n = 1
add = 1/n

while (add > 0.001):
	add = 1/n
	sum += add
	n += 1

print("The sum is", sum)