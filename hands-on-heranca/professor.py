from funcionario import Funcionario
from disciplina import Disciplina

class Professor(Funcionario):
	"""Classe Professor que herda a classe funcionário"""

	def __init__(self, nome:str, cpf:str, salario:float=0.0, disciplinas:list[Disciplina]=[]):
		super().__init__(cpf, nome, salario)
		self.__disciplinas = disciplinas

	@property
	def disciplinas(self):
		return self.__disciplinas
	
	@disciplinas.setter
	def disciplinas(self, disciplinas:Disciplina):
		"""Setter da propriedade disciplinas, verificando se todos os elementos passados são disciplinas"""

		if isinstance(disciplinas, list):
			continuar = True

			for disciplina in disciplinas:
				if not isinstance(disciplina, Disciplina):
					continuar = False
				if continuar:
					self.__disciplinas = disciplinas

		def add_disciplina(self, disciplina:Disciplina):
			"""Adiciona uma disciplina na lista e verifica seu tipo"""

			if isinstance(disciplina, Disciplina):
				self.__disciplinas.append(disciplina)

		def remove_disciplina(self, disciplina:Disciplina):
			"""Remove uma disciplina da lista, para tanto verifica seu tipo e a existância da lista"""

			if isinstance(disciplina.Disciplina) and (disciplina in self.__disciplinas):
				self.__disciplinas.remove(disciplina)