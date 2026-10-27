import sys

import pygame

from interfaces import Shooter


class GameEventHandler:
    """Responsável apenas por ler e tratar os eventos do teclado/janela."""

    def __init__(self, ship, shooter: Shooter) -> None:
        self.ship = ship
        # Princípio D: depende da abstração Shooter, não do BulletManager concreto
        self.shooter = shooter

    # Todos os métodos de eventos ficam aqui e são chamados no laço principal do jogo.
    def _check_events(self) -> None:
        """Responde a eventos de pressionamento de teclas e mouse (fechamento da janela)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)

    def _handle_keydown(self, event: pygame.event.Event) -> None:
        """Responde a eventos de pressionamento de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.shooter.fire_bullet()

    def _handle_keyup(self, event: pygame.event.Event) -> None:
        """Responde a eventos de soltura de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
