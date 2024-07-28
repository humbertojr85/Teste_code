# #Funções:
# def fatorial(n, show=False):
#     """
#     - > Calcula o Fatorial de um Número.
#     :param n: O Número a ser calculado.
#     :param show: (Optional) Mostra ou não a conta.
#     :return: O valor do Fatorial de um Número n.
#     """
#     f = 1
#     for c in range(n, 0, -1):
#         if show:
#             print(c, end='')
#             if c > 1:
#                 print(' X ', end='')
#             else:
#                 print(' => ', end='')
#         f *= c
#     return f

# #função main:
# def main():
#     num = int(input('Digite um número para ver o seu fatorial: '))
#     conta = str(input('Quer ver a conta: [S/N]: ')).upper()
#     print(f'O fatorial de {num} => ', end='')
#     if conta == 'S':
#         print(f'{fatorial(num, show=True)}')
#     else:
#         print(f'{fatorial(num)}')

# #Iniciando a main:
# main()

n1 = 0
n2 = 1
num = int(input('Digite um número para saber se ele é de fibonacci: '))
cont = 3
n3 = 3
print('-='*30)
print(f'{n1} -> {n2}', end='')
while n3 <= num:
    n3 = n1 + n2
    print(f'-> {n3}', end='')
    n1 = n2
    n2 = n3
    cont += 1
print(' -> Fim')
print('-=')