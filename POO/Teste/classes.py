# class Pessoa:
#     def __init__(self, nome, idade, falando=False, comendo=False):
#         self.nome = nome
#         self.idade = idade
#         self.falando = falando
#         self.comendo = comendo

#     def falar(self, palavras):
#         if self.falando:
#             print(f'{self.nome} já está falando')
#             return
#         print(f'{self.nome}, está falando -> {palavras}')
#         self.falando = True

#     def parar_de_falar(self):
#         if not self.falando:
#             print(f'{self.nome}, não está falando')
#             return
#         print(f'{self.nome}, parou de falar')
#         self.falando = False

class Pessoa:
    def __init__(self, nome, idade, falando=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo

    def falar(self, texto):
        if self.comendo:
            print(f"{self.nome} não pode falar enquanto está comendo.")
        elif self.falando:
            print(f"{self.nome} já está falando.")
        else:
            self.falando = True
            print(f"{self.nome} falou -> {texto}")

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome}, não está falando')
        else:
            self.falando = False
            print(f'{self.nome}, parou de falar')

    def comer(self):
        if self.falando:
            print(f"{self.nome} não pode comer enquanto está falando.")
        elif self.comendo:
            print(f"{self.nome} já está comendo.")
        else:
            self.comendo = True
            print(f"{self.nome} começou a comer.")

# Subclasse PessoaJovem
class PessoaJovem(Pessoa):
    def correr_rapido(self):
        print(f"{self.nome} está correndo rápido!")

# Subclasse PessoaVelha
class PessoaVelha(Pessoa):
    def sabedoria(self):
        print(f"{self.nome} está compartilhando sua sabedoria.")
