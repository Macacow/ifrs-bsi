class Conta():
	"""Classe para uma conta simples
	Exemplo de Herança Múltipla"""

	__contas_ativas = 0
	__slots__ = ["__numero", "__titular", "__saldo"]

	def __init__(self, titular:str, saldo:float=0.0):
		self.__numero = Conta.__contas_ativas
		self.titular = titular
		self.saldo = saldo
		Conta.__contas_ativas += 1 # Atributo de classe

	@property
	def numero(self) -> int:
		return self.__numero
	
	@property
	def titular(self) -> str:
		return self.__titular
	
	@property
	def saldo(self) -> float:
		return self.__saldo
	
	@property
	def saldo_disponivel(self) ->float:
		return self.__saldo
	
	@saldo.setter
	def saldo(self, saldo:float):
		if not hasattr(self, "__saldo"):
			self.__saldo = 0.0
		if isinstance(saldo, (float,int)) and saldo >= 0:
			self.__saldo = saldo
		else:
			raise ValueError("Saldo não pode ser negativo")

	@titular.setter
	def titular(self, titular:str):
		if not hasattr(self, "__titular"):
			self.__titular = ""
		if isinstance(titular, str):
			if self.__titular != titular:
				self.__titular = titular
			else:
				raise ValueError("Não é possível alterar o titular para um de mesmo nome")
		else:
			raise ValueError("O novo titular deve ter um nome válido no formato String")


	def sacar(self, valor:float):
		if isinstance(valor, float):
			if valor < self.saldo_disponivel:
				self.saldo = self.saldo_disponivel - valor
			else:
				raise ValueError("Saldo Insuficiente")
		else:
			raise ValueError("Valor inválido")

	def __str__(self):
		return "Conta: {} | Titular {}: R${:.2f}".format(self.numero, self.titular, self.saldo)