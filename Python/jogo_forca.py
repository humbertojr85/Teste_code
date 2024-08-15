from random import choice
#Inicio Jogo da Forca:
###################################################
with open('lista_palavras.txt', 'r') as arquivo:
    palavras = arquivo.readlines()

#p_aleatoria = ['Casa', 'pytohn', 'java', 'cadeira']
palavra = choice(palavras).strip()
letras_usuario = []
letras_erradas = []
chances = 5
ganhou = False
nike = ''

print('       ','\033[1;31;41mJOGO DA FORCA\033[m')
print('-='*30)
nike = str(input('Digite seu Nome para Jogar: '))

while True:
    #Criar a logica
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=' ')
        else:
            print(' _ ', end=' ')
    print('\n','-='*30)
    print(f'Olá, {nike}, tenha um ótimo Jogo!')
    palpite_letra = str(input('Digite uma letra para adivinhar a palavra: '))
    letras_usuario.append(palpite_letra.lower())
    
    # Verificar se o usuario acertou ou errou:
    if palpite_letra.lower() not in palavra.lower():
        chances -= 1
        letras_erradas.append(palpite_letra.upper())
    print(f'Letras erradas até o momento: {letras_erradas}')
    print(f'Você tem \033[1;31;41m{chances}\033[m Chances')
    
    #Logica Ganhou
    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    # Verificar as Chances
    if chances == 0 or ganhou:
        break

if ganhou:
    print(f'\033[1;36;40mPARABÉN! Você ganhou a palava era {palavra}\033[m')

else:
    print(f'\033[1;31;40mNão foi dessa vez, você perdeu a palavra era {palavra}\033[m')