from time import sleep


def mensagem(msg):
    """
        Função para printar uma mensagem.
    :param msg: Mensagem que será mostrada.
    """
    sleep(0.5)
    tot = len(msg) + 4
    print('=' * tot)
    print(f'  {msg}  ')
    print('=' * tot)
    sleep(0.5)


def funcao(func):
    """
        Função para mostrar as informações da função ou biblioteca.
    :param func: Função ou Biblioteca escolhida.
    """
    sleep(0.5)
    help(func)


def cor(cor1):
    """
        Função para mostrar cor desejada.
    :param cor1: Muda a cor conforme o valor escolhido de 0 (cor padrão) até 5.
    """
    if cor1 == 0:
        print('\033[m', end='')
    if cor1 == 1:
        print('\033[31m', end='')
    if cor1 == 2:
        print('\033[32m', end='')
    if cor1 == 3:
        print('\033[33m', end='')
    if cor1 == 4:
        print('\033[34m', end='')
    if cor1 == 5:
        print('\033[35m', end='')


cor(2)
mensagem('SISTEMA DE AJUDA PyHELP')
while True:
    cor(0)
    escolha = input('Função ou Biblioteca: ')
    if escolha.upper().strip() == 'FIM':
        break
    cor(4)
    mensagem(f'Acessando o manual do comando {escolha}')
    cor(5)
    funcao(escolha)
    cor(2)
    mensagem('SISTEMA DE AJUDA PyHELP')
