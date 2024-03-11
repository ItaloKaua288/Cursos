reta1=float(input('Tamanho da reta 1? '))
reta2=float(input('Tamanho da reta 2? '))
reta3=float(input('Tamanho da reta 3? '))

r1=(abs(reta2-reta3)<reta1)<(reta2+reta3)
r2=(abs(reta1-reta3)<reta2)<(reta1+reta3)
r3=(abs(reta2-reta1)<reta3)<(reta2+reta1)

if (r1 and r2 and r3)==True:
    print('Forma um triangulo')
else:
    print('Não forma um triangulo')
