import numpy as np
import math

def f(x):
    return(np.exp(-x)*math.sin(2*x) + 1)

def turunan(x0,h):
    step = 1
    condition = true
x0 = input('x:')
h = input('h:')
x0 = float(x0)
h = float(h)
err = 1000
dfxold = 1000
bfxold = 1000
cfxold = 1000
while err>=0.00001:
    dfx = (f(x0+h)-f(x0))/h
    err = abs(dfxold -dfx)
    dfxold=dfx
    h = h/2

print ("the forward derivative at x= with specifed accuracy is")
print (dfx)
