from . import cuentabancaria as cb


class CuentaAhorro(cb.CuentaBancaria):
    def __init__(self, titular, CBU, saldo=0, tasa_interes=0.001):
        super().__init__(titular, "Cuenta de Ahorro", CBU, saldo)
        self.tasa_interes = tasa_interes

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a cero.")
        if monto > self.saldo:
            raise ValueError("No hay suficiente saldo para realizar la extracción.")
        self.saldo -= monto

    def calcular_interes(self):
        return self.saldo * self.tasa_interes

    def aplicar_interes(self):
        self.saldo += self.calcular_interes()


'''
CuentadeAhorro = CuentaAhorro("María García", "0987654321098765432109", 5000, 0.001)
print(CuentadeAhorro)
CuentadeAhorro.aplicar_interes()
print(f"Saldo después de aplicar interés: ${CuentadeAhorro.saldo}")
CuentadeAhorro.extraer(1000)
print(f"Saldo después de extraer: ${CuentadeAhorro.saldo}")
'''
