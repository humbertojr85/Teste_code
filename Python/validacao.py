#Funções:
def validar_impar_par(n):
    if n % 2 == 0:
        print('Número é Par, ', end='')
    else:
        print('Número é Impar, ', end='')
    return n

def validar_positivo_negativo(n):
    if n >= 0:
        print('Positivo ', end='')
    else:
        print('Negativo ', end='')
    return n

def validar_int_dec(n):
    if n == round(n):
        print('e Inteiro')
    else:
        print('e Decimal')
    return n
#função main:
def main():
    num = float(input('Digite um número: '))
    validar_impar_par(num)
    validar_positivo_negativo(num)
    validar_int_dec(num)

#Chamando o main:
main()