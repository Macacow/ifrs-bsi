from datetime import date
from livro import Livro
from tipos import Pais

class Autor():
	"""A classe autor pode publicar livros e tal"""

	__slots__ = ['__nome', '__data_nascimento', '__pseudonimo', '__livros', '__pais']

	def __init__(self, nome:str, data_nascimento:date, pseudonimo:str=None, pais:Pais=None):
		"""Método Construtor da Classe Autor"""

		self.nome = nome
		self.data_nascimento = data_nascimento
		self.pseudonimo = pseudonimo

		self.__livros = set()

	@property
	def pais(self):
		if not hasattr(self, '__pais'):
			self.__pais = None

		if not isinstance(p, Pais):
			raise TypeError("O pais deve ser um Enum do tipo Pais")

		else:
			self.__pais = p	

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
			if len(n) >= 10 and len(n) <= 100:
				self.__nome = n
			else:
				raise ValueError("O Nome deve conter entre 10 e 100 caracteres")

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
			if len(pseudo) >= 3 and len(pseudo) <= 100:
				self.__pseudonimo = pseudo
			else:
				raise ValueError("O Psudônimo deve conter entre 3 e 100 caracteres")

	def adicionar_livro(self, livro:Livro):
		if not isinstance(livro, Livro):
			raise TypeError("O livro deve ser um objeto da classe Livro")
		self.__livros.add(livro)

	def get_livros(self):
		return self.__livros