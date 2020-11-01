import mylibrary as ml
import matplotlib.pyplot as plt

#define the problem function
f = lambda x: 4/(1+x**2)

#creaye list to store data
n_value, integral_list, sigma_list = [], [], []

#integrate for different N values
for i in range(1,3000):
	N = i*10
	n_value.append(N)
	integral, sigma = ml.monte_carlo(f,0,1,N)
	integral_list.append(integral)
	sigma_list.append(sigma)
	
print("The last calculated value of pi was", integral_list[-1])

#Plot the integral (pi) vs the N value
plt.plot(n_value, integral_list)
plt.title('$\pi$ vs N using monte carlo')
plt.ylabel('Estimated value of $\pi$')
plt.xlabel('N count')
plt.grid(axis = 'both', which = 'both')

#save the graph as pdf and display it
plt.savefig("Q4_graph.pdf")
print("Graph has been saved")
plt.show()

'''
OUTPUT:

The last calculated value of pi was 3.1422108682558823
Graph has been saved

'''