from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(data: list):
        oldest_date = SimpleReport._earliest_manufacturing(data)

        closets_date = SimpleReport._closest_expiration_date(data)

        company_with_more = SimpleReport._company_with_more_products(data)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closets_date}\n"
            f"Empresa com mais produtos: {company_with_more}"
        )

    def _earliest_manufacturing(data: list):
        oldest_date = [
            prd["data_de_fabricacao"]
            for prd in data
            if prd["nome_da_empresa"] != ""
        ]
        oldest = sorted(oldest_date)
        return oldest[0]

    def _closest_expiration_date(data: list):
        today = datetime.now()
        nearests_days = [
            prd["data_de_validade"]
            for prd in data
            if datetime.fromisoformat(prd["data_de_validade"]) > today
        ]
        nearests_days_sorted = sorted(nearests_days)
        return nearests_days_sorted[0]

    def _company_with_more_products(data: list):
        cwm = [
            prd["nome_da_empresa"]
            for prd in data
            if prd["nome_da_empresa"] != ""
        ]
        cwm_most = Counter(cwm).most_common(1)
        company_with_more = cwm_most[0][0]
        return company_with_more
