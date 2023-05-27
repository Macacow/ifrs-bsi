class Ingresso():
	"""Classe ingresso"""

	def __init__(self, valor:float):
		self.__valor = valor

	@property
	def valor(self):
		return self.__valor
	
	@valor.setter
	def valor(self, novo_valor:float):
		if isinstance(novo_valor, float) and (self.__valor != novo_valor):
			self.__valor = novo_valor

	def __str__(self):
		return 'Classe Ingresso: R${}'.format(self.__valor)