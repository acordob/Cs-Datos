# Crea tres variables emn Python

precio_producto = 1200
cantidad = 3
descuento = 10

# Calcular el precio total sin descuento
total_sin_descuento = precio_producto * cantidad

# Calcular el monto de descuento
monto_descuento = total_sin_descuento * (descuento / 100)

# Calcular el precio total con descuento
total_con_descuento = total_sin_descuento - monto_descuento

# Imprime los resultados de cada cálculo con mensajes claros
print(f"Total sin descuento: ${total_sin_descuento}")
print(f"Monto de descuento: ${monto_descuento}")
print(f"Total con descuento: ${total_con_descuento}")