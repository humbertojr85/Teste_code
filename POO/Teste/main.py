from classes import Pessoa
from classes import PessoaJovem
from classes import PessoaVelha

def main():
    jovem = PessoaJovem("Ana", 20)
    jovem.correr_rapido()

    velha = PessoaVelha("Maria", 80)
    velha.sabedoria()
    velha.falar('Jesus é meu Salvador')
    velha.parar_falar()
    velha.comer()

main()