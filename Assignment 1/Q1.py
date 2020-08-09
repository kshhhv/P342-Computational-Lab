#add 1+2+3+ ... 100 WITHOUT using the formula n(n+1)/2

sum = 0
n = int(input("Enter a number: "))

for i in range(n+1):
	sum = sum + i
	print(sum)

print("The sum is", sum)