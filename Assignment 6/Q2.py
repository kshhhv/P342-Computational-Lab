import mylibrary as ml

#Define the problem function
f = lambda x: x/(1+x)

N_values = [4,10,26]
analytic_value = 1.30685282

#initiate lists to store data
error_data = []
error_data.append(['N count, midpoint error, trapezoidal error, simpsons error'])
integral_data = []
integral_data.append(['N count, midpoint value, trapezoidal value, simpsons value'])

for i in N_values:
	#rectangle/midpoint method
	value_mid = ml.mid_integration(f,1,3,i)
	error_mid = abs(analytic_value-value_mid)

	#trapezoidal method
	value_trap = ml.trap_integration(f,1,3,i)
	error_trap = abs(analytic_value-value_trap)

	#simpsons method
	value_simp = ml.simpsons_integration(f,1,3,i)
	error_simp = abs(analytic_value-value_simp)

	#store data for current N value
	integral_data.append([i, value_mid, value_trap, value_simp])
	error_data.append([i, error_mid, error_trap, error_simp])

#print the integral value and error
print("\nThe final calculated value of each method for respective N count:")
for i in integral_data:
	print(i)

print("\nThe deviation of final value compared to analytical solution:")
for i in error_data:
	print(i)

'''
OUTPUT:

The final calculated value of each method for respective N count:
['N count, midpoint value, trapezoidal value, simpsons value']
[4, 1.3087801087801088, 1.3029761904761905, 1.3067460317460318]
[10, 1.3071646395900398, 1.3062285968245722, 1.3068497693110697]
[26, 1.3068990323038625, 1.3067603809022117, 1.3068527513069685]

The deviation of final value compared to analytical solution:
['N count, midpoint error, trapezoidal error, simpsons error']
[4, 0.0019272887801087268, 0.003876629523809516, 0.00010678825396825964]
[10, 0.00031181959003978577, 0.0006242231754278738, 3.0506889303616447e-06]
[26, 4.621230386248065e-05, 9.24390977883327e-05, 6.86930314852674e-08]

'''
