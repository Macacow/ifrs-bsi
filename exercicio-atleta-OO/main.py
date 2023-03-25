from atleta import Atleta

comissao = []

atleta_rugby = Atleta("Ricardo", "2001-10-20", "Rugby")
atleta_ping = Atleta("Carlos", "2010-10-15", "Ping-Pong", "João")
atleta_futebol01 = Atleta("Kannemann", "1980-05-15", "Futebol", "Geromel")
atleta_futebol02 = Atleta("Geromel", "1990-03-02", "Futebol")

comissao.append(atleta_futebol01)
comissao.append(atleta_futebol02)
comissao.append(atleta_rugby)
comissao.append(atleta_ping)

print("------------- Atletas Profissionais Cadastrados -------------")
for atleta in comissao:
	print(atleta)

print("------------- Atletas Profissionais de Futebol -------------")
for atleta in comissao:
	if atleta.esporte == "Futebol":
		print(atleta)

print("------------- Total de integrantes da comissão -------------")
print("Atletas: {}".format(Atleta.quantidade_atletas))
print("Responsáveis: {}".format(Atleta.quantidade_responsaveis))
print("TOTAL: {}".format(Atleta.quantidade_atletas + Atleta.quantidade_responsaveis))

print("------------- Apagando um Objeto -------------")
comissao.remove(atleta_futebol02)
del(atleta_futebol02)

print("------------- Atletas Profissionais Cadastrados -------------")
for atleta in comissao:
	print(atleta)

print("------------- Atletas Profissionais de Futebol -------------")
for atleta in comissao:
	if atleta.esporte == "Futebol":
		print(atleta)

print("------------- Total de integrantes da comissão -------------")
print("Atletas: {}".format(Atleta.quantidade_atletas))
print("Responsáveis: {}".format(Atleta.quantidade_responsaveis))
print("TOTAL: {}".format(Atleta.quantidade_atletas + Atleta.quantidade_responsaveis))