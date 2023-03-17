class Circulo():
	"""Documentação para a classe Círculo"""

	def __init__(self, raio:float):
		"""Método construtor de um objeto da classe Círculo"""
		self.raio = raio

	def calcularArea(self):
		area = raio * raio * 3.14
		print('Área: {:.2f}'.format(area))
	
	def __str__(self):
		return()