from conta import Conta

class Poupanca(Conta):

	__taxa = 0.0005

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	@property
	def saldo_disponivel(self):
		return self.saldo_disponivel + self.juros
	
	@property
	def juros(self) -> float:
		if super().saldo_disponivel > 0:
			return super().saldo_disponivel * Poupanca.__taxa
		else:
			return 0.0

	def __str__(self) -> str:
		return f"Conta Poupança: {self.numero}: -"\
				f" {self.titular} - R$ {self.saldo_disponivel:.2f}"