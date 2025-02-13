"""
Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
"""

numero: int = int(input("Digite o número: "))

if numero >= 0:
    raizQuadrada = numero * numero
    print(f"A raiz quadrada do número ({numero}) é {raizQuadrada}")
else:
    print(" O número fornecido é inválido.")