print('-='*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-='*30)

num = int(input('Digite um numero para saber se ele está na sequência de Fibonacci: '))

n1 = 0
n2 = 1
print('-='*30)
print(f'{n1} -> {n2}', end='')

cont = 3

while True:
    n3 = n1 + n2
    print(f' -> {n3}', end='')
    n1 = n2
    n2 = n3
    cont += 1
    if n3 == num:
        print(f'\nO {num} está na sequência de Fibonacci')
        print('-='*30)
        break
    if n3 > num:
        print(' -> FIM')
        print(f'O {num} não está na sequência de Fibonacci')
        print('-='*30)
        break
