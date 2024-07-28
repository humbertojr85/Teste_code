# cadastro = {'nome': 'Humberto', 'fone': '1234-5678', 'endereço': 'Rua'}
# print(cadastro)

# cadastro ['nome'] = 'Alcântara'

# for k, v in cadastro.items():
#     print(f'{k}: {v}')

# produtos = dict()
# lista_compras = list()

# for i in range(0, 3):
#     produtos['Produto'] = str(input('Digite o nome do produto: '))
#     produtos['Preço'] = float(input('Digite o valor do produto: '))
#     lista_compras.append(produtos.copy())

# for p in lista_compras:
#     for k, v in p.items():
#         print(f'{k} {v}')
    
###################################################


#Inicio das lista
##########################################
# pessoa = {}
# lista_pessoas = []
# while True:
#     pessoa['Nome'] = str(input('Digite o Nome: '))
#     pessoa['Idade'] = int(input('Digite a idade: '))
#     pessoa['CPF'] = str(input('Digite o CPF: '))
#     lista_pessoas.append(pessoa.copy())
    
#     res = str(input('Cadastrado com sucesso, quer continuar [S/N]: ')).upper().strip()
#     if res == 'N':
#         break
#     if res == 'S':
#         continue
#     else:
#         print('Digitação errada')

# menor_idade = []
# maior_idade = []

# for pessoa in lista_pessoas:
#     if int(pessoa['Idade']) < 18:
#         menor_idade.append(pessoa)
#     else:
#         maior_idade.append(pessoa)
# print('-='*30)
# print('Lista completa')
# for pessoa in lista_pessoas:
#     print(pessoa)
# print('-='*30)
# print('Menor Idade:')
# for menor in menor_idade:
#     print(menor)
# print('-='*30)
# print('Maior Idade:')
# for maior in maior_idade:
#     print(maior)


#Inicio
##############################
# cadastro = {}
# lista_cadastro = []

# # Adicionando cadastros à lista
# cadastro = {'nome': 'Humberto', 'Idade': '23'}
# lista_cadastro.append(cadastro)

# cadastro = {'nome': 'Cristina', 'Idade': '12'}
# lista_cadastro.append(cadastro)

# cadastro = {'nome': 'Alcantara', 'Idade': '15'}
# lista_cadastro.append(cadastro)

# cadastro = {'nome': 'Aguiar', 'Idade': '34'}
# lista_cadastro.append(cadastro)

# print('Lista completa')
# for cadastro in lista_cadastro:
#     print(cadastro)

# # Criando lista para menores de idade
# menor_idade = []

# # Iterando sobre a lista de cadastros e filtrando menores de idade
# for cadastro in lista_cadastro:
#     if int(cadastro['Idade']) < 18:
#         menor_idade.append(cadastro)

# # Imprimindo cadastros de menores de idade
# print('-=' * 30)
# for menor in menor_idade:
#     print(menor)

#Teste Fatorial:

# def fatorial(valor, show=False):
#     if valor < 0:
#         return -1
#     if valor == 0:
#         return 1

#     resultado = 1
#     for n in range(valor, 0, -1):
#         resultado = resultado*n
#         if show:
#             if n == 1:
#                 print(f'{n} = {resultado}')
#             else:
#                 print(f'{n} x ',end='')

#     return resultado

# def main():
#     try:
#         numero = int(input("Digite um numero para o calculo de fatorial: "))
#         resultado = fatorial(numero, show=True)
#         if resultado == -1:
#             print("Fatorial não existe")
#         else:
#             print(f"O fatorial de {numero} é {resultado}")
#     except ValueError:
#         print("O valor digitado não é um numero")

# main()


def fatorial(numero):
    if numero < 1:
        return -1
    if numero == 1:
        return 1
    return numero * fatorial(numero-1)

try:
    num = int(input('Digite um número para calcula o seu fatorial: '))
    resultado = fatorial(num)
    if resultado <= 0:
        print(f'Fatorial não existe')
    else:
        print(f'O Fatorial de {num} é {resultado}')
except ValueError:
    print('O Valor digitado não é um número')