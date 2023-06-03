from animal import Animal
from cachorro import Cachorro

class Pet(Animal, Cachorro):
	def __init__(self, apelido:str, raca:str = "Apenas um bom garoto"):
		Animal.__init__(self, Cachorro.nome, Cachorro.especie)
		Cachorro.__init__(self, raca)
		self.__apelido = apelido

	@property
	def apelido(self) -> str:
		return self.__apelido
	
	def __str__(self) -> str:
		return f"{self.apelido}\n"\
				f"{Cachorro.__str__(self)}\n"\
				f"{Animal.__str__(self)}"
