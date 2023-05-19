from datetime import time

Playlist = 'Playlist'
Album = 'Album'
Artista = 'Artistas'

class Musica:
    """Classe para criação de uma Musica."""

    __slots__ = ['__titulo', '__duracao', '__plays', '__playlists', '__albums', '__artistas']

    def __init__(self, titulo : str, duracao: time):
        self.titulo = titulo
        self.duracao= duracao
        self.__plays= 0
        self.__playlists = set()
        self.__albums = set()      
        self.__artistas = set()

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        if not hasattr(self, '__titulo'):
            self.__titulo = None
        if isinstance(titulo, str) and (3 <= len(titulo) <= 30):
            self.__titulo = titulo
        else:
            raise ValueError("O Titulo pode ter no máximo 20 caracteres")

    @property
    def duracao(self) -> time:
        return self.__duracao

    @duracao.setter
    def duracao(self, durcacao):
        if not hasattr(self, '__duracao'):
            self.__duracao = None
        if isinstance(durcacao, time):
            self.__duracao = durcacao

        else:
            raise ValueError("A duração deve ser uma variável do tipo Time")
    
    @property
    def plays(self) -> int:
        return self.__plays

    def __str__(self):
        mensagem = (f"Título: {self.titulo}, Duração: {self.duracao}, Reproduções: {self.plays}. \n")
        return mensagem

    def tocar(self):
        self.__plays += 1

    def add_playlist(self, p : Playlist):
        if p.__class__.__name__ == Playlist:
            self.__playlists.add(p)
        else:
            raise ValueError("A playlist deve ser um objeto da classe Playlist")
  
    def remove_playlist(self, p : 'Playlist'):
        if p.__class__.__name__ == 'Playlist':
            self.__playlists.remove(p)
        else:
            raise ValueError("A playlist deve ser um objeto da classe Playlist")

    def add_artista(self, art : Artista):
        if art.__class__.__name__ == 'Artista':
            self.__artistas.add(art)
        else:
            raise ValueError("O Artista deve ser um objeto da classe Artista")

    def remove_artista(self, art : Artista):
        if art.__class__.__name__ == 'Artista':
            self.__artistas.remove(art)
        else:
            raise ValueError("O Artista deve ser um objeto da classe Artista")

    def add_album(self, alb : Album):
        if alb.__class__.__name__ == 'Album':
            self.__albums.add(alb)
        else:
            raise ValueError("O Álbum deve ser um objeto da classe Album")

    def remove_album(self, alb : Album):
        if alb.__class__.__name__ == 'Album':
            self.__albums.remove(alb)
        else:
            raise ValueError("O Álbum deve ser um objeto da classe Album")