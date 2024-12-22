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


# def fatorial(numero):
#     if numero < 1:
#         return -1
#     if numero == 1:
#         return 1
#     return numero * fatorial(numero-1)

# try:
#     num = int(input('Digite um número para calcula o seu fatorial: '))
#     resultado = fatorial(num)
#     if resultado <= 0:
#         print(f'Fatorial não existe')
#     else:
#         print(f'O Fatorial de {num} é {resultado}')
# except ValueError:
#     print('O Valor digitado não é um número')

import pygame
import random
import sys

# Inicializar o Pygame
pygame.init()

# Dimensões da tela
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("🎉 Bingo de Final de Ano 🎉")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (200, 50, 50)
AMARELO = (255, 200, 0)
AZUL = (50, 100, 200)

# Fonte
FONTE_GRANDE = pygame.font.Font(None, 100)
FONTE_MEDIA = pygame.font.Font(None, 50)
FONTE_PEQUENA = pygame.font.Font(None, 30)

# Sons
pygame.mixer.init()
#SOM_BINGO = pygame.mixer.Sound("chime.wav")  # Coloque o caminho de um som aqui

# Gerar números de bingo
numeros = list(range(1, 76))
random.shuffle(numeros)
numeros_chamados = []

# Função para exibir texto na tela
def exibir_texto(texto, fonte, cor, x, y):
    superficie = fonte.render(texto, True, cor)
    retangulo = superficie.get_rect(center=(x, y))
    TELA.blit(superficie, retangulo)

# Função principal
def main():
    rodando = True
    numero_atual = None

    while rodando:
        TELA.fill(BRANCO)

        # Título
        exibir_texto("🎉 Bingo de Final de Ano 🎉", FONTE_MEDIA, AZUL, LARGURA // 2, 50)

        # Mostrar o número atual
        if numero_atual is not None:
            exibir_texto(f"Número: {numero_atual}", FONTE_GRANDE, VERMELHO, LARGURA // 2, ALTURA // 2 - 50)

        # Instruções
        exibir_texto("Pressione ESPAÇO para chamar o próximo número", FONTE_PEQUENA, PRETO, LARGURA // 2, ALTURA - 100)

        # Números chamados
        exibir_texto("Números chamados:", FONTE_PEQUENA, AZUL, LARGURA // 2, ALTURA - 250)
        exibir_texto(", ".join(map(str, numeros_chamados[-10:])), FONTE_PEQUENA, PRETO, LARGURA // 2, ALTURA - 200)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and numeros:
                    # Chamar o próximo número
                    numero_atual = numeros.pop(0)
                    numeros_chamados.append(numero_atual)
                    #SOM_BINGO.play()
                elif not numeros:
                    exibir_texto("Todos os números foram chamados!", FONTE_PEQUENA, VERMELHO, LARGURA // 2, ALTURA - 150)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Executar o programa
if __name__ == "__main__":
    main()
