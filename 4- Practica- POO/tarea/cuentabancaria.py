from abc import ABC, abstractmethod


class CuentaBancaria(ABC):
    """Clase base abstracta para representar una cuenta bancaria."""

    def __init__(self, titular, tipocuenta, CBU, saldo_inicial=0):
        self.titular = titular
        self.tipocuenta = tipocuenta
        self._CBU = CBU
        self._saldo = saldo_inicial
        

    @property
    def CBU(self):
        return self._CBU

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser menor a cero.")
        self._saldo = valor

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a cero.")
        self.saldo += monto

    def __str__(self):
        return (
            f"[Tipo de Cuenta: {self.tipocuenta}] Titular: {self.titular} | "
            f"CBU: {self.CBU} | Saldo: ${self.saldo}"
        )

    @abstractmethod
    def extraer(self, monto):
        pass
    

'''

cuenta = CuentaBancaria ("Juan Perez", "Cuenta Corriente", "1234567890123456789012", 1000)

print(cuenta.titular)

cuenta.depositar(500)

print(cuenta.saldo)

print(cuenta)

'''