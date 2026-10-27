"""Exemplo de desconto usado nas aulas de SOLID e de dublês de teste."""


class IDesconto:
    """Contrato de quem calcula um desconto (princípios I e D)."""

    def calcular(self, valor):
        raise NotImplementedError


class ICupom:
    """Contrato de quem aplica cupom."""

    def aplicar_cupom(self, codigo):
        raise NotImplementedError


class IVIP:
    """Contrato de quem valida usuário VIP."""

    def validar_usuario_vip(self, usuario):
        raise NotImplementedError


class DescontoNormal(IDesconto):
    """Desconto para cliente normal."""

    def calcular(self, valor):
        return valor * 0.1


class DescontoVIP(IDesconto, ICupom, IVIP):
    """Desconto para cliente VIP (também aceita cupom)."""

    def calcular(self, valor):
        return valor * 0.2

    def aplicar_cupom(self, codigo):
        return True

    def validar_usuario_vip(self, usuario):
        return usuario == "vip"


class DescontoPremium(IDesconto):
    """Desconto para cliente Premium."""

    def calcular(self, valor):
        return valor * 0.3


class Pedido:
    """Calcula o total do pedido sem saber qual desconto está sendo usado."""

    def __init__(self, desconto: IDesconto):
        self.desconto = desconto

    def total(self, valor):
        return valor - self.desconto.calcular(valor)


def aplicar_desconto(desconto: IDesconto, valor: float) -> float:
    """Funciona com qualquer desconto (princípio L)."""
    return desconto.calcular(valor)


def aplicar_cupom(cupom: ICupom, codigo: str) -> bool:
    """Só aceita quem sabe aplicar cupom (princípio I)."""
    return cupom.aplicar_cupom(codigo)


def main():
    valor = 100

    normal = DescontoNormal()
    vip = DescontoVIP()
    premium = DescontoPremium()

    print("Desconto normal:", aplicar_desconto(normal, valor))
    print("Desconto VIP:", aplicar_desconto(vip, valor))
    print("Desconto Premium:", aplicar_desconto(premium, valor))
    print("Cupom VIP:", aplicar_cupom(vip, "DESC10"))

    pedido_normal = Pedido(normal)
    pedido_vip = Pedido(vip)
    print("Total normal:", pedido_normal.total(valor))
    print("Total VIP:", pedido_vip.total(valor))


if __name__ == "__main__":  # pragma: no cover
    main()
