# Inventario inicial: lista de libros como diccionarios
libros = [
    {"titulo": "1984", "autor": "George Orwell", "precio": 12.99, "stock": 5},
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "precio": 15.50, "stock": 3},
    {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "precio": 9.99, "stock": 0},
    {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "precio": 11.75, "stock": 4},
    {"titulo": "Orgullo y prejuicio", "autor": "Jane Austen", "precio": 10.25, "stock": 2}
]

# Descuentos por autor
descuentos_autor = {
    "George Orwell": 0.10,
    "Jane Austen": 0.15
}

# Función para mostrar libros disponibles
def mostrar_libros_disponibles():
    print("\n📚 Libros disponibles:")
    for libro in libros:
        if libro["stock"] > 0:
            print(f"- {libro['titulo']} ({libro['autor']}) - ${libro['precio']} - Stock: {libro['stock']}")

# Función para filtrar por rango de precios
def filtrar_por_precio(min_precio, max_precio):
    print(f"\n🔎 Libros entre ${min_precio} y ${max_precio}:")
    for libro in libros:
        if min_precio <= libro["precio"] <= max_precio:
            print(f"- {libro['titulo']} (${libro['precio']})")

# Función para comprar libros
def comprar_libros(titulo, cantidad):
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if libro["stock"] >= cantidad:
                precio_unitario = libro["precio"]
                descuento = descuentos_autor.get(libro["autor"], 0)
                precio_total = precio_unitario * cantidad * (1 - descuento)
                ahorro = precio_unitario * cantidad * descuento
                libro["stock"] -= cantidad
                print(f"\n✅ Compra exitosa: {cantidad} x {libro['titulo']}")
                print(f"Total pagado: ${precio_total:.2f}")
                print(f"Ahorro por descuento: ${ahorro:.2f}")
                return precio_total, ahorro
            else:
                print("❌ No hay suficiente stock disponible.")
                return 0, 0
    print("❌ Libro no encontrado.")
    return 0, 0

# Bucle principal
total_pagado = 0
total_ahorro = 0
total_libros = 0

while True:
    mostrar_libros_disponibles()
    opcion = input("\n¿Deseas comprar un libro? (sí/no): ").lower()
    if opcion == "no":
        break
    titulo = input("Ingrese el título del libro: ")
    try:
        cantidad = int(input("Cantidad a comprar: "))
        pagado, ahorro = comprar_libros(titulo, cantidad)
        total_pagado += pagado
        total_ahorro += ahorro
        total_libros += cantidad
    except ValueError:
        print("⚠️ Cantidad inválida.")

# Factura final
print("\n🧾 Factura final:")
print(f"Total de libros comprados: {total_libros}")
print(f"Total pagado: ${total_pagado:.2f}")
print(f"Ahorro total por descuentos: ${total_ahorro:.2f}")
