def menu():
    """
        Função que exibe o menu de opções
    """
    from time import sleep

    titulo('MENU PRINCIPAL')
    print('\033[1;34m1\033[m - Ver pessoas cadastradas')
    print('\033[1;34m2\033[m - Cadastrar nova pessoa')
    print('\033[1;34m3\033[m - Sair do programa')
    print('\033[1;34m-\033[m' * 30)
    while True:
        res = input('\033[36mSua opção: ')
        if not res.isnumeric():
            while True:
                if res.isnumeric():
                    break
                print('\033[1;31mERRO! Digite uma opção válida!\033[m')
                res = input('Sua opção: ')
        res = int(res)
        if res == 3:
            titulo('Saindo do sistema... Até logo!')
            break
        elif res == 1:
            sleep(0.5)
            pessoasCadastradas()
        elif res == 2:
            sleep(0.5)
            cadastrar()


def pessoasCadastradas():
    """
        Função que exibe as pessoas cadastradas e caso a lista não tenha sido criado ele cria automaticamente
    :return:
    """
    try:
        lista = open('lista de cadastro/Cadastrados.txt')
    except:
        lista = open('lista de cadastro/Cadastrados.txt', 'x')
        lista.close()
    lista = open('lista de cadastro/Cadastrados.txt')
    titulo('PESSOAS CADASTRADAS')
    print(lista.read())
    lista.close()
    print('\033[1;34m-\033[m' * 30)


def cadastrar():
    """
        Função para cadastrar novas pessoas e caso a lista não tenha sido criado ele cria automaticamente
    :return:
    """
    from time import sleep

    titulo('NOVO CADASTRO')
    nome = input('Nome: ')
    idade = input('Idade: ')
    if not idade.isnumeric():
        while True:
            print('\033[1;31mERRO! Digite uma idade válida!\033[m')
            idade = input('Sua opção: ')
            if idade.isalnum():
                break
        idade = int(idade)
    lista = open('lista de cadastro/Cadastrados.txt', 'a')
    lista.write(f'{nome:20}'f'{idade:>5} anos\n')
    lista.close()
    print(f'Registro de {nome} adicionado')
    sleep(1)
    print('-' * 30)


def titulo(msg='0'):
    """
        Função que exibe os títulos
    :param msg: O titulo
    """
    print('\033[1;34m-' * 30)
    print(f'{msg: ^30}')
    print('\033[1;34m-\033[m' * 30)
