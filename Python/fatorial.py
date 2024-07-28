def fatorial(numero):
    #Começando a verificação
    if numero < 1:
        return -1
    if numero == 1:
        return 1
    return numero * fatorial(numero-1)

def main():
    try:
        numero = int(input("Digite um numero para o calculo de fatorial: "))
        resultado = fatorial(numero)
        if resultado == -1:
            print("Fatorial não existe")
        else:
            print(f"O fatorial de {numero} é {resultado}")
    except ValueError:
        print("O valor digitado não é um numero")

main()