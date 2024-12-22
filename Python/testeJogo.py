from random import choice

palavras = ['casa', 'python', 'Amor', 'praia']

palavraAleatoria = choice(palavras).strip().lower()

letras_usuario = []

while True:
    palavra_completa = True

    for letra in palavraAleatoria:
        if letra in letras_usuario:
            print(letra, end=' ')
        else:
            print(' _', end=' ')
            palavra_completa = False
        print()

        if palavra_completa:
            print('Parabéns! A palavra está correta', palavraAleatoria)
            break

        palpite = input('Digite uma letra para acertar a palavra: ').strip().lower()

        if len(palpite) != 1:
            print("Erro: Vc não pode digitar mais de uma letra")
            continue
        if palpite in letras_usuario:
            print("Vc já tentou essa letra. Tente outra.")
            continue

        letras_usuario.append(palpite.lower())
