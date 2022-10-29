from tests.factories.product_factory import ProductFactory
from datetime import datetime


class SimpleReport:
    def generate(data: list):
        pass


if __name__ == "__main__":
    data_list = []
    for i in range(101):
        prd = ProductFactory()
        data_list.append(prd)

    hoje = datetime.now()
    mais_proximo = 10000
    for prd in data_list:
        # if datetime.fromisoformat(prd.data_de_validade) < hoje:
        #     status = "Vencido"
        #     dias_para_medalha = 0
        # else:
        #     status = "apto para consumo"
        #     dias_para_medalha = (
        #         datetime.fromisoformat(prd.data_de_validade) - hoje
        #     )
        # if (
        #     int(dias_para_medalha.days) < mais_proximo
        #     and status == "apto para consumo"
        # ):
        #     dt_mais_prox = prd.data_de_validade
        #     mais_proximo = dias_para_medalha

        print(
            f"""Produto: {prd.nome_do_produto}
Fabricação: {prd.data_de_fabricacao}
Validade: {prd.data_de_validade}
DT Validade: {datetime.fromisoformat(prd.data_de_validade)}
Data atual: {hoje}
"""
        )
