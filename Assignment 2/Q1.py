size = int(input("How many points to consider?"))
points = []

for n in range(size):
	points.append(n)
	n += 1

sum = 0
pairs = 0

print("List is", points)

for i in points:
	print("i is", i)
	for j in points[i+1:]:
		print("j is", j)
		distance = j - i
		sum += distance
		pairs += 1

avg_dist = sum/pairs

print("The average distance between two points is ", avg_dist)