from datetime import datetime
from collections import Counter
from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory


def product_test():
    np = ProductFactory()
    produto = Product(
        np.id,
        np.nome_do_produto,
        np.nome_da_empresa,
        np.data_de_fabricacao,
        np.data_de_validade,
        np.numero_de_serie,
        np.instrucoes_de_armazenamento,
    )
    return {
        "id": produto.id,
        "nome_do_produto": produto.nome_do_produto,
        "nome_da_empresa": produto.nome_da_empresa,
        "data_de_fabricacao": produto.data_de_fabricacao,
        "data_de_validade": produto.data_de_validade,
        "numero_de_serie": produto.numero_de_serie,
        "instrucoes_de_armazenamento": produto.instrucoes_de_armazenamento,
    }


class SimpleReport:

    def generate(data: list):
        oldest_date = SimpleReport.__earliest_manufacturing(data)

        closets_date = SimpleReport.__closest_expiration_date(data)

        company_with_more = SimpleReport.__company_with_more_products(data)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closets_date}\n"
            f"Empresa com mais produtos: {company_with_more}"
        )

    def __earliest_manufacturing(data: list):
        oldest_date = [
            datetime.fromisoformat(prd["data_de_fabricacao"])
            for prd in data
            if prd["nome_da_empresa"] != ""
        ]

        return min(oldest_date).strftime("%Y-%m-%d")

    def __closest_expiration_date(data: list):
        today = datetime.now()
        nearests_days = [
            (
                (datetime.fromisoformat(prd["data_de_validade"]) - today).days,
                prd["data_de_validade"],
            )
            for prd in data
            if datetime.fromisoformat(prd["data_de_validade"]) > today
        ]

        nearest_day = nearests_days[0][0]
        for ind in range(len(nearests_days)):
            if nearests_days[ind][0] < nearest_day:
                nearest_day = nearests_days[ind][0]
                closets_date = nearests_days[ind][1]

        return closets_date

    def __company_with_more_products(data: list):
        cwm = [
            prd["nome_da_empresa"]
            for prd in data
            if prd["nome_da_empresa"] != ""
        ]
        cwm_most = Counter(cwm).most_common(1)
        company_with_more = cwm_most[0][0]
        return company_with_more


if __name__ == "__main__":
    data_list = []
    for i in range(150):
        prd = product_test()
        data_list.append(prd)

    print(SimpleReport.generate(data_list))
