class Carro():
	"""Documentação para a classe carro"""

	def __init__(self, marca, modelo, ano, placa, chassi, cor, cor_lateral, velocidade, consumo, tipo_combustivel):
		"""Método construtor de um objeto da classe Carro"""

		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.placa = placa
		self.chassi = chassi
		self.cor = cor
		self.cor_lateral = cor_lateral
		self.velocidade = velocidade
		self.consumo = consumo
		self.tipo_combustivel = tipo_combustivel


	def __str__(self):
		"""Método para retorno dos dados de um carro"""

		retorno = 'Carro: {} - {}\n'.format(self.marca, self.modelo)
		retorno += 'Identificação: {} - {}\n'.format(self.placa, self.chassi)
		retorno += 'Ano: {} | Velocidade: {} km/h\n'.format(self.ano, self.velocidade)
		retorno += 'Cores: {}, {}\n'.format(self.cor, self.cor_lateral)
		retorno += 'Consumo: {} de {} por km'.format(self.consumo, self.tipo_combustivel)
		return(retorno)

	def movimentar(self):
		"""Documentação do método"""
		pass

	def parar(self):
		"""Documentação do método"""
		pass

	def acelerar(self):
		"""Documentação do método"""
		pass

	def estacionar(self):
		"""Documentação do método"""
		pass

	def get_velocidade(self):
		"""Documentação do método"""
		pass

