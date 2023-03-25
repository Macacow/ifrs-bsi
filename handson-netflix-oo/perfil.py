class Perfil():
	"""A classe Perfil permite criar um perfil de usuário da Netflix. Uma conta pode conter diversos perfis."""

	quantidade_perfis = 0

	def __init__(self, nome, foto_perfil="Foto Padrão", lista=[], series_assistidas=[], restrito=False):
		"""Método construtor da classe Perfil.
		Caso nenhuma foto de perfil hipotética seja colocada, uma "Foto Padrão" será definida.
		Caso nenhuma série/filme seja adicionada à lista, ela é criada vazia.
		Caso não seja definida a restriçao, está será definida como fasa e todas as séries +12 serão liberadas
		Como o exercício tem apenas fins educativos, iremos trabalhar apenas com o termo 'série' (sem 'filmes') """

		if not isinstance(nome, str):
			raise TypeError("O nome deve ser uma string")

		if not isinstance(foto_perfil, str):
			raise TypeError("Defina uma string para representar uma foto de perfil")

		self.nome = nome
		self.foto_perfil = foto_perfil
		self.lista = []
		self.series_assistidas = []
		self.restrito = restrito

		Perfil.quantidade_perfis += 1

	def adicionar_lista(self, nome_serie):
		if not isinstance(nome_serie, str):
			raise TypeError("O nome da série deve ser uma string")
		else:
			self.lista.append(nome_serie)

	def assistir_serie(self, nome_serie):
		if not isinstance(nome_serie, str):
			raise TypeError("O nome da série deve ser uma string")
		else:
			self.series_assistidas.append(nome_serie)

	def remover_lista(self, nome_serie):
		if not isinstance(nome_serie, str):
			raise TypeError("O nome da série deve ser uma string")
		else:
			if nome_serie in self.lista:
				self.lista.remove(nome_serie)
			else:
				raise TypeError("A série selecionada não estava na sua lista :/")

	def __str__(self):
		"""Método padrão para o retorno das informações sobre o Perfil"""
		return f"Nome do Usuário: {self.nome}\nFoto de Perfil: {self.foto_perfil}\nLista de Séries: {self.lista}\nSéries Assistidas: {self.series_assistidas}\nPerfil com restrições de idade? {self.restrito}"

	def __del__(self):
		"""Método destrutor que decrementa o contador de perfis"""
		Perfil.quantidade_perfis -= 1