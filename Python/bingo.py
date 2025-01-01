import pygame
import random
import sys
import pyttsx3

# Inicializar o mecanismo de texto para fala
voz = pyttsx3.init()

# Configurar a voz (opcional)
voz.setProperty('rate', 200)  # Velocidade da fala
voz.setProperty('volume', 2.0)  # Volume (1.0 = máximo)

# Função para falar o número sorteado
def falar_numero(numero):
    if numero % 10 == 0:
        texto = f"De Rombo {numero}"
    else:
        texto = f"Bola número {numero}"
    pygame.mixer.music.stop()
    voz.say(texto)
    voz.runAndWait()
    pygame.mixer.music.play(-1)

# Inicializar o Pygame
pygame.init()

# Dimensões da tela
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("🎉 O melhor Jogo de Bingo Feito por Humberto 🎉")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (200, 50, 50)
AZUL = (50, 100, 200)
VERDE = (50, 200, 50)
CORES_FOGOS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255)
]

# Fonte
FONTE_GRANDE = pygame.font.Font(None, 150)
FONTE_MEDIA = pygame.font.Font(None, 70)
FONTE_PEQUENA = pygame.font.Font(None, 40)

# Sons
pygame.mixer.init()
SOM_FUNDO = pygame.mixer.music.load("audio/fundo3.mp3")
SOM_FUNDO = pygame.mixer.music.play(-1)
SOM_BINGO = pygame.mixer.Sound("audio/ding.mp3")
SOM_FOGOS = pygame.mixer.Sound("audio/fogos.mp3")

# Imagem de fundo
IMAGEM_FUNDO = pygame.image.load("imagem/imagem.jpg")  # Substitua pelo caminho da imagem
IMAGEM_FUNDO = pygame.transform.scale(IMAGEM_FUNDO, (LARGURA, ALTURA))

# Gerar números de bingo
numeros = list(range(1, 90))
random.shuffle(numeros)
numeros_chamados = []

# Função para exibir texto na tela
def exibir_texto(texto, fonte, cor, x, y):
    superficie = fonte.render(texto, True, cor)
    retangulo = superficie.get_rect(center=(x, y))
    TELA.blit(superficie, retangulo)

# Função para desenhar fogos de artifício
def desenhar_fogos():
    for _ in range(50):
        x = random.randint(0, LARGURA)
        y = random.randint(0, ALTURA)
        cor = random.choice(CORES_FOGOS)
        pygame.draw.circle(TELA, cor, (x, y), random.randint(5, 10))

# Função principal
def main():
    rodando = True
    ganhador = False
    numero_atual = None

    while rodando:
        if ganhador:
            TELA.fill(PRETO)  # Tela escura para o ganhador
        else:
            TELA.blit(IMAGEM_FUNDO, (0, 0))  # Exibir imagem de fundo

        # Título
        exibir_texto("Bingo de Final de Ano", FONTE_MEDIA, PRETO, LARGURA // 2, 350)

        if ganhador:
            # Exibir a última bola chamada em destaque
            exibir_texto(f"Última bola: {numero_atual}", FONTE_GRANDE, VERMELHO, LARGURA // 2, 290)

            # Listar as demais bolas chamadas abaixo
            y_pos = 350
            x_pos = 50
            for i, numero in enumerate(numeros_chamados[:-1]):  # Excluir a última bola
                exibir_texto(f"{numero:02}", FONTE_PEQUENA, BRANCO, x_pos, y_pos)
                x_pos += 60
                if (i + 1) % 15 == 0:  # Nova linha a cada 15 números
                    x_pos = 50
                    y_pos += 50

            # Efeito de fogos
            desenhar_fogos()
            exibir_texto("🎊 Temos um ganhador! Pressione ESC para sair. 🎊", FONTE_PEQUENA, VERDE, LARGURA // 2, ALTURA - 50)

        else:
            # Mostrar o número atual
            if numero_atual is not None:
                exibir_texto(f"Bola: {numero_atual}", FONTE_MEDIA, VERMELHO, LARGURA // 2, 400)

            # Mostrar todos os números chamados
            y_pos = 450
            x_pos = 50
            for i, numero in enumerate(numeros_chamados):
                cor = VERMELHO if numero == numero_atual else PRETO
                exibir_texto(f"{numero:02}", FONTE_PEQUENA, cor, x_pos, y_pos)
                x_pos += 50
                if (i + 1) % 15 == 0:  # Nova linha a cada 15 números
                    x_pos = 50
                    y_pos += 40

            # Instruções
            #exibir_texto("ESPAÇO p/ chamar o próximo número ou ENTER p/ ganhador", FONTE_PEQUENA, PRETO, LARGURA // 2, ALTURA - 50)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and numeros and not ganhador:
                    # Chamar o próximo número
                    numero_atual = numeros.pop(0)
                    numeros_chamados.append(numero_atual)
                    SOM_BINGO.play()

                    # Falar o número sorteado
                    falar_numero(numero_atual)
                elif evento.key == pygame.K_RETURN and numero_atual is not None:
                    # Declarar ganhador
                    ganhador = True
                    pygame.mixer.music.stop()
                    SOM_FOGOS.play()
                elif evento.key == pygame.K_ESCAPE and ganhador:
                    # Sair após ganhador
                    rodando = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Executar o programa
if __name__ == "__main__":
    main()
