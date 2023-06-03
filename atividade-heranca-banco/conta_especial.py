from conta import Conta

class ContaEspecial(Conta):
	__slots__ = ['__limite', '__uso_limite']

	def __init__(self, limite:float=0.0, **kwargs):
		saldo = (kwargs.get("saldo") or 0.0)
		self.__uso_limite = min(saldo, 0)
		saldo_calculado = limite + saldo
		if saldo_calculado >= 0 and saldo < 0:
			kwargs.update({
				"saldo": 0.0
			})
		if saldo_calculado < 0:
			raise ValueError("Limite Excedido")

		super().__init__(**kwargs)
		self.limite = limite

	@property
	def limite(self):
		return self.__limite
	
	@limite.setter
	def limite(self, limite:float):
		try:
			if not hasattr(self, "__limite"):
				self.__limite = 0.0
			if isinstance(limite, float):
				novo_saldo  = self.saldo_disponivel + limite
				if novo_saldo <= 0:
					self.__limite = limite
				else:
					raise ValueError("Conta com excesso sobre o limite")
		except Exception as e:
			raise e


	@property
	def saldo_disponivel(self):
		return self.limite + super().saldo_disponivel + self.__uso_limite

	@saldo_disponivel.setter
	def saldo_disponivel(self, saldo:float):
		if isintance(saldo, float) and saldo >= 0:
			super(Conta, self).__saldo = saldo
		else:
			raise ValueError("O Saldo não pode ser negativo")

	def sacar(self, valor:float):
		if isintance(valor, (float, int)):
			if valor < self.saldo_disponivel:
				if valor < super().saldo_disponivel:
					self.saldo = super().saldo_disponivel - valor
				else:
					self.__uso_limite = self.saldo - valor + self.__uso_limite
					self.saldo = 0
			else:
				raise ValueError("Saldo Insuficiente")
		else:
			raise ValueError("Valor inválido")

	def __str__(self):
		return f"Conta Especial: {self.numero}: - {self.titular} - R${self.saldo_disponivel:.2f}"
