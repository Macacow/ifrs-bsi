from musica import Musica

class Playlist():
	"""A Classe Playlist pode contemplar músicas, além de adicioná-las e removê-las"""

	__slots__ = ['__nome', '__musicas']

	def __init__(self, nome:str):
		"""Método construtor da classe Playlist"""

		if not isinstance(nome, str):
			raise TypeError("O nome da playlist deve ser uma string")

		self.nome = nome
		self.__musicas = set()

	@property
	def musicas(self):
		return self.__musicas

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, n:str):
		if not hasattr(self, '__nome'):
			self.__nome = None

		if not isinstance(n, str):
			raise TypeError("O nome deve ser uma string")

		else:
			self.__nome = n

	def add_musica(self, m:Musica):
		if not isinstance(m, Musica):
			raise TypeError("A música deve ser um objeto da classe Musica")
		else:
			self.musicas.add(m)

	def remove_musica(self, m:Musica):
		if not isinstance(m, Musica):
			raise TypeError("A música deve ser um objeto da classe Musica")
		else:
			self.musicas.remove(m)

	def __str__(self):
		return __musicas