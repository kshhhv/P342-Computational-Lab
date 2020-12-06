import mylibrary as ml
import matplotlib.pyplot as plt
from math import log,e

#Define the problem function
f1 = lambda x,y,z: z
f2 = lambda x,y,z: z+1
#define analytical solution
fx = lambda x: 2*e**x -x -1

#Initial values
x0,y0 = 0,1
xn,yn = 1,3.436
h = [0.5, 0.1, 0.05, 0.02]
#intial guess of z
z0,z1=0,2

#loop through different stepsize
for i in h:
	#call the boundary function to calculate z
	z = ml.Boundary(f1, f2, x0, y0, xn, yn, z0, z1, i)
	print("for stepsize {}, z = {}".format(i,z))

	#use the calculated z in runge kutta to plot graph
	#define x range
	x1,x2 = -5,2.5
	#negative plot
	Xl,Yl = ml.rungeKuttaSecond(x0, y0, z, x1, -i, f1, f2)
	Xl.reverse()
	Yl.reverse()
	#positive plot
	X,Y = ml.rungeKuttaSecond(x0, y0, z, x2, i, f1, f2)
	X = Xl + X
	Y = Yl + Y
	plt.plot(X,Y,label = 'stepsize={}'.format(i))

#Analytical solution
ml.plot_fun(fx,-5,2.5,0.02)

#give title and labels
plt.title("Boundary value problem solution")
plt.xlabel('x value')
plt.ylabel('y value')
plt.grid()
plt.legend()

plt.savefig("Q3_graph.pdf")
print("Graph has been saved")
plt.show()


'''
OUTPUT:
for stepsize 0.5, z = 1.240162514518219
for stepsize 0.1, z = 0.8503709461987103
for stepsize 0.05, z = 1.0494032326735714
for stepsize 0.02, z = 1.0202816500769978
Graph has been saved
'''


plt.show()
