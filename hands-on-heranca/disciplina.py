class Disciplina():
	"""Classe para mapear uma disciplina"""

	slots = ['__nome']

	def __init__(self, nome:str):
		self.nome = nome

	@property
	def nome(self):
		return self.__nome
	