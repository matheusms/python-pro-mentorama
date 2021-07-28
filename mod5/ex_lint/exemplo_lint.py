"""
módulo principal
"""
from fizzbuzz import Calcular


def run():
    """
    Função principal para execução do fizzbuzz
    """
    while True:
        valor = input("Digite um número natural: ")
        if int(valor) < 0 or isinstance(valor, int):
            print("valor digitado não pertence ao grupo dos numeros naturais")
        else:
            break
        resultado = Calcular.fizzbuzz(int(valor))

    print(f"Para o numero digitado a resposta é {resultado}")


run()
