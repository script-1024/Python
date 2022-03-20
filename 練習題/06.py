#求一元二次方程式 ax2+bx+c=0 的根
a,b,c = map(int,input().split(' '))
try:
    x1 = ( (-b)+(b**2-4*a*c)**0.5 ) / (2*a)
    x2 = ( (-b)-(b**2-4*a*c)**0.5 ) / (2*a)
    x1,x2 = int(x1),int(x2)

    if x1<x2: x1,x2 = x2,x1
    if x1==x2: print(f"Two same roots x={x1}")
    else: print(f"Two different roots x1={x1} , x2={x2}")
except: print("No real root")