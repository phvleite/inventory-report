from tests.factories.product_factory import ProductFactory
from datetime import datetime


class SimpleReport:
    def generate(data: list):
        oldest_date = SimpleReport.__earliest_manufacturing(data)

        closets_date = SimpleReport.__closest_expiration_date(data).strftime(
            "%Y-%m-%d"
        )

        company_with_more = SimpleReport.__company_with_more_products(data)

        oldest = oldest_date['data_de_fabricacao']
        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {closets_date}\n"
            f"Empresa com mais produtos: {company_with_more}"
        )

    def __earliest_manufacturing(data: list):
        oldest_date = datetime.fromisoformat(data[0].data_de_fabricacao)

        for prd in data:
            if prd.nome_da_empresa != "":
                if (
                    datetime.fromisoformat(prd.data_de_fabricacao)
                    < oldest_date
                ):
                    oldest_date = datetime.fromisoformat(
                        prd.data_de_fabricacao
                    )

        return {"data_de_fabricacao": oldest_date.strftime("%Y-%m-%d")}

    def __closest_expiration_date(data: list):
        closets_date = datetime.fromisoformat(data[0].data_de_validade)
        today = datetime.now()
        nearets_days = (
            datetime.fromisoformat(data[0].data_de_validade) - today
        ).days

        for prd in data:
            if (
                datetime.fromisoformat(prd.data_de_validade) > today
                and prd.nome_da_empresa != ""
            ):
                qtd_days = (
                    datetime.fromisoformat(prd.data_de_validade) - today
                ).days
                if qtd_days < nearets_days:
                    nearets_days = qtd_days
                    closets_date = datetime.fromisoformat(prd.data_de_validade)

        return closets_date

    def __company_with_more_products(data: list):
        company_with_products = {}
        for prd in data:
            if (
                prd.nome_da_empresa not in company_with_products
                and prd.nome_da_empresa != ""
            ):
                company_with_products[prd.nome_da_empresa] = 0
            company_with_products[prd.nome_da_empresa] += 1

        qtde = 0
        for cmp in company_with_products:
            if company_with_products[cmp] > qtde:
                qtde = company_with_products[cmp]
                company_with_more = cmp

        return company_with_more


if __name__ == "__main__":
    data_list = []
    for i in range(101):
        prd = ProductFactory()
        data_list.append(prd)

    print(SimpleReport.generate(data_list))
