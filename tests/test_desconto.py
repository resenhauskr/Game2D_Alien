import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(_ROOT / "src"), str(_ROOT / "tests")]

import pytest  # noqa: E402
from desconto import (  # noqa: E402
    DescontoNormal,
    DescontoPremium,
    DescontoVIP,
    ICupom,
    Pedido,
    aplicar_cupom,
    aplicar_desconto,
)


def test_desconto_normal_e_10_por_cento():
    assert DescontoNormal().calcular(100) == pytest.approx(10)


def test_desconto_vip_e_20_por_cento():
    assert DescontoVIP().calcular(100) == pytest.approx(20)


def test_desconto_premium_e_30_por_cento():
    assert DescontoPremium().calcular(100) == pytest.approx(30)


@pytest.mark.parametrize(
    "desconto, esperado",
    [(DescontoNormal(), 10), (DescontoVIP(), 20), (DescontoPremium(), 30)],
)
def test_lsp_qualquer_desconto_funciona_no_mesmo_lugar(desconto, esperado):
    assert aplicar_desconto(desconto, 100) == pytest.approx(esperado)


def test_pedido_com_desconto_normal():
    assert Pedido(DescontoNormal()).total(100) == pytest.approx(90)


def test_pedido_com_desconto_vip():
    assert Pedido(DescontoVIP()).total(100) == pytest.approx(80)


def test_isp_vip_aplica_cupom():
    assert aplicar_cupom(DescontoVIP(), "DESC10") is True


def test_isp_desconto_normal_nao_e_obrigado_a_ter_cupom():
    assert not isinstance(DescontoNormal(), ICupom)


def test_vip_valida_usuario():
    vip = DescontoVIP()
    assert vip.validar_usuario_vip("vip") is True
    assert vip.validar_usuario_vip("comum") is False
