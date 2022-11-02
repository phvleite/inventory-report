from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data: list):
        oldest_date = cls._earliest_manufacturing(data)

        closets_date = cls._closest_expiration_date(data)

        company_with_more = cls._company_with_more_products(data)

        stocks = CompleteReport._products_stocked_by_company(data)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closets_date}\n"
            f"Empresa com mais produtos: {company_with_more}\n"
            "Produtos estocados por empresa:\n"
            f"{stocks}"
        )

    def _products_stocked_by_company(data: list):
        stocks = [product["nome_da_empresa"] for product in data]
        qtd_product = Counter(stocks)
        stocks_report = ""
        for prd in qtd_product:
            stocks_report += f"- {prd}: {qtd_product[prd]}\n"
        return stocks_report
