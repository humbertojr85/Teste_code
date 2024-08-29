from animal import Mamifero
from animal import Reptil
from animal import Ave


def main():
    cachorro = Mamifero('Cachorro', 3, True)

    cachorro.fazer_som()
    cachorro.movimentar()
    cachorro.linha()

    lagarto = Reptil('Lagarto', 7, 'liso')

    lagarto.fazer_som()
    lagarto.movimentar()
    lagarto.linha()

    passaro = Ave('Passaro', 4, True)

    passaro.fazer_som()
    passaro.movimentar()
    passaro.linha()

    passaro.pode_voar = False
    passaro.movimentar()

main()