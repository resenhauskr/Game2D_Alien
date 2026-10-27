from abc import ABC, abstractmethod


class Shooter(ABC):
    """Contrato de quem sabe disparar projéteis."""

    @abstractmethod
    def fire_bullet(self) -> None:
        """Dispara um projétil."""


class BulletUpdater(ABC):
    """Contrato de quem sabe atualizar projéteis."""

    @abstractmethod
    def update_bullets(self, aliens) -> None:
        """Atualiza os projéteis."""


class FleetUpdater(ABC):
    """Contrato de quem sabe atualizar a frota de alienígenas."""

    @abstractmethod
    def update_aliens(self) -> None:
        """Atualiza a frota."""
