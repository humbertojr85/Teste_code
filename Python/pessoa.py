class Pessoa:
    def __init__(self, nome, idade, sexo, comendo=False, sorrindo=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.comendo = comendo
        self.sorrindo = sorrindo

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        
        print(f'{self.nome} \nsexo: {self.sexo} \nEstá comendo {alimento}')
        self.comendo = True