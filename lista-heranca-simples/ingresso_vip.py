from ingresso import Ingresso

class Ingresso_Vip(Ingresso):
	"""Classe Ingresso Vip que herda a calsse Ingresso"""

	def __init__(self, valor_adicional:float):
		super().__init__(valor)

		self.__valor_adicional = valor

	@property
	def valor_adicional(self):
		return self.__valor_adicional
	