import random
import matplotlib.pyplot as plt


def vector_sum(vec_A, vec_B):
    if len(vec_A) == len(vec_B):
        dim = len(vec_A)
    else:
        raise IndexError("Length of vectors are not same.")
    
    add = []
    for i in range(dim):
        add.append(vec_A[i] + vec_B[i])

    return add

def vector_product(vec_A, vec_B):
    if len(vec_A) == len(vec_B):
        dim = len(vec_A)
    else:
        raise IndexError("Length of vectors are not same.")

    in_pro = 0
    for i in range(dim):
        in_pro += vec_A[i]*vec_B[i]

    return in_pro

def load_matrix(file):
    with open(file, 'r' ) as f:
        mat_M = [[int(num) for num in row.split(' ')] for row in f]
    return mat_M

def print_matrix(mat_M):
    for i in mat_M:
        print(i)

def matrix_operation(mat_M, vec_A):
    if len(mat_M[0]) != len(vec_A):
        raise IndexError("Columns of matrix is not equal to vector elements.")

    vec_B = [0,0,0]
    for i in range(len(mat_M)):
        for j in range(len(mat_M[i])):
            vec_B[i] += mat_M[i][j]*vec_A[j]
    return vec_B

def matrix_product(mat_M, mat_N):
    if len(mat_M[0]) != len(mat_N):
        raise IndexError("Columns of first matrix is not equal to rows of second matrix.")

    mat_C = []
    for i in range(len(mat_M)):
        row = []
        for j in range(len(mat_M[0])):
            element = 0
            for k in range(len(mat_N[j])):
                element += mat_N[k][j] * mat_M[i][k]
            row.append(element)
        mat_C.append(row)

    return mat_C


def partial_pivot(mat_M, mat_N = None):
    n = len(mat_M)
    for r in range(n-1):
        if mat_M[r][r] == 0:
            for r1 in range(r+1,n):
                if mat_M[r1][r] > mat_M[r][r]:
                    mat_M[r], mat_M[r1] = mat_M[r1], mat_M[r]
                    if mat_N == None:
                    	continue
                    mat_N[r], mat_N[r1] = mat_N[r1], mat_N[r]

    if mat_N == None:
    	return mat_M
    	
    return mat_M, mat_N

def gauss_jordan(mat_M, mat_N):
    n = len(mat_M)
    #do partial pivoting
    partial_pivot(mat_M, mat_N)

    for r in range(n):
        #make the diagonal element 1
        pivot = mat_M[r][r]
        for c in range(r,n):
            mat_M[r][c] = mat_M[r][c]/pivot
        if type(mat_N[0]) == list:
            for k in range(n):
                mat_N[r][k] = mat_N[r][k]/pivot
        else:
            mat_N[r] = mat_N[r]/pivot

        #make the other element in that column 0
        for r1 in range(n):
            #nothing to do for the diagonal element or if it already is 0
            if (r1 == r) or (mat_M[r1][r] == 0):
                continue
            else:
                factor = mat_M[r1][r]
                for c in range(r,n):
                    mat_M[r1][c] = mat_M[r1][c] - factor*mat_M[r][c]
                if type(mat_N[0]) == list:
                    for l in range(n):
                        mat_N[r1][l] = mat_N[r1][l] - factor*mat_N[r][l]
                else:
                    mat_N[r1] = mat_N[r1] - factor*mat_N[r]
    return mat_N

def forward_backaward_substitution(mat_L, mat_U, vec_B):

    #initialize two vectors to store the solution
    x = [0] * len(mat_U[0])
    y = [0] * len(mat_L[0])
    
    #forward substitution    
    for i in range(len(mat_L)):
        sum = 0
        for j in range(i):
            sum += mat_L[i][j]*y[j]
        y[i] = vec_B[i] - sum

    #backward substitution (loop should run in reverse)
    for i in reversed(range(len(mat_U))):
        sum = 0
        for j in reversed(range(i, len(mat_U[0]))):
            sum += mat_U[i][j]*x[j]
        x[i] = (y[i] - sum)/mat_U[i][i]

    return x

def LU_decomposition(mat_A):

    n = len(mat_A)

    #initialize empty matrix to store decomposed matrices
    L = [[0 for x in range(n)] for y in range(n)] 
    U = [[0 for x in range(n)] for y in range(n)]

    #loop through every columns of A 
    for i in range(len(mat_A)):

        #Diagonal entries of L matrix are all 1
        L[i][i] = 1

        #Upper triangular matrix
        for k in range(i, len(mat_A[0])):
            sum = 0
            for j in range(i): 
                sum += (L[i][j] * U[j][k])
  
            U[i][k] = mat_A[i][k] - sum

        #Lower triangular matrix
        for k in range(i+1, len(mat_A[0])):             
            sum = 0 
            for j in range(i): 
                sum += (L[k][j] * U[j][i]) 
            
            #The order of element is reversed from i,k to k,i
            L[k][i] = (mat_A[k][i] - sum) / U[i][i] 
  
    return L,U

