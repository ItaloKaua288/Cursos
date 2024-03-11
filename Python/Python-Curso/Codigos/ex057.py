print('Qual seu sexo?'
      '[M] Masculino'
      '[F] Feminino')
opçôes = 'M', 'F'
sexo = ''

while sexo not in opçôes:
    print('Tente novamente')
    sexo = input('Qual seu sexo? ').upper().strip()
