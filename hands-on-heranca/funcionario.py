class Funcionario():
	"""Classe para mapear um funcionário"""

	def __init__(self, nome:str, cpf:str, salario:float=0.0):
		self.__nome = nome
		self.__cpf = cpf
		self.__salario = salario

	@property
	def nome(self):
		return self.__nome
	
	@property
	def cpf(self):
		return self.__cpf
	
	@property
	def salario(self):
		return self.__salario
	
	@nome.setter
	def nome(self, novo_nome=str):
		if isinstance(novo_nome, str) and (novo_nome != self.__nome):
			self.__nome = novo_nome

	@cpf.setter
	def cpf(self, novo_cpf:str):
		if isinstance(novo_cpf, str) and len(novo_cpf) == 11:
			self.__cpf = novo_cpf

	@salario.setter
	def salario(self, novo_salario:float):
		if isinstance(novo_salario, float) and (novo_salario >= 0.0):
			self.__salario = novo_salario

