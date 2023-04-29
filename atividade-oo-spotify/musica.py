from datetime import time

class Musica():
	"""A classe Música possibilita o cadastro de uma música no Spotify. Uma música tem título, duração e quantidade de plays, além de métodos para tocar o som bacana"""

	__slots__ = ['__titulo', '__duracao', '__plays']
	
	def __init__(self, titulo:str, duracao:time):
		"""Método construtor da classe Música"""

		if not isinstance(titulo, str):
			raise TypeError("O Título da música deve ser uma string")

		if not isinstance(duracao, time):
			raise TypeError("A duração da música deve ser informada em uma variável do tipo time")

		self.titulo = titulo
		self.duracao = duracao
		self.__plays = 0

	@property
	def titulo(self):
		return self.__titulo

	@titulo.setter
	def titulo(self, t:str):
		if not hasattr(self, '__titulo'):
			self.__titulo = None

		if not isinstance(t, str):
			raise TypeError("O titulo deve ser uma string")

		else:
			self.__titulo = t

	@property
	def duracao(self):
		return self.__duracao

	@duracao.setter
	def duracao(self, d:time):
		if not hasattr(self, '__duracao'):
			self.__duracao = None

		if not isinstance(d, time):
			raise TypeError("A duracao deve ser uma variável do tipo time")

		else:
			self.__duracao = d


	def tocar():
		self.__plays += 1

