def bisection(f, a, b, e=0.5, N = 100):
  x_1 = a
  x_2 = b
  
  if f(x_1)*f(x_2) >= 0:
    print("Use another guess range")
    return None
  
  for n in range (1,N):
    x_m = (x_1 + x_2)/2
    if abs(f(x_m)) < e:
      return x_m, n
    else:
      if f(x_1)*f(x_m) < 0:
        x_2 = x_m
      elif f(x_2)*f(x_m) < 0:
        x_1 = x_m
  return x_m, n

f = lambda x: 2*x**3-4*x**2-24
a = 2
b = 9

x_root, iteration = bisection(f,a,b)
print('Hasil : ',"%.4f" % x_root)
print('In %d iteration' %iteration)
