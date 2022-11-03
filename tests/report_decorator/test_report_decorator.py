from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory
import re


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


def test_decorar_relatorio():
    data_list = []
    for i in range(11):
        prd = product_test()
        data_list.append(prd)

    cr = ColoredReport(SimpleReport)
    report = cr.generate(data_list)
    sr = SimpleReport.generate(data_list)

    index_start = sr.find("mais produtos:") + 15
    index_finish = sr.find("\n", index_start)
    if index_finish == -1:
        index_finish = len(sr)

    report_dates = re.findall(r"(\d+-\d+-\d+)", report)

    assert "\033[32mData de fabricação mais antiga:\033[0m" in report
    assert "\033[32mData de validade mais próxima:\033[0m" in report
    assert "\033[32mEmpresa com mais produtos:\033[0m" in report
    for date in report_dates:
        assert f"\033[36m{date}\033[0m" in report
    assert f"\033[31m{sr[index_start:index_finish]}\033[0m" in report
