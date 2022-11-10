from funcoes import *

print('''
	====== Qual time é teu? ======
	[ 1 ] Responder Questionário
	[ 2 ] Exibir Respostas
	[ 3 ] Exibir Totalizador
	[ 4 ] Limpar Histórico e Totalizador
	==============================
	''')

opcao = int(input('Qual operação deseja realizar? '))

if opcao == 1:
	nome = input('Qual o seu nome? ')
	idade = input('Qual sua idade? ')
	time = input('Qual o seu time do coração? ')

	responder_questionario(nome, idade, time)

elif opcao == 2:
	exibir_historico()

elif opcao == 3:
	exibir_totalizador()

elif opcao == 4:
	limpar_questionario()

else:
	print("Tente novamente escolhendo uma opção válida!")