def check_inverse(mat_U):
    #initialize variable to store determinant
    det = 1
    for i in range(len(mat_U)):
        det = det*mat_U[i][i]

    #raise error if determinant is zero, return False
    if det == 0:
        raise Warning("Inverse of the matrix does not exist")
        return False
    
    else:
        return True


def matrix_inverse(mat_A):

    n = len(mat_A)

    #initialize empty matrix to store inverse
    inverse_mat = [[0 for x in range(n)] for y in range(n)] 

    #Decompose the matrix
    L,U = LU_decomposition(mat_A)

    #Check if the inverse exist
    if check_inverse(U) == True:

        for i in range(n):

            #initialize vector with ith value 1, rest 0
            B = [0 for x in range(n)]
            B[i] = 1

            column = forward_backaward_substitution(L, U, B)

            #Store the solution column wise
            for j in range(n):
                inverse_mat[j][i] = round(column[j], 3)

        return inverse_mat

    else:
        return None

def derivative(f,x):
	return (f(x+0.0001)-f(x - 0.0001))/(2*0.0001)

def double_derivative(f,x):
    return (derivative(f, x+0.0001) - derivative(f, x-0.0001))/2*0.0001

def bracketing(a,b,f,bt):
	while f(a)*f(b)>0:
		print(a,b,f(a),f(b))
		if abs(f(a))>abs(f(b)):
			b = b + bt*(b-a)
		elif abs(f(a))<abs(f(b)):
			a = a - bt*(b-a)
	return a,b

def bisection(a, b, f, max_iter = 200):
	c = a #initial guess
	errors = []
	for i in range(max_iter):
		c_prev = c
        #define c as midpoint of a and b
		c = (a+b)/2
		if f(c) == 0:
			return c, f(c)
		elif f(a)*f(c) < 0:
			b = c
		elif f(a)*f(c) > 0:
			a = c
        #append the absolute error in list        
		errors.append(abs(c - c_prev))
        #check if convergence criteria satisfied
		if abs(c - c_prev) < 10**(-6):
			return (c, i+1, errors)

def reg_falsi(a,b,f, max_iter = 200):
	c = a
	errors = []
	for i in range(max_iter):
		c_prev = c
        #define c as the point of intersection of f(b)-f(a) and x-axis
		c = b - (b-a)*f(b)/(f(b)-f(a))
		if c == 0:
			return c, f(c)
		elif f(a)*f(c) < 0:
			b = c
		elif f(a)*f(c) > 0:
			a = c
        #append the absolute error in list
		errors.append(abs(c - c_prev))
        #check if convergence criteria satisfied
		if abs(c - c_prev) < 10**(-6):
			return (c, i+1, errors)


def newton_raphson(x,f, max_iter = 200):
	errors = []
	for i in range(max_iter):
		x_prev = x
        #update x as per newton-raphson formula
		x = x - f(x)/derivative(f,x)
        #append the absolute error in list
		errors.append(abs(x-x_prev))
        #check if convergence criteria satisfied
		if abs(x-x_prev) < 10**(-6):
			return (x, i+1, errors)

def store_data(file_name, data1, data2):
    #open the file
	f = open(file_name, 'w')
    #give header
	f.writelines("Iteration count, C(i) - C(i-1) \n")
	for i in range(len(data1)):
        #store data as csv
		f.writelines(str(data1[i]+1) +',' + str(data2[i]) + '\n')
	print("Data succesfully stored in", file_name)
    #close the file
	f.close()

def print_data(file_name):
    #open the file
	f = open(file_name, 'r')
	print('Printing data from', file_name, ':')
	for i in f.readlines():
        #print data from csv in tabular form
		row = i.strip().split(',')
		print(row[0] + '\t' + row[1])
    #close the file   
	f.close()

#function to output polynomial function from coefficients
def polynomial_fun(coeffs):
    def p(x):
        n = len(coeffs)
        y = 0
        for i in range(n):
            y += coeffs[i]*x**(n-i-1)
        return y
    return p


def laguerre(coeffs, x0, max_iter = 200):
    n = len(coeffs)
    #define the polynomial function
    p = polynomial_fun(coeffs)
    x = x0
    #check if guess was correct
    if p(x) == 0:
        return x
    for i in range(max_iter):
        #store previous value for comparison
        x_prev = x
        G = derivative(p,x)/p(x)
        H = G**2 - double_derivative(p,x)/p(x)
        denom1 = G+((n-1)*(n*H - G**2))**0.5
        denom2 = G-((n-1)*(n*H - G**2))**0.5
        #compare denominators
        if abs(denom2)>abs(denom1):
            a = n/denom2
        else:
            a = n/denom1
        x = x - a
        #check if convergence criteria satisfied
        if abs(x - x_prev) < 10**(-6):
            return x
    return x


def syn_division(coeffs, root):
    n = len(coeffs)
    #initiate list with the same first element
    new_coeffs = []
    new_coeffs.append(coeffs[0])
    for i in range(1, n):
        new_coeffs.append(new_coeffs[i-1]*root+coeffs[i])
    return new_coeffs[:-1]

