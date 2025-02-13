"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""
numero1: int = int(input("Informe o primeiro número: "))
numero2: int = int(input("Informe o segundo número: "))

if numero1 > numero2:
    print(f"o primeiro número ({numero1} é maior que o segundo número ({numero2}))")
elif numero1 == numero2:
    print(f"Os números são iguais: número 1 ({numero1}), número 2 ({numero2})")
else:
    print(f"o segundo número ({numero2} é maior que o primeiro número ({numero1}))")

