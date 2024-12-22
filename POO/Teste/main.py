from classes import Pessoa
from classes import PessoaJovem
from classes import PessoaVelha

def main():
    jovem = PessoaJovem("Ana", 20)
    #jovem.correr_rapido()

    velha = PessoaVelha("Maria", 80)
    # velha.sabedoria()
    # velha.falar('Jesus é meu Salvador')
    # velha.parar_falar()
    # velha.comer()

    while True:
       print ('''
        1 - Correr
        2 - Falar
        3 - Para de Falar
        4 - Comer
        5 - Para de Comer
        6 - Sair
        ''')
       res = int(input('Escolha sua opção'))
       if res == 1:
           jovem.correr_rapido()

main()