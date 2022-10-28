from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory


def test_cria_produto():
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
    assert produto.id == np.id
    assert produto.nome_do_produto == np.nome_do_produto
    assert produto.nome_da_empresa == np.nome_da_empresa
    assert produto.data_de_fabricacao == np.data_de_fabricacao
    assert produto.data_de_validade == np.data_de_validade
    assert produto.numero_de_serie == np.numero_de_serie
    assert (
        produto.instrucoes_de_armazenamento == np.instrucoes_de_armazenamento
    )
