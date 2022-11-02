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


class CompleteReport:
    def generate(data: list):
        oldest_date = CompleteReport.__earliest_manufacturing(data)

        closets_date = CompleteReport.__closest_expiration_date(data)

        company_with_more = CompleteReport.__company_with_more_products(data)

        stocks = CompleteReport.__products_stocked_by_company(data)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closets_date}\n"
            f"Empresa com mais produtos: {company_with_more}\n"
            "Produtos estocados por empresa:\n"
            f"{stocks}"
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
            prd["data_de_validade"]
            for prd in data
            if datetime.fromisoformat(prd["data_de_validade"]) > today
        ]
        nearests_days_sorted = sorted(nearests_days)
        return nearests_days_sorted[0]

    def __company_with_more_products(data: list):
        cwm = [
            prd["nome_da_empresa"]
            for prd in data
            if prd["nome_da_empresa"] != ""
        ]
        cwm_most = Counter(cwm).most_common(1)
        company_with_more = cwm_most[0][0]
        return company_with_more

    def __products_stocked_by_company(data: list):
        stocks = [product["nome_da_empresa"] for product in data]
        qtd_product = Counter(stocks)
        stocks_report = ""
        for prd in qtd_product:
            stocks_report += f"- {prd}: {qtd_product[prd]}\n"

        return stocks_report


if __name__ == "__main__":
    data_list = []
    for i in range(15):
        prd = product_test()
        data_list.append(prd)

    print(CompleteReport.generate(data_list))
