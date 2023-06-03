from conta import Conta
from conta_especial import ContaEspecial
from poupanca import Poupanca
from conta_integrada import ContaIntegrada

contas = [
	Conta("Ricardo", saldo=500.0),
	ContaEspecial(limite=1000.0, titular="Adair"),
	Poupanca(saldo=9500.0, titular="Deivison"),
	ContaEspecial(limite=9000.0, saldo=100.0, titular="Lucas"),
	ContaEspecial(limite=9000.0, saldo=120.5, titular="Vitinho"),
	ContaIntegrada(titular="João", saldo=100.0, limite=5000.0),
	ContaIntegrada(titular="Yuri", saldo=500.75, limite=1000.0),
	ContaIntegrada(titular="Dudu", saldo=1000.0, limite=2500.0),
]

for conta in contas:
	print(conta)
	conta.sacar(1.0)
	print(conta)