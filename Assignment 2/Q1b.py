size = int(input("Enter the size of grid: "))
points = []

for m in range(size):
	for n in range(size):
		points.append([m,n])
		n += 1
	m += 1

sum = 0
pairs = size**4

tot_points = len(points)

for i in range(tot_points):
	x1,y1 = points[i]
	for j in range(tot_points):
		x2,y2 = points[j]
		sum += abs(x2 - x1) + abs(y2 - y1)

avg_dist = sum/pairs
print("The average distance between two points is",avg_dist)