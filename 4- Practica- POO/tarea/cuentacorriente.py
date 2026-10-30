from . import cuentabancaria as cb


class CuentaCorriente(cb.CuentaBancaria):
    """Cuenta bancaria que permite disponer de un descubierto autorizado."""

    def __init__(self, titular, CBU, saldo=0, limite_descubierto=500):
        super().__init__(titular, "Cuenta Corriente", CBU, saldo)
        self.limite_descubierto = limite_descubierto

    def extraer(self, monto):
        """Extrae el monto si no excede el saldo más el descubierto autorizado."""
        if monto < 0:
            return False

        if monto <= self.saldo + self.limite_descubierto:
            self._saldo -= monto
            return True

        if monto > (self.saldo + self.limite_descubierto):
            return print("No hay suficiente saldo ni descubierto autorizado para realizar la extracción.")                     

        return False

'''
cuenta = CuentaCorriente("Juan Perez", "1234567890123456789012", 1000, 500)
print(cuenta)

cuenta.extraer(500)
print(cuenta)
cuenta.extraer(700)
print(cuenta)
cuenta.extraer(400)
print(cuenta)
'''