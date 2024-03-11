def escreva(msg):
    print(f'{"-" * len(msg)}----')
    print(f'  {msg}  ')
    print(f'{"-" * len(msg)}----')


escreva(str(input('Digite uma frase: ')))
