from musica import Musica

class Playlist:
    """Classe para a criação de uma Playlist"""

    __slots__= ['__nome','__musicas',]

    def __init__(self, nome : str):
        self.__nome = nome
        self.__musicas = set()


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not hasattr(self, '__nome'):
            self.__nome = None
        if isinstance(nome , str):
            self.__nome = nome
        else:
            TypeError("O Titulo deve conter no máximo 20 caracteres :()")

    @property
    def musicas(self) -> set:
        return self.__musicas
    
    def add_musica(self, m : Musica):
        if isinstance(m, Musica):
            if m in self.__musicas:
                raise ValueError("Esta música já existe nesta Playlist")
            else:
                self.__musicas.add(m)
        else:
            raise ValueError("A Música deve ser um objeto do tipo Música")

    def remove_musica(self, m :Musica):
        if isinstance(m, Musica):
            if m in self.__musicas:
                self.__musicas.remove(m)
            else:
                raise ValueError("Esta música não existe nesta Playlist")
        else:
            raise ValueError("A Música deve ser um objeto da classe Música")
        
    def __str__(self):
        return self.nome