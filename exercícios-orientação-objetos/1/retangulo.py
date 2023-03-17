class Retangulo():
	"""Documentação para a Classe Retângulo"""

	def __init__(self, lado1:float, lado2:float):
		"""Método construtor de um objeto da classe Retângulo"""

		self.lado1 = lado1
		self.lado2 = lado2

	def calcularArea(self):
		area = self.lado1 * self.lado2
		return(area)

	def calcularPerimetro(self):
		perimetro = (2 * self.lado1) + (2 * self.lado2)
		return(perimetro)

	def __str__(self):
		return('Retângulo ({}/{}):\nPerímetro: {}\nÁrea: {}\n----------'.format(self.lado1, self.lado2, self.calcularPerimetro(), self.calcularArea()))