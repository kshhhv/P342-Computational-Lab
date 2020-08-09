# factorial n! say for n=10 or 15, check and trap negative integers, say for -5!

product = 1
n = int(input("Enter a number: "))

if n<0:
	print("Factorial of negative number is undefined.")

else:	
	while (n>0):
		product = product * n
		n = n - 1

	print("The factorial is", product)
