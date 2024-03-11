import math

co=float(input('qual o cateto oposto?'))
ca=float(input('qual o cateto adjacente?'))
h= math.pow(co, 2)*math.pow(ca, 2)

print('A hipotenusa é {}'.format(h))
