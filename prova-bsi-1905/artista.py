from musica import Musica
from album import Album

class Artista:
    """Classe que gerencia os dados do Artista"""
    
    __slots__ = ['__nome', '__nascimento', '__plays', '__verificado']

    def __init__(self, nome :str):
        self.nome = nome
        self.__nascimento = None
        self.__plays = 0
        self.verificado = False

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nome):
        if not hasattr(self, '__nome'):
            self.__nome = None
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("o Nome deve ser uma String")

    @property
    def nascimento(self):
        return self.nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        if not hasattr(self, '__nascimento'):
            self.__nascimento = None
        if isinstance(nascimento, date):
            self.__nascimento = nascimento
        else:
            raise TypeError("o nascimento deve ser uma Date")

    @property
    def plays(self) -> int:
        return self.__plays

    @property
    def verificado(self):
        return self.verificado

    @verificado.setter
    def verificado(self, verificado):
        if not hasattr(self, '__verificado'):
            self.__verificado = None
        if isinstance(verificado, bool):
            self.__verificado = verificado
        else:
            raise TypeError("Por favor informe uma váriavel do tipo Booleano")

    def play(self):
        self.__plays += 1

    def exibir_plays(self):
        return "Artista: {} | Plays: {}".format(self.__nome, self.__plays)

    def __str__(self):
        return "{}".format(self.__nome)