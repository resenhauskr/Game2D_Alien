import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(_ROOT / "src"), str(_ROOT / "tests")]

import pygame  # noqa: E402
import pytest  # noqa: E402
from doubles import StubAlien, StubSettings, StubShip  # noqa: E402
from fleet_manager import FleetManager  # noqa: E402
from game_events import GameEventHandler  # noqa: E402
from interfaces import Shooter  # noqa: E402


def test_espaco_dispara_um_projetil(mocker):
    shooter = mocker.Mock(spec=Shooter)  # mock respeitando o contrato Shooter
    handler = GameEventHandler(StubShip(), shooter)
    evento = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)

    handler._handle_keydown(evento)

    shooter.fire_bullet.assert_called_once()


def test_seta_direita_move_nave_sem_disparar(mocker):
    shooter = mocker.Mock(spec=Shooter)
    ship = StubShip()
    handler = GameEventHandler(ship, shooter)
    evento = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)

    handler._handle_keydown(evento)

    assert ship.moving_right is True
    shooter.fire_bullet.assert_not_called()


def test_update_aliens_chama_borda_e_colisao_uma_vez(mocker):
    fleet = FleetManager(None, StubSettings(), StubShip(), StubAlien)
    check_edges = mocker.patch.object(fleet, "_check_fleet_edges")
    check_collision = mocker.patch.object(fleet, "_check_ship_collision")

    fleet.update_aliens()

    check_edges.assert_called_once()
    check_collision.assert_called_once()


def test_colisao_com_a_nave_encerra_o_jogo(mocker):
    fleet = FleetManager(None, StubSettings(), StubShip(), StubAlien)
    mocker.patch(
        "fleet_manager.pygame.sprite.spritecollideany", return_value=object()
    )

    with pytest.raises(SystemExit):
        fleet._check_ship_collision()
