import math

angulo=float(input('qual o ângulo?'))
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))

print('O seno, cosseno e tangente de {} é {:.2f}, {:.2f}, {:.2f}'.format(angulo, seno, cosseno, tangente))
