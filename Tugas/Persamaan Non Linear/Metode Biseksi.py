def RegFalsi(f,a,b,tol,No):
    # This program is to find root using Secant method
    # INPUTS:
    # f represents the function that you want to find the root
    # a represents initial point 1 of the search
    # b represents initial point 2 of the search
    # tol represents the tolerance 
    # No represents the total number of iteration to be performed
    # OUTPUTS:
    # i represents current number of iteration
    # p represents the computed root
    i = 2
    ap = a
    bp = b
    fa = f(ap)
    print ("i  p")
    print i-2, ap
    print i-1, bp
    if (fa*f(bp))>0:
        print "There is no root in [",a,",", b,"]"      
        return
    while i<= No:
        p = bp-f(bp)*(bp-ap)/(f(bp)-fa)
        fp = f(p)
        print i,p        
        if fp is 0 or (bp-ap)/2.0<tol :
            return p
        i = i+1
        if fa*fp > 0:
            ap = p
            fa = fp
        else:
            bp = p
    print "After", No, "iterations, still couldn't find the root."
    
def f(x):
    from math import cos
    fx = cos(x)-x
    return fx