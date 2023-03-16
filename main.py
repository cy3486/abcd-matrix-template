#import numpy as np
from sympy import * #use sympy to calculate symbolically

var = symbols('var')
lam = 1.064*10**(-3)#lambda is reserved word
n = 1.82  #refractive index

#defining the functions
def f(x):# lens
    return Matrix([[1, 0], [-1/x, 1]])
def l(x):# length
    return Matrix([[1, x], [0, 1]])
def fth(x, P):#thermal lens
    return Matrix([[1, 0], [-1/(x/P), 1]])
def s(a, d):#stable range
    return a + d
def w(a, b, d):#beam radius
    return (2*lam*abs(b)/(pi*(4 - (a + d)**2)**0.5))**0.5#sqrt() is unavailable here
def w0(a, c, d):#beam waist
    return (abs((lam/(2*pi*c))*(4 - (a + d)**2)**0.5))**0.5#sqrt() is unavailable here
def L(a, c, d):#waist location
    return (a - d)/(2 * c)

#ABCD the cavity running matrix
a1, b1, c1, d1 = #write your ABCD matrix here! use @ between 2 matrices to multiply them. 

#calculating the cavity
s1 = s(a1, d1)
w1 = w(a1, b1, d1)
w10 = w0(a1, c1, d1)
l10 = L(a1, c1, d1)

#plot the results
downlimit = 0
rge = 350
p1 = plot(s1, (var, downlimit, rge), ylim=(-2,2), show=false)
p1.title = 'a+d'
p2 = plot(w1, (var, downlimit, rge), ylim=(0,0.5), show=false)
p2.title = 'radius'
p3 = plot(w10, (var, downlimit, rge), ylim=(0,0.5), show=false)
p3.title = 'waist'
p4 = plot(l10, (var, downlimit, rge), show=false)
p4.title = 'waist location'

p1.append(p2[0])
p1.append(p3[0])
p1.append(p4[0])
p1.show()
