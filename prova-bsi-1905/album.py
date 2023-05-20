from datetime import date
from musica import Musica

Artista = 'Artista'

class Album():
	"""Classe Album"""

	__slots__ = ['__nome', '__artist', '__music', '__lancamento', '__ao_vivo', '__gravadora', '__musicas', '__artistas']

	def __init__(self, nome:str, artist:Artista, music:Musica):
		self.nome = nome
		self.__artist = artist
		self.__music = music
		self.__lancamento = None
		self.__gravadora = None
		self.__ao_vivo = None
		self.__musicas = set()
		self.__artistas = set()

		self.__artistas.add(self.__artist)
		self.__musicas.add(self.__music)

	@property
	def nome(self):
		return self.nome

	@nome.setter
	def nome(self, nome:str):
		if not hasattr(self, '__nome'):
			self.__nome = None
		if isinstance(nome, str):
			self.__nome = nome
		else:
			raise ValueError("O Nome deve ser uma String")

	@property
	def lancamento(self):
		return self.__lancamento
	
	@lancamento.setter
	def lancamento(self, lancamento:date):
		if not hasattr(self, '__lancamento'):
			self.lancamento = None
		if isinstance(lancamento, str):
			self.__lancamento = lancamento
		else:
			raise ValueError("O lançamento deve ser do tipo date")

	@property
	def ao_vivo(self):
		return self.ao_vivo
	
	@ao_vivo.setter
	def ao_vivo(self, ao_vivo:str):
		if not hasattr(self, '__ao_vivo'):
			self.__ao_vivo = None
		if isinstance(ao_vivo, str):
			self.__ao_vivo = ao_vivo
		else:
			raise ValueError("Informe se a música foi gravada ao vivo através de uma variável Booleana")

	@property
	def gravadora(self):
		return self.gravadora
	
	@gravadora.setter
	def gravadora(self, gravadora:str):
		if not hasattr(self, '__gravadora'):
			self.__gravadora = None
		if isinstance(gravadora, str):
			self.__gravadora = gravadora
		else:
			raise ValueError("A Gravadora deve ser uma String")

	@property
	def musicas(self) -> set:
		return self.__musicas

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

	def lancar(self, data:date):
		if not hasattr(self, '__lancamento'):
			self.__lancamento = None
		if isinstance(data, date):
			self.__lancamento = data
		else:
			raise ValueError("Por favor, insira uma Data")

	def __str__(self):
		texto = "{} ({})".format(self.__nome, self.__lancamento)
		for x in (self.__musicas):
			texto += '\n    {}'.format(x)
		return(texto)
