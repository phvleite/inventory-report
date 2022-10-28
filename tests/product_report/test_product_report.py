from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory


def test_relatorio_produto():
    np = ProductFactory()
    prd = Product(
        np.id,
        np.nome_do_produto,
        np.nome_da_empresa,
        np.data_de_fabricacao,
        np.data_de_validade,
        np.numero_de_serie,
        np.instrucoes_de_armazenamento,
    )
    result = str(prd.__repr__)
    assert prd.nome_do_produto in result
    assert prd.nome_da_empresa in result
    assert prd.data_de_fabricacao in result
    assert prd.data_de_validade in result
    assert prd.instrucoes_de_armazenamento in result
