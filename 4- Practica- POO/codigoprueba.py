from tarea import cuentaahorro as ca
from tarea import cuentacheque as ch
from tarea import cuentacorriente as cc

# --- CASOS DE PRUEBA ---
ahorro = ca.CuentaAhorro("Carlos Rossi", "285001", saldo=1000)
corriente = cc.CuentaCorriente("María López", "285002", saldo=500, limite_descubierto=1000)
cheque = ch.CuentaCheque("Empresa SRL", "285003", saldo=2000, costo_emision=100)

cuentas = [ahorro, corriente, cheque]

print("--- ESTADO INICIAL ---")
for c in cuentas:
    print(c)

print("\n--- PRUEBA POLIMÓRFICA DE EXTRACCIONES ($800) ---")
monto_extraccion = 800
for c in cuentas:
    monto_resultante = c.extraer(monto_extraccion)
    
    texto = str(c)

    if hasattr(c, "limite_descubierto"):
        texto += f" | Límite descubierto: ${c.limite_descubierto}"

    if hasattr(c, "costo_emision"):
        texto += f" | Costo de emisión: ${c.costo_emision}"

    print(texto)

print("\n--- PRUEBA DE INTERÉS EN CUENTA AHORRO ---")
ahorro.aplicar_interes()
print(f"Saldo después de aplicar interés: ${ahorro.saldo}")

print("\n--- PRUEBA DE LECTURA Y PROTECCIÓN (@property) ---")
print(f"Saldo consultado: ${ahorro.saldo}")
#ahorro.saldo = -500  # Descomentar para verificar que arroja ValueError
#ahorro.CBU = "999"   # Descomentar para verificar que arroja AttributeError (solo lectura)