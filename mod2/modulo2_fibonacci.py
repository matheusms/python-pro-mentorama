#Crie um objeto que gere a seq de Fibonacci
import pytest

class Fibonacci:
    def __init__(self, interacao):
        self.anterior = 0
        self.proximo = 1
        self.interacao = interacao
  
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.interacao == 0:
            return
        soma = self.anterior + self.proximo
        assert soma > self.anterior
        self.anterior = self.proximo
        self.proximo = soma
        self.interacao -= 1
        return self.proximo


elementos = int(input("Insira qtd de elementos: "))
u = Fibonacci(elementos) #iniciando a class
seq = iter(u) #iterando
var=[] #variavel para salvar a sequencia

for k in range(elementos): #rodando o programa
    var.append(next(u))

fibo = { k : v for k,v in enumerate(var)} #criando o dicionário por dict comprehension
print(fibo) #print da sequencia em forma de dicionário