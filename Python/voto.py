#Funções:
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'tem {idade} anos: Não VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'tem {idade} anos: O VOTO OPCIONAL.'
    else:
        return f'tem {idade} anos: O VOTO OBRIGATORIO.'

#função main:
def main():
    print('-='*20)
    ano = int(input('Qual o ano do nascimento da pessoa: '))
    print('-='*20)
    print(f'A pessoa que nasceu no ano {ano}, {voto(ano)}')
    print('-='*20)

#Inicio main:
main()