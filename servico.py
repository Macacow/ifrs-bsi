class Servico:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Banho(Servico):
    def __init__(self):
        super().__init__("Banho", 30.0)
        self.duracao = 60  # minutos

    def agendar(self, animal):
        # Lógica para agendar o serviço de banho para o animal
        print("Agendando banho para o animal:", animal.nome)

class Tosa(Servico):
    def __init__(self):
        super().__init__("Tosa", 50.0)
        self.duracao = 90  # minutos

    def agendar(self, animal):
        # Lógica para agendar o serviço de tosa para o animal
        print("Agendando tosa para o animal:", animal.nome)

class ConsultaVeterinária(Servico):
    def __init__(self):
        super().__init__("Consulta", 100.0)
        self.duracao = 45 #minutos

    def agendar(self, animal):
        # Lógica para agendar o serviço de tosa para o animal
        print("Agendando consulta veterinária para o animal: ", animal.nome)
        