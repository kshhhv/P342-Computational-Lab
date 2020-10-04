import mylibrary as ml
import matplotlib.pyplot as plt
import math

#Define the problem function
f = lambda x: -x - math.cos(x)
#define initial bracket guess for bisection and regula falsi
a,b = -2,2
#initial guess for newton_raphson
x_guess = -2


print("USING BISECTION")
#Call the root finding method passing the bracketed values and function
a_bi, iteration_bi, errors_bi= ml.bisection(a, b, f)
print("The root of the function is: ", a_bi)
#store the convergence data in csv and display it
ml.store_data('Q1b_bisection.csv', range(iteration_bi), errors_bi)
ml.print_data('Q1b_bisection.csv')

print('\n')#extra lines

print("USING REGULA FALSI")
#Call the root finding method passing the bracketed values and function
a_reg, iteration_reg, errors_reg= ml.reg_falsi(a, b, f)
print("The root of the function is: ", a_reg)
#store the convergence data in csv and display it
ml.store_data('Q1b_reg_falsi.csv', range(iteration_reg), errors_reg)
ml.print_data('Q1b_reg_falsi.csv')

print('\n')#extra lines


print("USING NEWTON RAPHSON")
#Call the root finding method passing the bracketed values and function
a_new, iteration_new, errors_new= ml.newton_raphson(x_guess, f)
print("The root of the function is: ", a_new)
#store the convergence data in csv and display it
ml.store_data('Q1b_newton_raphson.csv', range(iteration_new), errors_new)
ml.print_data('Q1b_newton_raphson.csv')

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
plt.savefig('Q1b_graph.pdf')
plt.show()

'''
OUTPUT:
USING BISECTION
The root of the function is:  -0.7390851974487305
Data succesfully stored in Q1b_bisection.csv
Printing data from Q1b_bisection.csv :
Iteration count  C(i) - C(i-1)
1       2.0
2       1.0
3       0.5
4       0.25
5       0.125
6       0.0625
7       0.03125
8       0.015625
9       0.0078125
10      0.00390625
11      0.001953125
12      0.0009765625
13      0.00048828125
14      0.000244140625
15      0.0001220703125
16      6.103515625e-05
17      3.0517578125e-05
18      1.52587890625e-05
19      7.62939453125e-06
20      3.814697265625e-06
21      1.9073486328125e-06
22      9.5367431640625e-07


USING REGULA FALSI
The root of the function is:  -0.7390851075956052
Data succesfully stored in Q1b_reg_falsi.csv
Printing data from Q1b_reg_falsi.csv :
Iteration count  C(i) - C(i-1)
1       2.416146836547142
2       0.8581409353700294
3       0.25004850112314936
4       0.04085405611230608
5       0.00540103748255627
6       0.0006876910011640591
7       8.712025559531877e-05
8       1.10297457364128e-05
9       1.3962926479482718e-06
10      1.7675956265339465e-07


USING NEWTON RAPHSON
The root of the function is:  -0.7390851332151607
Data succesfully stored in Q1b_newton_raphson.csv
Printing data from Q1b_newton_raphson.csv :
Iteration count  C(i) - C(i-1)
1       1.2654638321494631
2       0.0045535563599105044
3       4.590990635877645e-06
4       4.650835272457243e-12
'''