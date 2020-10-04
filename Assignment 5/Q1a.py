import mylibrary as ml
import matplotlib.pyplot as plt
import math

#Define the problem function
f = lambda x: math.log(x) - math.sin(x)


print("USING BISECTION")
#Call the root finding method passing the bracketed values and function
a_bi, iteration_bi, errors_bi= ml.bisection(1.5, 2.5, f)
print("The root of the function is: ", a_bi)
#store the convergence data in csv and display it
ml.store_data('Q1a_bisection.csv', range(iteration_bi), errors_bi)
ml.print_data('Q1a_bisection.csv')

print('\n')#extra lines

print("USING REGULA FALSI")
#Call the root finding method passing the bracketed values and function
a_reg, iteration_reg, errors_reg= ml.reg_falsi(1.5, 2.5, f)
print("The root of the function is: ", a_reg)
#store the convergence data in csv and display it
ml.store_data('Q1a_reg_falsi.csv', range(iteration_reg), errors_reg)
ml.print_data('Q1a_reg_falsi.csv')

print('\n')#extra lines

print("USING NEWTON RAPHSON")
#Call the root finding method passing the function and initial guess
a_new, iteration_new, errors_new= ml.newton_raphson(1.5, f)
print("The root of the function is: ", a_new)
#store the convergence data in csv and display it
ml.store_data('Q1a_newton_raphson.csv', range(iteration_new), errors_new)
ml.print_data('Q1a_newton_raphson.csv')

#plot the graph of convergence
plt.plot(range(iteration_bi), errors_bi, '-o', label = 'Bisection' )
plt.plot(range(iteration_reg), errors_reg, '-o', label = 'Regula Falsi')
plt.plot(range(iteration_new), errors_new, '-o', label = 'Newton Raphson')

plt.title('Convergence comparison')

plt.ylabel('C(i) - C(i-1)')
plt.xlabel('Iteration count')
plt.legend()
plt.minorticks_on()
plt.grid(axis = 'y', which = 'both')

#save the graph as pdf and display it
plt.savefig("Q1a_graph.pdf")
plt.show()


'''
OUTPUT:
USING BISECTION
The root of the function is:  2.2191076278686523
Data succesfully stored in Q1a_bisection.csv
Printing data from Q1a_bisection.csv :
Iteration count  C(i) - C(i-1)
1       0.5
2       0.25
3       0.125
4       0.0625
5       0.03125
6       0.015625
7       0.0078125
8       0.00390625
9       0.001953125
10      0.0009765625
11      0.00048828125
12      0.000244140625
13      0.0001220703125
14      6.103515625e-05
15      3.0517578125e-05
16      1.52587890625e-05
17      7.62939453125e-06
18      3.814697265625e-06
19      1.9073486328125e-06
20      9.5367431640625e-07


USING REGULA FALSI
The root of the function is:  2.2191071418525734
Data succesfully stored in Q1a_reg_falsi.csv
Printing data from Q1a_reg_falsi.csv :
Iteration count  C(i) - C(i-1)
1       0.650690637448136
2       0.06358816982236615
3       0.004498957497641953
4       0.0003069684216292501
5       2.0890509801585466e-05
6       1.4214364827402903e-06
7       9.671651568510242e-08


USING NEWTON RAPHSON
The root of the function is:  2.219107148913746
Data succesfully stored in Q1a_newton_raphson.csv
Printing data from Q1a_newton_raphson.csv :
Iteration count  C(i) - C(i-1)
1       0.9934562933536615
2       0.2586818171598342
3       0.015599302073612265
4       6.802390317739437e-05
5       1.303291696785891e-09
'''