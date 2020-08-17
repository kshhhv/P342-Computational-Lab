size = int(input("Number of linear equidistant points:"))
points = []

for n in range(size):
	points.append(n)
	n += 1

tot_dist = 0
tot_pairs = size*size

for i in points:
	for j in points:
		tot_dist += abs(j - i)

avg_dist = tot_dist/tot_pairs

print("The average distance between two points is ", avg_dist)
'''
Number of linear equidistant points:6
The average distance between two points is  1.9444444444444444
'''