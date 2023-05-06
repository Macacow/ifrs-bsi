from datetime import date
from tipos import Genero

Autor = "Autor"

class Livro():
	"""Classe livro né"""

	__slots__ = ['__cod', '__titulo', '__resumo', '__isbn', '__publicacao', '__autores']

	def __init__(self, cod:str, isbn:str):
		"""Método Construtor da classe Livro"""

		self.cod = cod
		self.titulo = ''
		self.resumo = ''
		self.isbn = isbn

		self.__autores = set()

	@property
	def cod(self):
		return self.__cod

	@cod.setter
	def cod(self, c:str):
		if not hasattr(self, '__cod'):
			self.__cod = None

		if not isinstance(c, str):
			raise TypeError("O Código deve ser uma string")

		else:
			self.__cod = c

	@property
	def titulo(self):
		return self.__titulo

	@titulo.setter
	def titulo(self, title:str):
		if not hasattr(self, '__titulo'):
			self.__titulo = None

		if not isinstance(title, str):
			raise TypeError("O Título deve ser uma variável do tipo string")

		else:
			self.__titulo = title

	@property
	def resumo(self):
		return self.__resumo

	@resumo.setter
	def resumo(self, resum:str):
		if not hasattr(self, '__resumo'):
			self.__resumo = None

		if not isinstance(resum, str):
			raise TypeError("O Resumo deve ser uma variável do tipo string")

		else:
			self.__resumo = resum

	@property
	def isbn(self):
		return self.__isbn

	@isbn.setter
	def isbn(self, i:str):
		if not hasattr(self, '__isbn'):
			self.__isbn = None

		if not isinstance(i, str):
			raise TypeError("O ISBN deve ser uma variável do tipo string")

		else:
			self.__isbn = i

	@property
	def titulo(self):
		return self.__titulo

	@titulo.setter
	def titulo(self, title:str):
		if not hasattr(self, '__titulo'):
			self.__titulo = None

		if not isinstance(title, str):
			raise TypeError("O Título deve ser uma variável do tipo string")

		else:
			self.__titulo = title

	@property
	def publicacao(self):
		if hasattr(self, '__publicacao'):
			return self.__publicacao
		else:
			return "Livro ainda não publicado"

	@publicacao.setter
	def publicacao(self, publi:date):
		if not hasattr(self, '__publicacao'):
			self.__publicacao = None

		if not isinstance(publi, date):
			raise TypeError("A Publicação deve ser uma variável do tipo date")

		else:
			self.__publicacao = publi

	def __str__(self):
		return "{} | {}\nData de Publicação: {} | {}\n{}".format(self.titulo, self.cod, self.publicacao, self.isbn, self.resumo)

	def listar_autores(self):
		return self.__autores

	def add_autor(self, a:Autor):
		if a.__class__.__name__ != Autor:
			raise TypeError("O autor deve ser um objeto da classe Autor")

		self.__autores.add(a)

	def remove_autor(self, a:Autor):
		if a in self.__autores:
			self.__autores.remove(a)