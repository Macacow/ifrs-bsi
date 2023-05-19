from musica import Musica
from datetime import date

Musica = 'Musica'
Artista = 'Artista'

class Album():
    """Um album tem artista, músicas e outras cositas más :)"""

    __slots__ = ['__nome', '__lancamento', '__gravadora', '__sinopse', '__musicas','__artistas']

    def __init__(self, nome: str, gravadora: str):
        self.nome = nome
        self.__lancamento = None
        self.gravadora = gravadora
        self.__sinopse = None
        self.__musicas = set()
        self.__artistas = set()

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
            raise ValueError("O Nome deve ser uma String")
        
    @property
    def gravadora(self):
        return self.gravadora
    
    @gravadora.setter
    def gravadora(self, gravadora):
        if not hasattr(self, '__gravadora'):
            self.__gravadora = None
        if isinstance(gravadora, str):
            self.__gravadora = gravadora
        else:
            raise ValueError("A Gravadora deve ser uma String")
    
    @property
    def sinopse(self):
        return self.__sinopse

    @sinopse.setter
    def sinopse(self, sinopse):
        if not hasattr(self, '__sinopse'):
            self.__sinopse = None
        if isinstance(sinopse, str):
            self.sinopse = sinopse
        else:
            raise ValueError("A Sinopse deve ser uma String")

    @property
    def lancamento(self):
        return self.__lancamento

    @lancamento.setter
    def lancamento(self, lancamento: date):
        if not hasattr(self, 'lancamento'):
            self.__lancamento = None
        if isinstance(lancamento, str):
            self.lancamento = lancamento
        else:
            raise ValueError("O lançamento deve ser do tipo Date")
    
    def lancar(self, d :date):
        if isinstance(d, date):
            self.d = None
        else:
            raise ValueError("Por favor, insira uma Data")
    
    def add_musica(self, musi : Musica):
        if musi.__class__.__name__ == 'Musica':
            self.__musicas.add(musi)
        else:
            raise ValueError("A Música deve ser um objeto da classe Música")

    def remove_musica(self, musi : Musica):
        if musi.__class__.__name__ == 'Album':
            self.__musicas.add(musi)
        else:
            raise ValueError("A música deve ser um objeto da classe Música")
        
    def add_artista(self, art : Artista):
        if art.__class__.__name__ == 'Artista':
            self.__artistas.add(art)
        else:
            raise ValueError("O Artista deve ser um objeto da classe Artista")
    
    def remove_artista(self, art: Artista):
        if art.__class__.__name__ == 'Artista':
            self.__artistas.remove(art)
        else:
            raise ValueError("O Artista deve ser um objeto da classe Artista")
        
    