import mylibrary as ml
import matplotlib.pyplot as plt
from math import log,e

#Define the problem function
f1 = lambda x,y,z: z
f2 = lambda x,y,z: 1-x-z

#analytical solution:
fx = lambda x: 1 + e**(-x) - x**2/2 + 2*x
#initial values
x0,y0,z0 = 0,2,1
#define stepsizes and x range
h = [0.5, 0.1, 0.05, 0.02]
xn = 5

for i in h:
	#Call runge kutta function from library
	Xl,Yl = ml.rungeKuttaSecond(x0, y0, z0, -xn, -i, f1, f2)
	#reverse from (like, 0 to -1) to (-1 to 0)
	Xl.reverse()
	Yl.reverse()
	X,Y = ml.rungeKuttaSecond(x0, y0, z0, xn, i, f1, f2)
	X = Xl + X
	Y = Yl + Y
	plt.plot(X,Y,label = 'runge kutta, step={}'.format(i))

#Analytical solution
ml.plot_fun(fx,-5,5,0.02)

#give title and labels
plt.title("Second order DE using Runge Kutta")
plt.xlabel('x value')
plt.ylabel('y value')
plt.grid()
plt.legend()

plt.savefig("Q2_graph.pdf")
print("Graph has been saved")
plt.show()


'''
OUTPUT:
Graph has been saved
'''
