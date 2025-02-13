"""
3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.
"""
numero: int = int(input("Informe o número: "))

if numero % 2 == 0:
    print(f"O número informado é par ({numero})")
else:
    print(f"O número informado é ímpar ({numero})")