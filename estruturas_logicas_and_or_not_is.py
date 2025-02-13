"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operaradores unitários:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor booleano é invertida, ou seja, se for True, vira False, se for False, vira True
Para o 'is', o valor é comparado com o segundo.

"""
ativo = False
logado = True

# Se não estiver ativo
if ativo:
    print("Seja bem-vindo")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")

# Ativo é verdadeiro
print(ativo is True)
