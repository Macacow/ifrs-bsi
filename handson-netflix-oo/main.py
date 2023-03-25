from perfil import Perfil

conta = []

perfil1 = Perfil("João", "Mickey Mouse")
perfil2 = Perfil("Ricardinho")
perfil3 = Perfil("Mariazinha", "Fotinho da Barbie", restrito=True)



perfil2.adicionar_lista("Westworld")
perfil2.adicionar_lista("Black Mirror")

perfil3.adicionar_lista("Barbie a Saga da Princesa")
perfil3.adicionar_lista("Dragon Ball Sei lá quall")
perfil3.assistir_serie("Marcha e Bugre")


conta.append(perfil1)
conta.append(perfil2)
conta.append(perfil3)

print("--- Perfis ---")
for perfil in conta:
	print(perfil, "\n")
	print(perfil1)

print("--- Excluindo Séries ---")

perfil2.remover_lista("Westworld")

print("--- Perfis ---")
for perfil in conta:
	print(perfil, "\n")