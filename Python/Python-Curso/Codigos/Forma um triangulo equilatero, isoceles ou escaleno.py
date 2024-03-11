reta1=float(input('Tamanho da reta 1? '))
reta2=float(input('Tamanho da reta 2? '))
reta3=float(input('Tamanho da reta 3? '))

r1=abs(reta2-reta3)<=reta1<=(reta2+reta3)
r2=(abs(reta1-reta3)<=reta2)<=(reta1+reta3)
r3=(abs(reta2-reta1)<=reta3)<=(reta2+reta1)
equi=(reta1 == reta2 == reta3)
esca=(reta1 != reta2 != reta3)
iso=(reta1==reta2 and (reta1!=reta3)) or (reta1==reta3 and (reta1!=reta2))

if (r1 and r2 and r3) == True:
    if equi == True:
        print('Forma um triangulo')
        print('É um triangulo equilatero')
    elif esca == True:
        print('Forma um triangulo')
        print('É um triangulo escaleno')
    elif iso == True:
        print('Forma um triangulo')
        print('É um triangulo isoceles')
else:
    print('Não forma um triangulo')