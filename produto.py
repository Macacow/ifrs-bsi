class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def buscar(self, parametro):
        # Implementação padrão para busca por nome
        print("Realizando busca por nome:", parametro)

    def buscar(self, parametro, por_codigo):
        if por_codigo:
            # Implementação para busca por código
            print("Realizando busca por código:", parametro)
        else:
            # Implementação para busca por nome
            print("Realizando busca por nome:", parametro)

    def __str__(self):
        return f"Produto: {self.nome}, Preço: {self.preco}"