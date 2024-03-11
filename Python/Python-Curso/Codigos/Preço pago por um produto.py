valor=float(input('Valor do produto: '))
metodo=int(input('''Qual o metodo de pagamento?
Á vista dinheiro/cheque: 1
Á vista cartão: 2
Em até 2x no cartão: 3
3x ou mais no cartão: 4
Opção: '''))

if metodo==1:
    print('O produto de preço {} pago á vista no dinheiro/cheque tem 10% de desconto e fica {} reais'.format(valor, (valor-(valor*(10/100)))))
elif metodo==2:
    print('O produto de preço {} pago á vista no cartão tem 5% de desconto e fica {} reais'.format(valor, (valor-(valor*(5/100)))))
elif metodo==3:
    print('O produto de preço {} pago em 2x no cartão fica o valor normal'.format(valor,))
elif metodo==4:
    print('O produto de preço {} pago 3x ou mais no cartão tem 20% de juros e fica de 3x de {} reais'.format(valor, (valor+(valor*(20/100)))))
