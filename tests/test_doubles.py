import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(_ROOT / "src"), str(_ROOT / "tests")]

from desconto import IDesconto, Pedido  # noqa: E402
from doubles import StubSemDesconto  # noqa: E402


def test_pedido_com_stub():
    pedido = Pedido(StubSemDesconto())
    assert pedido.total(100) == 100


def test_pedido_com_mock_desconto(mocker):
    mock_desconto = mocker.Mock(spec=IDesconto)  # criar mock do desconto
    mock_desconto.calcular.return_value = 10  # definir comportamento do mock

    pedido = Pedido(mock_desconto)  # injetar mock no Pedido
    resultado = pedido.total(100)  # executar método

    assert resultado == 90  # verificar resultado final

    mock_desconto.calcular.assert_called()
    mock_desconto.calcular.assert_called_once_with(100)
    assert mock_desconto.calcular.call_count == 1
