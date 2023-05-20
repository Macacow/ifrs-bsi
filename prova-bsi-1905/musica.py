from datetime import time

Artista = 'Artista'
Album = 'Album'

class Musica:
	"""Classe Música"""

	__slots__ = ['__nome', '__duracao', '__ano', '__compositor', '__interprete', '__compositores', '__interpretes', '__albuns']

	def __init__(self, nome:str, duracao:time, compositor:Artista, interprete:Artista):
		self.nome = nome
		self.duracao = duracao
		self.__compositor = compositor
		self.__interprete = interprete
		self.__interpretes = set()
		self.__compositores = set()
		self.__albuns = set()

		self.__compositores.add(self.__compositor)
		self.__interpretes.add(self.__interprete)

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
	def duracao(self) -> time:
		return self.__duracao

	@duracao.setter
	def duracao(self, dur):
		if not hasattr(self, '__duracao'):
			self.__duracao = None
		if isinstance(dur, time):
			self.__duracao = dur

		else:
			raise ValueError("A duração deve ser uma variável do tipo Time")

	def add_compositor(self, art:Artista):
		if art.__class__.__name__ == 'Artista':
			self.__compositores.add(art)
		else:
			raise ValueError("O compositor deve ser um objeto da classe Artista")
	
	def remove_compositor(self, art:Artista):
		if art.__class__.__name__ == 'Artista':
			self.__compositores.remove(art)
		else:
			raise ValueError("O compositor deve ser um objeto da classe Artista")

	def add_interprete(self, art:Artista):
		if art.__class__.__name__ == 'Artista':
			self.__interpretes.add(art)
		else:
			raise ValueError("O Interprete deve ser um objeto da classe Artista")
	
	def remove_interprete(self, art:Artista):
		if art.__class__.__name__ == 'Artista':
			self.__interpretes.remove(art)
		else:
			raise ValueError("O Artista deve ser um objeto da classe Artista")

	def add_album(self, alb : Album):
		if alb.__class__.__name__ == 'Album':
			self.__albuns.add(alb)
		else:
			raise ValueError("O Álbum deve ser um objeto da classe Album")

	def remove_album(self, alb : Album):
		if alb.__class__.__name__ == 'Album':
			self.__albuns.remove(alb)

	def tocar(self):
		for x in (self.__interpretes):
			x.play()

	def __str__(self):		
		return "{} ({}) - {}".format(self.__nome, self.__compositor, self.__interprete)

