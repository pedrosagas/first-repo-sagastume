monto = float(input("Ingresa el monto de la cuenta: Q"))
porcentaje = float(input("¿Que porcentaje de propina quieres dejar? (ej. 10, 15, 20): "))
propina = monto * (porcentaje / 100)
total = monto + propina
print(f"Propina ({porcentaje}%): Q{propina:.2f}")
print(f"Total a pagar: Q{total:.2f}")