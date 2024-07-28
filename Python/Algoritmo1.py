n1 = input('Digite um Número: ')

# Verifica se o número é inteiro ou decimal
try:
    num = float(n1)

    if num.is_integer():
        num = int(num)
        if num % 2 == 0:
            paridade = "Par"
        else:
            paridade = "Ímpar"
        
        if num >= 0:
            sinal = "Positivo"
        else:
            sinal = "Negativo"
        
        print(f'O Número {num} é {paridade} e {sinal}')
    else:
        if num >= 0:
            sinal = "Positivo"
        else:
            sinal = "Negativo"
        
        print(f'O Número {num} é Decimal e {sinal}')
except ValueError:
    print("O valor digitado não é um número válido.")
