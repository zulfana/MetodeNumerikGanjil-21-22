import math
# Definisikan Fungsi
def f(x):
    return x**2 + e**(2*x*math.sin(x))

# Definisikan Turunan dari Fungsi
def g(x):
    return (x**2*e**(2*x*math.sin(x)+1))/(e**(2*x*math.sin(x)))

# Implementasi dari Metode Newton Raphson

def newtonRaphson(x0,e,N):
    print('\n\n*** Implementasi dari Metode Newton Raphson ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Error dibagi 0')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nTidak Konvergen.')


# Input Section
x0 = input('Tebakan Awal: ')
e = input('Toleransi Error: ')
N = input('Iterasi Ke N: ')

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
N = int(N)

# Starting Newton Raphson Method
newtonRaphson(x0,e,N)