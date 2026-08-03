monto = float(input("Ingresa el monto de la cuenta: Q"))
propina = monto * 0.15
total = monto + propina
print(f"Propina (15%): Q{propina:.2f}")
print(f"Total a pagar: Q{total:.2f}")