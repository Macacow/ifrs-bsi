class Animal:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

class Cao(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, "Cão", idade)
        self.raca = raca

class Gato(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, "Gato", idade)
        self.cor = cor

class Passaro(Animal):
    def __init__(self, nome, idade, especie):
        super().__init__(nome, "Pássaro", idade)
        self.especie = especie