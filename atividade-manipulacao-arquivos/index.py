from funcoes import *

programa = '[ + ] Programa executado [ + ]'

print('''
====== Qual time é teu? ======

[ 1 ] Responder Questionário
[ 2 ] Exibir Respostas
[ 3 ] Limpar Histórico
[ 4 ] Forçe uma excessão ('EOFError', 'ValueError', 'NameError', 'RuntimeError', 'KeyboardInterrupt')

==============================
''')

try:

	opc = input('Qual operação deseja realizar? ')

	if opc == '1':
		nome = input('Qual o seu nome? ')
		idade = input('Qual sua idade? ')
		time = input('Qual o seu time do coração? ')

		responder_questionario(nome, idade, time)

	elif opc == '2':
		exibir_historico()

	elif opc == '3':
		limpar_questionario()

	elif opc == 'EOFError':
		raise EOFError()
			
	elif opc == 'ValueError':
		raise ValueError()

	elif opc == 'NameError':
		raise NameError()

	elif opc == 'RuntimeError':
		raise RuntimeError()

	elif opc == 'KeyboardInterrupt':
		raise KeyboardInterrupt()

except EOFError:
	print("EOFError")
except ValueError:
	print("ValueError")
except NameError:
	print("NameError")
except RuntimeError:
	print("RuntimeError")
except KeyboardInterrupt:
	print('KeyboardInterrupt')
else:
	print("[ + ] Execução bem sucedida [ + ]")
finally:
	print(programa)