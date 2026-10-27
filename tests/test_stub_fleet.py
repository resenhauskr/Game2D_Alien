import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(_ROOT / "src"), str(_ROOT / "tests")]

from doubles import (  # noqa: E402
    StubAlien,
    StubEdgeAlien,
    StubSettings,
    StubShip,
)
from fleet_manager import FleetManager  # noqa: E402


def make_fleet(alien_class=StubAlien, settings=None):
    settings = settings or StubSettings()
    return FleetManager(None, settings, StubShip(), alien_class)


def test_create_fleet_cria_12_aliens_com_stub():
    fleet = make_fleet()
    fleet.create_fleet()
    # 4 aliens por linha x 3 linhas, com tela 1000x1000 e alien 100x100
    assert len(fleet.aliens) == 12


def test_create_fleet_posiciona_primeiro_e_ultimo_alien():
    fleet = make_fleet()
    fleet.create_fleet()
    posicoes = {(a.rect.x, a.rect.y) for a in fleet.aliens}
    assert (100, 100) in posicoes
    assert (700, 500) in posicoes


def test_change_fleet_direction_desce_a_frota_e_inverte_direcao():
    settings = StubSettings()
    fleet = make_fleet(settings=settings)
    fleet.create_fleet()
    y_antes = sorted(a.rect.y for a in fleet.aliens)

    fleet._change_fleet_direction()

    y_depois = sorted(a.rect.y for a in fleet.aliens)
    assert y_depois == [y + settings.fleet_drop_speed for y in y_antes]
    assert settings.fleet_direction == -1


def test_check_fleet_edges_muda_direcao_quando_alien_toca_a_borda():
    settings = StubSettings()
    fleet = make_fleet(StubEdgeAlien, settings)
    fleet.create_fleet()

    fleet._check_fleet_edges()

    assert settings.fleet_direction == -1
