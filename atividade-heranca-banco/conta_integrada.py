from conta_especial import ContaEspecial
from poupanca import Poupanca

class ContaIntegrada(ContaEspecial, Poupanca):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	@property
	def saldo_disponivel(self) -> float:
		return super().saldo_disponivel
	
	def __str__(self) -> str:
		return f"Conta Integrada: {self.numero}: - "\
				f"{self.titular} - R${self.saldo_disponivel:.2f}"