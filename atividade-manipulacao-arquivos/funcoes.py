def responder_questionario(nome, idade, time):
	arquivo = open('historico-respostas.txt', 'a')
	arquivo.write(nome + ' | ' + idade + ' | ' + time + '\n')
	arquivo.close()

	arquivo = open('historico-respostas.txt', 'r')
	linhas = arquivo.readlines()
	arquivo.close()

	arquivo = open('totalizador-respostas.txt', 'a')

	for linha in linhas:
		dados = linha.split(' | ')
		#arquivo.write(dados[0] + ' | ' + dados[1] + ' | ' + str(dados[2]) + '\n')
	arquivo.close()

#====================================================================

def exibir_historico():
	arquivo = open('historico-respostas.txt', 'r')
	linhas = arquivo.readlines()

	for linha in linhas:
		print(linha, end = '')

	arquivo.close()

#====================================================================

def limpar_questionario():
	arquivo = open('historico-respostas.txt', 'w')
	arquivo.write('')
	arquivo.close()

	arquivo = open('totalizador-respostas.txt', 'w')
	arquivo.write('')
	arquivo.close()