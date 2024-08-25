# listagem = (
#     'Lápis', 1.75,
#     'Borracha', 0.75,
#     'Caderno', 12.80,
#     'Livro', 31.55,
#     'Caneta', 2.50,
#     'Regua', 2.65,
#     'Apagador', 4.45,
#     'Mochila', 20.75,
#     'Compasso', 12.75,
# )

# print('-'*40)
# print(f'{"LISTAGEM DE PREÇOS":^40}')
# print('-'*40)

# for pos in range(0, len(listagem)):
#     if pos % 2  == 0:
#         print(f'{listagem[pos]:.<30}', end='')
#     else:
#         print(f'R${listagem[pos]:>7.2f}')

# print('-'*40)

palavras = ('gato', 'Rato', 'Barata', 'Escorpiao', 'Leao', 'Macaco', 'Tigre', 'Sapo')

for p in palavras:
    print(f'\nNa palavra {p} temos -> ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')