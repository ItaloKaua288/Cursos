nome=input('Qual seu nome completo?').strip()
n=nome.split()

print('Olá! Prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome.split()[0]))
print('Seu ultimo nome é: {}'.format(n[len(n)-1]))
