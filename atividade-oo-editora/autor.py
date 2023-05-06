from datetime import date
from livro import Livro
from tipos import Pais

class Autor():
	"""A classe autor pode publicar livros e tal"""

	__slots__ = ['__nome', '__data_nascimento', '__pseudonimo', '__livros']

	def __init__(self, nome:str, data_nascimento:date, pseudonimo:str=None):
		"""Método Construtor da Classe Autor"""

		self.nome = nome
		self.data_nascimento = data_nascimento
		self.pseudonimo = pseudonimo

		self.__livros = set()

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
	def data_nascimento(self):
		return self.__data_nascimento

	@data_nascimento.setter
	def data_nascimento(self, dn:date):
		if not hasattr(self, '__data_nascimento'):
			self.__data_nascimento = None

		if not isinstance(dn, date):
			raise TypeError("A data de nascimento deve ser uma variável do tipo date")

		else:
			self.__data_nascimento = dn

	@property
	def pseudonimo(self):
		return self.__pseudonimo

	@pseudonimo.setter
	def pseudonimo(self, pseudo:str):
		if not hasattr(self, '__pseudonimo'):
			self.__pseudonimo = None

		if not isinstance(pseudo, str):
			raise TypeError("O pseudônimo deve ser uma variável do tipo string")

		else:
			self.__pseudonimo = pseudo

	def adicionar_livro(self, livro:Livro):
		if not isinstance(livro, Livro):
			raise TypeError("O livro deve ser um objeto da classe Livro")
		self.__livros.add(livro)

	def get_livros(self):
		return self.__livros