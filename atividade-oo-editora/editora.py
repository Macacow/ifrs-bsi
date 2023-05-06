from livro import Livro
from datetime import date

class Editora():
	"""A classe editora contem e publica livros"""

	__slots__ = ['__cod', '__razao_social', '__nome_fantasia', '__email', '__livros']

	def __init__(self, cod:str, razao_social:str, nome_fantasia:str=None, email:str=None):
		"""Método Construtor da classe Editora"""

		self.cod = cod
		self.razao_social = razao_social
		self.nome_fantasia = nome_fantasia
		self.email = email

		self.__livros = set()

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
	def razao_social(self):
		return self.__razao_social

	@razao_social.setter
	def razao_social(self, rs:str):
		if not hasattr(self, '__razao_social'):
			self.__razao_social = None

		if not isinstance(rs, str):
			raise TypeError("A variável Razão Social deve ser do tipo string")

		else:
			self.__razao_social = rs


	@property
	def nome_fantasia(self):
		return self.__nome_fantasia

	@nome_fantasia.setter
	def nome_fantasia(self, ns:str):
		if not hasattr(self, '__nome_fantasia'):
			self.__nome_fantasia = None

		if not isinstance(ns, str):
			raise TypeError("A variável Nome Social deve ser do tipo string")

		else:
			self.__nome_fantasia = ns

	@property
	def email(self):
		return self.__email

	@email.setter
	def email(self, mail:str):
		if not hasattr(self, '__email'):
			self.__email = None

		if not isinstance(mail, str):
			raise TypeError("A variável Email deve ser do tipo string")

		else:
			self.__email = mail

	def __str__(self):
		return "Editora: {}\nRazão Social: {}\nNome Fantasia: {}\nEmail: {}\n\n".format(self.cod, self.razao_social, self.nome_fantasia, self.email)


	def listar_livros(self):
		return self.__livros

	def publicar(self,livro:Livro):
		
		if not isinstance(livro, Livro):
			raise TypeError("O livro deve ser um objeto da classe Livro")

		livro.publicacao = date.today()
		self.__livros.add(livro)
		