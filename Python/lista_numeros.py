def somar_valores(lista):
    soma = 0
    for numero in lista:
        soma = soma + numero
    return soma

def media_valores(lista):
    soma = somar_valores(lista)
    media = soma/len(lista)
    return media

def valores_maiores_media(lista):
    contador = 0
    media = media_valores(lista)
    for numero in lista:
        if numero > media:
            contador = contador + 1
    return contador

def valores_menor(lista, nota):
    contador = 0
    for numero in lista:
        if numero < nota:
            contador = contador + 1
    return contador

def main():
    lista_numeros = []
    numero = 0
    
    while numero != -1:
        numero = float(input("Digite um nota (-1 encerra...):"))
        if numero != -1:
            if numero < 0 or numero > 10:
                print("Nota invalida...")
            else:
                lista_numeros.append(numero)
        
    ## Questao A
    print("Quantidade de notas: ",len(lista_numeros))

    ## Questao B
    print("Mostrando todos os numeros na ordem digitadas: ")
    for numero in lista_numeros:
        print(numero, end=" ")
    print()

    ## Questao C
    print("Mostrando todos os numeros na ordem inversa: ")
    for i in range(len(lista_numeros)-1, -1, -1):
        print(lista_numeros[i], end=" ")

    # lista_inversa = []
    # for i in range(len(lista_numeros)):
    #     lista_inversa.insert(0, lista_numeros[i])

    # print(lista_inversa)

    ##Questao D
    soma = somar_valores(lista_numeros)
    print("A soma de todas as notas foi: ", soma)
    
    ##Questao E
    media = media_valores(lista_numeros)
    print(f'A media foi de {media:.2f}')

    ## Questao F
    quantidade = valores_maiores_media(lista_numeros)
    print("A quantidade de notas acima da média da turma foi: ", quantidade)

    ## Questao G
    quant_menor_sete = valores_menor(lista_numeros, 7)

main()