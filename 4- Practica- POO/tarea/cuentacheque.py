from . import cuentabancaria as cb


class CuentaCheque(cb.CuentaBancaria):
    """Cuenta bancaria que cobra un costo fijo por cada cheque/extracción."""

    def __init__(self, titular, CBU, saldo=0, costo_emision=50):
        super().__init__(titular, "Cuenta Cheque", CBU, saldo)
        self.costo_emision = costo_emision

    def extraer(self, monto):
        """Extrae el monto solicitado más el costo de emisión."""

        if monto <= 0:
            return False

        total = monto + self.costo_emision

        if total <= self.saldo:
            self.saldo -= total
            return True

        return False

'''
cheque = CuentaCheque("Empresa SRL", "285003", saldo_inicial=2000, costo_emision=100)

print(cheque)

print("Extracción:", cheque.extraer(500))

print(cheque)

'''