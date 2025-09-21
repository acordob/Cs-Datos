# Inventario inicial
libros = [
    {"titulo": "Data Science con Python", "autor": "Joel Grus", "precio": 25500, "stock": 5},
    {"titulo": "El Camino del Artista", "autor": "Julia Cameron", "precio": 16760, "stock": 3},
    {"titulo": "La Vegetariana", "autor": "Han Kang", "precio": 15150, "stock": 5},
    {"titulo": "Poesía Completa", "autor": "Alejandra Pizarnik", "precio": 19970, "stock": 7},
    {"titulo": "Harry Potter y la Piedra Filosofal", "autor": "J. K. Rowling", "precio": 40880, "stock": 15}
]

# Descuentos por autor
descuentos_autor = {
    "Joel Grus": 0.15,
    "Julia Cameron": 0.10,
    "Alejandra Pizarnik": 0.05
}

# Función 1: Mostrar libros disponibles
def mostrar_libros_disponibles():
    print("\n --- Libros disponibles --- ")
    for libro in libros:
        if libro["stock"] > 1:
            print(f"- {libro['titulo']} ({libro['autor']}) - ${libro['precio']} CLP - Stock: {libro['stock']}")

# Función 2: Filtrar por rango de precios
def filtrar_por_precio(min_precio, max_precio):
    print(f"\n Libros entre ${min_precio} y ${max_precio} CLP:")
    encontrados = False
    for libro in libros:
        if min_precio <= libro["precio"] <= max_precio:
            print(f"- {libro['titulo']} (${libro['precio']} CLP)")
            encontrados = True
    if not encontrados:
        print("No se encontraron libros en ese rango de precio.")
    elif max_precio < min_precio:
        print("El rango ingresado no es válido.")
    else:
        print("Búsqueda completada.")

# Función 3: Comprar libros
def comprar_libros(titulo, cantidad):
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if libro["stock"] >= cantidad:
                descuento = descuentos_autor.get(libro["autor"], 0)
                precio_unitario = libro["precio"]
                precio_total = precio_unitario * cantidad * (1 - descuento)
                ahorro = precio_unitario * cantidad * descuento
                libro["stock"] -= cantidad
                print(f"\n Compra exitosa: {cantidad} x {libro['titulo']} - Total: ${int(precio_total)} CLP")
                if descuento > 0:
                    print(f"Se aplicó un descuento de {int(descuento * 100)}%")
                return cantidad, precio_total, ahorro
            else:
                print("Stock insuficiente.")
                return 0, 0, 0
    print("Libro no encontrado.")
    return 0, 0, 0

# Bucle principal
total_libros = 0
total_pagado = 0
total_ahorro = 0

while True:
    print("\n --- SISTEMA DE COMPRAS --- ")
    print("1. Mostrar libros disponibles")
    print("2. Filtrar libros por rango de precios")
    print("3. Comprar libro")
    print("4. Finalizar compra y mostrar factura")
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        mostrar_libros_disponibles()
    elif opcion == "2":
        try:
            min_precio = int(input("Ingrese precio mínimo: "))
            max_precio = int(input("Ingrese precio máximo: "))
            filtrar_por_precio(min_precio, max_precio)
        except ValueError:
            print("Entrada inválida. Use números enteros.")
    elif opcion == "3":
        titulo = input("Ingrese el título del libro: ")
        try:
            cantidad = int(input("Cantidad a comprar: "))
            comprados, pagado, ahorro = comprar_libros(titulo, cantidad)
            total_libros += comprados
            total_pagado += pagado
            total_ahorro += ahorro
        except ValueError:
            print("Cantidad inválida.")
    elif opcion == "4":
        print("\n --- FACTURA FINAL --- ")
        print(f"Total de libros comprados: {total_libros}")
        print(f"Total pagado: ${int(total_pagado)} CLP")
        print(f"Ahorro por descuentos: ${int(total_ahorro)} CLP")
        print("Gracias por su compra en Libros & Bytes")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
