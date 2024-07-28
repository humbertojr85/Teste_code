def soma(numeros):
    soma = 0
    for num in numeros:
        soma += num
    return soma

def media(numeros):
    media = soma(numeros) 
    return media / len(numeros)


def main():

    lista_numeros = []

    while True:
        lista_numeros.append(int(input(f'Digite um número: ')))
        res = str(input('Quer continuar [S/N]: ')).upper()
        if res == 'N':
            break
        elif res != 'S':
            while res != 'SN':
                res = str(input('Digitação invalida Digite S/N: ')).upper()
                if res == 'S' or res == 'N':
                    break
            if res == 'N':
                break    
    
    somanum = soma(lista_numeros)
    med = media(lista_numeros)

    print(f'A soma dos numeros é >>> {somanum}, sua média é >>> {med}')
    print('-='*30)
    lista_numeros.sort(reverse=True)
    print(f'Você digitou {len(lista_numeros)} elementos')
    print(f'A lista em ordem decrecente ->>> {lista_numeros}')
    if 5 in lista_numeros:
        print(f'O valor 5 está na lista')
    else:
        print(f'O valor 5 não está na lista')

main()