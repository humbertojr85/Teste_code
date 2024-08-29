from abc import abstractmethod,ABC

#Classe Animal:

class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    #@abstractmethod
    def fazer_som(self):
        print(f'O {self.nome} está fazendo som')

    def movimentar(self):
        print(f'O {self.nome} está se movimentando')


#SubClasse
class Mamifero(Animal):
    def __init__(self, nome, idade, tem_pelo):
        super().__init__(nome, idade)
        self.tem_pelo = tem_pelo

    def fazer_som(self):
        return print(f'O {self.nome} está rugindo')

#subClasse
class Ave(Animal):
    def __init__(self, nome, idade, pode_voar):
        super().__init__(nome, idade)
        self.pode_voar = pode_voar
    
    def movimentar(self):
        if self.pode_voar:
            print(f'A {self.nome} está voando')
        else:
            print(f'A {self.nome} está andando')

#Subclasse
class Reptil(Animal):
    def __init__(self, nome, idade, tipo_de_pele):
        super().__init__(nome, idade)
        self.tipo_de_pele = tipo_de_pele
    
    def movimentar(self):
        print(f'O {self.nome} está rastejando')

