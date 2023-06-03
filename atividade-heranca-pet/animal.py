class Animal:

	slots = ['__nome', '__especie', '__vivo']

	def __init__(self, nome:str, especie:str):
		self.__nome = nome
		self.__especie = especie
		self.__vivo = True

	@property
	def nome(self) -> str:
		return self.__nome

	@property
	def especie(self) -> str:
		return self.__especie
	
	def __str__(self) -> str:
		condicao = self.verificar_vida()
		return f"{self.nome}: {self.especie}. Está {condicao}!"

	def morrer(self):
		self.__vivo = False

	def verificar_vida(self) -> str:
		return "Vivo(a)" if self.__vivo else "Morto(a)"