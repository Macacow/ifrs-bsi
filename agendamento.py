class Agendamento:
    def __init__(self, cliente, animal, servico, data):
        self.cliente = cliente
        self.animal = animal
        self.servico = servico
        self.data = data
        self.concluido = False

    def concluir_servico(self):
        self.concluido = True
        # Outras ações para concluir o serviço, se necessário

    def __del__(self):
        if self.concluido:
            print("Serviço concluído:", self.servico.nome)
            print("Data e hora de conclusão:", self.data)
        else:
            print("Agendamento de serviço não concluído:", self.servico.nome)