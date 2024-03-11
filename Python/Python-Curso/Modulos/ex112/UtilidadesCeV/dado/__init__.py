def leiadinheiro(valor):
    """
        Função para verificar se o valor é um número
    :param valor: valor a ser verificado
    :return: Retorna o valor quando for um número
    """
    num = input(valor).strip().replace(',', '.')
    if num.isnumeric():
        return float(num)
    else:
        if num.isalnum() or num == '':
            while True:

                print('\033[1;31mERRO! DIGITE UM NÚMERO VÁLIDO\033[m')
                num = input(valor).strip()
                if num.isnumeric():
                    return float(num)
        else:
            return float(num)
