"""
Funções de cálculo
"""


def moeda(n):
    """
        Formata o resultado para reais
    :param n: O valor atribuido
    :return: Retorna o valor formatado
    """
    return f'R${n:.2f}'


def aumentar(n, n2=0, form=False):
    """
        Aumenta o valor conforme a porcentagem escolhida
    :param n: Valor a ser aumentado
    :param n2: Porcentagem
    :param form: True para valor formatado e False para valor sem formatação
    :return: Retorna o valor aumentado
    """
    resul = n + n * (n2 / 100)
    if form:
        return moeda(resul)
    else:
        return resul


def diminuir(n=0, n2=0, form=False):
    """
        Diminui o valor conforme a porcentagem escolhida
    :param n: Valor a ser diminuido
    :param n2: Porcentagem
    :param form: True para valor formatado e False para valor sem formatação
    :return: Retorna o valor diminuido
    """
    resul = n - n * (n2 / 100)
    if form:
        return moeda(resul)
    else:
        return resul


def dobro(n, form=False):
    """
        Dobra o valor
    :param n: Valor a ser dobrado
    :param form: True para valor formatado e False para valor sem formatação
    :return: Retorna o valor dobrado
    """
    n *= 2
    if form:
        return moeda(n)
    else:
        return n


def metade(n, form=False):
    """
        Divide o valor na metade
    :param n: Valor a ser dividido
    :param form: True para valor formatado e False para valor sem formatação
    :return: Retorna o valor dividido
    """
    n /= 2
    if form:
        return moeda(n)
    else:
        return n
