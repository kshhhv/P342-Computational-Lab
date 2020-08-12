size = int(input("Enter the size of grid"))
points = []

for m in range(size):
	for n in range(size):
		points.append([m,n])
		n += 1
	m += 1

sum = 0
pairs = 0
print("List is", points)
tot_points = len(points)

for i in range(tot_points):
	print("From the point ", points[i])
	x1,y1 = points[i]
	for j in range(i+1, tot_points):
		x2,y2 = points[j]
		distance = abs(x2 - x1) + abs(y2 - y1)
		print("Distance: ", distance)
		sum += distance
		pairs += 1

print("Sum is", sum)
print("Pair is", pairs)

avg_dist = sum/pairs
print("The average distance between two points is ", avg_dist)