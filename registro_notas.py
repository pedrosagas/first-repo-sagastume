#Autor: Pedro Sagastume 
#5 Agosto 2026 


total=0
cantidad=0

while True:
    nota=float(input("Notas: "))

    if nota == -1:
        break

    elif 0 <= nota <= 100:
        total = total + nota 
        cantidad = cantidad + 1 

    else:
        print("Inválida")

print("Cantidad:", cantidad )
print("Promedio", total / cantidad)

    

