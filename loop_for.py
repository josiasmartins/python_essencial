"""
Looop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java

for (int i = 0; i < 10; i++) {
    // Execução do loop
}

Python

for item in interavel:
    // Execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis
- String
    nome = 'Geek University'
- Lista
    lista = [1, 2, 3, 4]
- Range
    numeros = range(1, 3, 4)


# Exemplo de for 1 (Iterando sobre uma string)

for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
range(valor_initial, valor_final)

OBS: O valor final não é inclusive.

for numero in range(1, 10):
    print(numero)

Enumerate:

((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), ...)

for indece, letra in enumerate(nome):
    print(nome[indece])

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)

nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor[1])

"""

nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor[1])