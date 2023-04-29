from datetime import date


class Album():
	"""A classe Album comporta várias músicas, além de possuir um nome, data de lançamento, gravadora e uma sinopse"""
	
	__slots__ = ['__nome', '__lancamento', '__gravadora', '__sinopse']

	def __init__(self, 	nome:str, gravadora:str):
		"""Método construtor para um objeto da classe Album"""

		if not isinstance(nome, str):
			raise TypeError("O nome do álbum deve ser uma string")

		if not isinstance(lancamento, date):
			raise TypeError("A data de lançamento do álbum deve ser do tipo date")

		if not isinstance(gravadora, str):
			raise TypeError("O nome da gravadora deve ser uma string")

		self.nome = nome
		self.lancamento = None
		self.gravadora = gravadora
		self.sinopse = None

	def lancar(d:date):
		self.lancamento = d