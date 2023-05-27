from professor import Professor

professores = [Professor('1234567809', 'Deivison'), Professor('1224467809', 'Ricardo'), Professor('3216549877', 'Adair')]

professores[0].salario = 250.75

for professor in professores:
	print("Professor: {} | {}".format(professor.nome, professor.cpf))
	print("Salário: R${}".format(professor.salario))
	print("Total de Disciplinas: {}".format(len(professor.disciplinas)))
	print("=-"*10)