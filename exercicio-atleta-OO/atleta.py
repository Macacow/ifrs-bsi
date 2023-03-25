from datetime import datetime

class Atleta():
	"""A classe atleta permite criar profissionais para diferentes esportes"""

	quantidade_atletas = 0
	quantidade_responsaveis = 0

	def __init__(self, nome, nascimento, esporte, responsavel=None):
		"""Método construtor para um atleta. Caso o atleta for menor de idade, é necessário definir um responsável"""
		
		if not isinstance(nome, str):
			raise TypeError("O Nome deve ser uma string")

		if not isinstance(nascimento, str):
			raise TypeError("O Nascimento deve ser uma string")

		if not isinstance(esporte, str):
			raise TypeError("O Esporte deve ser uma string")

		if (not isinstance(responsavel, str)) ^ (responsavel is None):
			raise TypeError("O Responsável deve ser uma string")

		try:
			nascimento = datetime.fromisoformat(nascimento)
			if ((datetime.today() - nascimento).days / 365.25) <= 18:
				if responsavel is None:	
					raise TypeError("Por favor, declare um responsável >:(")
			self.nome = nome
			self.esporte = esporte
			self.nascimento = nascimento
			self.responsavel = responsavel

			Atleta.quantidade_atletas += 1
			if self.responsavel is not None:
				Atleta.quantidade_responsaveis += 1

		except Exception as e:
			raise e

	def __str__(self):
		"""Método padrão para retorno de informações sobre um atleta"""
		if self.responsavel == None:
			return("{}: {}".format(self.nome, self.esporte))
		else:
			return("{} ({}): {}".format(self.nome, self.responsavel, self.esporte))
			
	def __del__(self):
		"""Método destrutor que decrementa o contador"""
		if self.responsavel is not None:
			Atleta.quantidade_responsaveis -=1
		Atleta.quantidade_atletas -= 1