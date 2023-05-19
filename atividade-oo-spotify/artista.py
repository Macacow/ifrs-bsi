from musica import Musica
from album import Album
from tipos import Pais,Genero

class Artista:
    """Classe que gerencia os dados do Artista"""
    
    __slots__ = ['__nome','__ativo','__genero', '__musicas','__pais']

    def __init__(self, nome :str, ativo : bool, pais : Pais, genero: Genero):
        self.nome = nome
        self.ativo= ativo
        self.__genero = genero
        self.__musicas = set()
        self.__pais = pais

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
    def ativo(self):
        return self.ativo

    @ativo.setter
    def ativo(self, ativo):
        if not hasattr(self, '__ativo'):
            self.__ativo = None
        if isinstance(ativo, bool):
            self.__ativo = ativo
        else:
            raise TypeError("Por favor informe uma váriavel do tipo Booleano")

    def __str__(self):
        return f"{self.nome}"

    @property
    def genero(self):
        return self.genero

    @genero.setter
    def genero(self, g : Genero):
        if not hasattr(self, '__genero'):
            self.genero = None
        if isinstance(g , Genero):
            self.genero = g
        else:
            raise TypeError("O gênero deve respeitar a tabelinha de generos lá do tipos né meu")

    def add_musica(self, m : Musica):
        if m.__class__.__name__ == 'Musica':
            self.__musicas.add(m)
        else:
            raise ValueError("A Música deve ser um objeto da classe Musica")

    def remove_musica(self, m : 'Musica'):
        if m.__class__.__name__ == 'Musica':
            self.__musicas.remove(m)
        else:
            raise ValueError("A Música deve ser um obejto da classe Musica")

    def add_album(self, alb : Album):
        if alb.__class__.__name__ == 'Album':
            self.__musicas.add(alb)
        else:
            raise ValueError("O Álbum deve ser u objeto da classe Album")

    def remove_album(self, alb : Album):
        if alb.__class__.__name__ == 'Album':
            self.__musicas.remove(alb)
        else:
            raise ValueError("O Álbum deve ser u objeto da classe Album")