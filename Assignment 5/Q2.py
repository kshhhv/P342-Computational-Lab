import mylibrary as ml
import math

#Define list of coefficients from higher to lower power
coeffs = [1, -3, -7, 27, -18]

a = 1.5 #initial guess 

#Call the polynomial solving function that returns list of roots
sol = ml.polynomial_solution(coeffs, a)

print("The roots of the polynomial are:")
print(sol)

'''
OUTPUT:
The roots of the polynomial are:
[3.0000000000000577, -3.0000000000000058, 1.9999999999999334, 1.0000000000000147]
'''
