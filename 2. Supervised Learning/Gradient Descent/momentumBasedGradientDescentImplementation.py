import math
 
alpha = 0.01   #Learning rate
beta = 0.9     #Same use case as acceleration in physics

def obj_func(x):
    return x**2 - 4*x + 4

#Gradient of the paticular function(df/dx)
def grad(x):
    return 2*x - 4

#Parameter of the objective function
x = 0

#Number of iterations
iterations = 0

v = 0 

while(1):
    iterations += 1
    v = beta*v + (1-beta)*grad(x)
    x_prev = x
    x = x - alpha*v
    print("Value of objective function on iteration ",iterations," is ",x)
    if(x == x_prev):
        print("Done optimizing the objective function")
        break