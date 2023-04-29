from datetime import date
from tipos import Pais, Genero

class Artista():
	"""A classe Artista pode lançar Álbuns e Músicas"""

	__slots__ = ['__nome', '__ativo', '__pais', '__genero']

	def __init__(self, nome:str):
		"""Método construtor da classe Artista"""

		self.nome = nome
		self.__ativo = True

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

	@property
	def pais(self):
		return self.__pais

	@pais.setter
	def pais(self, p:Pais):
		if not hasattr(self, '__pais'):
			self.__pais = None

		if not isinstance(p, Pais):
			raise TypeError("O país deve ser um objeto da classe Pais")

		else:
			self.__pais = p

	@property
	def genero(self):
		return self.__genero

	@genero.setter
	def genero(self, g:Genero):
		if not hasattr(self, '__genero'):
			self.__genero = None

		if not isinstance(g, Genero):
			raise TypeError("O gênero deve ser um objeto da classe Genero")

		else:
			self.__genero = g

	def __str__(self):
		return "Nome do Artista: {}\nPaís: {}".format(self.nome, self.__pais)