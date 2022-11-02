from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory import Inventory


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

    print("SimpleReport:")
    print(SimpleReport.generate(data_list))
    print("\n\n")
    print("CompleteReport:")
    print(CompleteReport.generate(data_list))
    print("\n\n")
    print("Inventory")
    print(
        Inventory.import_data(
            "inventory_report/data/inventory.xml",
            "simples",
        )
    )


if __name__ == "__main__":
    main()
