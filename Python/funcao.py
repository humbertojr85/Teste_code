res = 'S'
lista_numero = []
lista_maior = []
soma = quant = media = maior = menor = 0

while res in 'Ss':
    num = int(input('Digite um número: '))
    lista_numero.append(num)
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num >= maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma/ quant
print(f'Foram digitados {len(lista_numero)} números, essa é a lista {lista_numero}')
numeros = sorted(lista_numero)
print(f'A lista em ordem crecente é {numeros}')
numeros.reverse()
print(f'A lista ao contrario é {numeros}')

print(f'Você digitou {quant} númerose a média é {media}, sua soma é {soma} o Maior é {maior} e o menor é {menor}')
