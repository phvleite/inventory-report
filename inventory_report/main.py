from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory
# from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport
# from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.csv_importer import CsvImporter
# from inventory_report.importer.json_importer import JsonImporter
# from inventory_report.importer.xml_importer import XmlImporter
# from inventory_report.reports.colored_report import ColoredReport


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


def main():
    data_list = []
    for i in range(11):
        prd = product_test()
        data_list.append(prd)

    # print("SimpleReport:")
    # print(SimpleReport.generate(data_list))
    # print("\n\n")
    # print("CompleteReport:")
    # print(CompleteReport.generate(data_list))
    # print("\n\n")
    # print("Inventory")
    # print(
    #     Inventory.import_data(
    #         "inventory_report/data/inventory.xml",
    #         "simples",
    #     )
    # )
    print("CsvImporter:")
    data = CsvImporter.import_data("inventory_report/data/inventory.csv")
    for prd in data:
        print(prd)
    # print("JsonImporter:")
    # data = JsonImporter.import_data("inventory_report/data/inventory.json")
    # for prd in data:
    #     print(prd)
    # print("XmlImporter:")
    # data = XmlImporter.import_data("inventory_report/data/inventory.xml")
    # for prd in data:
    #     print(prd)
    # cp = ColoredReport(SimpleReport)
    # print(cp.generate(data_list))


if __name__ == "__main__":
    main()
