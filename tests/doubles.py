"""Dublês de teste (stubs) usados nos testes do Game2D_Alien."""

import pygame


class StubSettings:
    """Stub das configurações: valores fixos e controlados."""

    def __init__(self) -> None:
        self.screen_width = 1000
        self.screen_height = 1000
        self.fleet_drop_speed = 10
        self.fleet_direction = 1


class StubShip:
    """Stub da nave: só tem o que os testes precisam."""

    def __init__(self) -> None:
        self.rect = pygame.Rect(0, 0, 100, 100)
        self.moving_right = False
        self.moving_left = False


class StubAlien(pygame.sprite.Sprite):
    """Stub de alienígena: não carrega imagem e nunca toca a borda."""

    def __init__(self, screen, settings) -> None:
        super().__init__()
        self.rect = pygame.Rect(0, 0, 100, 100)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self) -> bool:
        return False

    def update(self) -> None:
        pass


class StubEdgeAlien(StubAlien):
    """Stub de alienígena que sempre está na borda da tela."""

    def check_edges(self) -> bool:
        return True
