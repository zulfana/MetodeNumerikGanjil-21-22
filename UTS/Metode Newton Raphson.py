def newtons(f,df,x0):
  e = 0.001
  N = 100
  for i in range (0,N):
    print("%d   | %f    | %f    " %(i,x0,f(x0)))
    if abs(f(x0)) < e:
      return x0,i
    if df(x0) == 0:
      print("Zero derivative")
      return None
    x0 = x0 - f(x0)/df(x0)
  print("Maximum iteration")
  return x0, i

f  = lambda x: 2*x**3-4*x**2-24
df = lambda x: 6*x**2-8*x
x0 = 5

x_root, iteration = newtons(f,df,x0)
print('Hasil : ',"%.4f" % x_root)
print('In %d iteration' %iteration)
