"""retirando a class pois nao era necessário
pelo pylint"""


def fizzbuzz(valor):
    """"função do módulo para calcular fizzbuzz"""
    resposta = ""
    if valor % 5 == 0:
        resposta += "fizz"

    if valor % 7 == 0:
        resposta += "buzz"

    if len(resposta) == 0:
        resposta += "miss"

    return resposta