def polynomial_solution(coeffs, x):
    n = len(coeffs)
    roots = []
    for i in range(n-1):
        #find one of the root of polynomial and add to list
        root = laguerre(coeffs, x)
        roots.append(root)
        #reduce the polynomial by synthetic division
        coeffs = syn_division(coeffs, root)
    return roots

#ASSIGNMENT 6

#Integration methods
def mid_integration(f,a,b,N):
    integ = 0
    h = (b-a)/N
    for i in range(N):
        x = (2*a+(2*i+1)*h)/2
        integ += h*f(x)
    return integ

def trap_integration(f,a,b,N):
    integ = 0
    h = (b-a)/N
    x = a
    for i in range(N):
        xn = x + h
        integ += h*(f(xn)+f(x))/2
        x = xn
    return integ

def simpsons_integration(f,a,b,N):
    h = (b-a)/N
    x = a
    integ = h*f(x)/3
    for i in range(N-1):
        x = x + h
        if i%2 == 0:
            integ += h*4*f(x)/3
        else:
            integ += h*2*f(x)/3
    integ += h*f(b)/3
    return integ

#ceil function
def ceil(x):
    if (x/1.0).is_integer() != True:
        x = int(x)+1
    return x

#N calculation for different integration methods
def mid_N(a,b,max_f, error):
    N = ((b-a)**3*max_f/(24*error))**0.5
    N = ceil(N)
    return N

def trap_N(a,b,max_f, error):
    N = ((b-a)**3*max_f/(12*error))**0.5
    N = ceil(N)
    return N

def simp_N(a,b,max_f, error):
    N = ((b-a)**5*max_f/(180*error))**0.25
    N = ceil(N)
    return N

#intgeration by monte carlo
def monte_carlo(f,a,b,N):
    sum = 0
    sq_sum = 0
    for i in range(N):
        r = random.random()
        x = a + (b-a)*r
        sum += f(x)
        sq_sum += f(x)**2

    integral = (b-a)*sum/N
    sigma = ((1/N)*(sq_sum) - (sum/N)**2)**0.5
    return integral, sigma

### After Assignment 7 ###

#first order ode using explicit euler's method
def euler_de(y_dash, y0, x0, h, xn):
	#intialize list with initial values
    y = [y0]
    x = [x0]
    i = 0
    #append lists
    while x[i] < xn:
        y.append(y[i] + h * y_dash(y[i],x[i]))
        x.append(x[i]+h)
        i+=1

    return y,x

def rungeKuttaSecond(x0, y0, z0, xn, h, f1, f2):
	#intialize lists
    x = x0
    X = [x0]   
    Y = [y0]
    Z = [z0]
    i = 0
    #check if range is covered
    while abs(x)<abs(xn):
        x,y,z = X[i],Y[i],Z[i]
        k1 = h*f1(x, y, z)
        l1 = h*f2(x, y, z)
        
        k2=h*f1(x+h/2, y+(k1*h)/2, z+(l1*h)/2)
        l2=h*f2(x+h/2, y+(k1*h)/2, z+(l1*h)/2)
        
        k3=h*f1(x+h/2, y+(k2*h)/2, z+(l2*h)/2)
        l3=h*f2(x+h/2, y+(k2*h)/2, z+(l2*h)/2)
        
        k4=h*f1(x+h, y+k3, z+l3)
        l4=h*f2(x+h, y+k3, z+l3)

        i += 1
        X.append(x + h)
        Y.append(y+((k1+2*k2+2*k3+k4))/6)
        Z.append(z+((l1+2*l2+2*l3+l4))/6)
         
    return X[:-1],Y[:-1]

def plot_fun(f,x,xn,h):
	#create empty lists
	Xt = []
	Yt = []
	i = 0
	#append the list for diff values
	while x<=xn:
	     Xt.append(x)
	     Yt.append(f(x))
	     x = x + h
	     i += 1
	#plot the graph
	plt.plot(Xt,Yt, label = 'analytical solution')


def Boundary(f, g, x0, y0, xn, yn, z0, z1, h):
	#find the first guess y for lower and upper z guess
    temp,a_list = rungeKuttaSecond(x0, y0, z0, xn, h, f, g)
    a = a_list[-1]
    temp,b_list = rungeKuttaSecond(x0, y0, z1, xn, h, f, g)
    b = b_list[-1]
    #compare the obtained y
    if abs(a - yn)>0.001 and abs(yn - b)>0.001:
        z = z1 + (((z0 - z1)*(yn - b))/(a-b))
        temp,d_list = rungeKuttaSecond(x0, y0, z, xn, h, f, g)
        d = d_list[-1]
        #call recursively
        if (d - yn)>0.001:
            z2 = z1 + (z-z1)*(yn - b)/(d-b)
            Boundary(f, g, x0, y0, xn, yn, z2, z1, h)
        if (yn - d)>0.001:
            z2 = z + (z0-z)*(yn - d)/(a-d)
            Boundary(f, g, x0, y0, xn, yn, z2, z1, h)
        if abs(yn - d)<0.001:
            return z
    if abs(a - yn)<0.001:
        return z0
    if abs(b - yn)<=0.001:
        return z1


