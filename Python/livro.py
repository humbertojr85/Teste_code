class Livro():
    def __init__(self, titulo, autor, ano, editora='Não informado'):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editora = editora
    
    def listar_livros(self):
        return [self.titulo, self.autor, self.ano, self.editora]