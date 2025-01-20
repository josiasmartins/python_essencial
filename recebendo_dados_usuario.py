"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, String é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angeline Jolie'
- Aspas duplas -> "Angeline Jolie"
- Aspas simples triplas -> '''Angeline Jolie'''
- Aspas duplas triplas -> tres_pas Angeline Jolie tres_aspas

"""
# Entrada de dados
# print("Qual seu nome?")
# nome = input() # Input -> Entrada

nome = input("Qual é seu nome?")

# Exemplo de print 'antigo' 2.x
# print("Seja bem vindo(a) %s" % nome)

# Exemplo de print 'moderno' 3.x
# print("Seja bem-vindo(a) {0}".format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

# print("Qual a sua idade?")
# idade = input()

idade = int(input("Qual a sua idade?"))


# Processamento

# Saída de dados
# Exemplo de print 'antigo' 2.x
# print("A %s tem %s anos" % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print("A {0} tem {1} anos".format(nome, idade))


# Exemplo de print 'mais atual' 3.7
print(f"A {nome} tem {2018 - int(idade)} anos")

