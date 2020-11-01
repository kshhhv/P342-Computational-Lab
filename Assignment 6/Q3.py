import mylibrary as ml
from math import e

#Define the problem function
f = lambda x: e**(-x**2)

#define max value of 2nd and 4th order derivative
f_second_max = 2
f_fourth_max = 12

#calculate the N value and then integral for each method
mid_n = ml.mid_N(0,1,f_second_max,0.0001)
mid_value = ml.mid_integration(f,0,1,mid_n)
print("Midpoint method: N = {}, integral = {}".format(mid_n,mid_value))

trap_n = ml.trap_N(0,1,f_second_max,0.0001)
trap_value = ml.trap_integration(f,0,1,trap_n)
print("Trapezoidal method: N = {}, integral = {}".format(trap_n,trap_value))

simp_n = ml.simp_N(0,1,f_fourth_max,0.0001)
simp_value = ml.simpsons_integration(f,0,1,simp_n)
print("Simpsons method: N = {}, integral = {}".format(simp_n,simp_value))

'''
OUTPUT:

Midpoint method: N = 29, integral = 0.7468605879210651
Trapezoidal method: N = 41, integral = 0.7467876578237479
Simpsons method: N = 6, integral = 0.7468303914893448

'''