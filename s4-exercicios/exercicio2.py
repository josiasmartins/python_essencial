"""
Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
"""

from math import sqrt

numero: int = int(input("Digite o número: "))

if numero >= 0:
    print(f"A raiz quadrada do número ({numero}) é {sqrt(numero)}")
else:
    print(" O número fornecido é inválido.")