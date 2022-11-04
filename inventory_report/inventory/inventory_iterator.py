from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data: list):
        self.data = data
        self.index = 0

    def __next__(self):
        try:
            result = f"""
            Id: {self.data[self.index]['id']}
            Nome do produto: {self.data[self.index]['nome_do_produto']}
            Nome da empresa: {self.data[self.index]['nome_da_empresa']}
            Data de fabricação: {self.data[self.index]['data_de_fabricacao']}
            Data de Validade: {self.data[self.index]['data_de_validade']}
            Número de série: {self.data[self.index]['numero_de_serie']}
            Instruções de armazento:
            {self.data[self.index]['instrucoes_de_armazenamento']}
            """
            # result = self.data[self.index]['nome_da_empresa']
            self.index += 1
            return result
        except Exception:
            raise StopIteration
