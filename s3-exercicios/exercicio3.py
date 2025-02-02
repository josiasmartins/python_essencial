"""
2. Faça um programa que recebe três valores e apresenta a soma dos quadrados dos valores lidos.
"""

valor1: int = int(input("Informe o primeiro valor: "))
valor2: int = int(input("Informe o segundo valor: "))
valor3: int = int(input("Informe o terceiro valor: "))

soma: int = (valor1 * valor1) + (valor2 * valor2) + (valor3 * valor3)

print(f"A soma dos números {valor1} com {valor2} e {valor3} é {soma}")