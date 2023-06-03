class Cachorro:

	especie = "Canis lupus familiaris"
	nome = "Cachorro"

	slots = ['__raca']

	def __init__(self, raca:str):
		self.__raca = raca

	@property
	def raca(self) -> str:
		return self.__raca

	def latir(self) -> str:
		return "Au au"

	def __str__(self) -> str:
		return f"{self.raca}: {Cachorro.nome}"