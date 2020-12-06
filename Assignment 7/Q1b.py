import mylibrary as ml
import matplotlib.pyplot as plt
from math import log,e

#Define the problem function
y_dash = lambda y,x: 6 - (2*y/x)
#Define analytical solution
fx = lambda x: -45/(x*x) + 2*x 

#define initial value and step size
y0 = 1
x0 = 3
h = [0.5,0.1,0.05,0.02]
xn = 25

#call euler function for diff stepzsize
for i in h:
	y,x = ml.euler_de(y_dash,y0,x0,i,xn)
	plt.plot(x,y,label="Euler's method, step = {}".format(i))

#plot analytical solution
ml.plot_fun(fx,x0,xn,0.02)

#add title and labels
plt.title("Differential equation solution using Euler's method")
plt.ylabel('y value')
plt.xlabel('x value')
plt.grid(axis = 'both', which = 'both')
plt.legend()

#save the graph as pdf and display it
plt.savefig("Q1b_graph.pdf")
print("Graph has been saved")
plt.show()

'''
OUTPUT
Graph has been saved
'''
