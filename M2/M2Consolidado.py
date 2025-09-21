# M2 Evaluacion Final
# Alumna: Alejandra Córdoba Sepúlveda

# Definir variables básicas y tipos de datos (1 punto): Crea una lista que contenga al menos cinco libros, donde cada libro sea un 
# diccionario con los atributos título (cadena de caracteres), autor (cadena de caracteres), precio (decimal) y cantidad en stock (entero)

libros = [
    {"titulo": "El Camino del Artista", "autor": "Julia Cameron", "precio": 16.760, "stock": 3},
    {"titulo": "La Vegetariana", "autor": "Han Kang", "precio": 15.150, "stock": 5},
    {"titulo": "Pizarnik: Poesia Completa", "autor": "Alejandra Pizarnik", "precio": 19.970, "stock": 7},
    {"titulo": "Harry poter y la Piedra Filosofal", "autor": "J. K. Rowling", "precio": 40.880, "stock": 15},
    {"titulo": "Murdle: Resuelve el Crimen", "autor": "G. T. Karber", "precio": 18.160, "stock": 2}
]

# Control de flujo (1 punto): Implementa una función llamada mostrar_libros_disponibles() que recorra la lista de libros y muestre en pantalla los libros que tienen más de una unidad en stock usando
# una sentencia for y una condición if.

def mostrar_libros_disponibles():
    print("\n Libros disponibles:")
    for libro in libros:
        if libro['stock'] > 1:
            print(f"{libro['titulo']} - ({libro['autor']}) - ${libro['precio']} - Stock: {libro['stock']}")


# Condiciones y operadores (1 punto):Solicita al usuario que ingrese un rango de precios (mínimo y máximo) y utiliza una sentencia if elif else para filtrar los libros en el rango ingresado y mostrarlos en pantalla

def filtro_precio(min_precio, max_precio):
    print(f"\n Libros entre ${min_precio} y ${max_precio}")
    encontrados = False
    for libro in libros:
        if min_precio <= libro['precio'] <= max_precio and libro['stock'] > 0:
            print(f"{libro['titulo']} - ${libro['precio']}")
            encontrados = True
        if not encontrados:
            print("No se encontraron libros en el rango de precios.")
        elif max_precio < min_precio:
            print("El rango ingresado no es válido.")
        else:
            print("Libro encontrado")


# Función personalizada para simular una compra (2 puntos):Crea una función comprar_libros(título, cantidad) que reciba como parámetros el título del libro y la cantidad a comprar. La función debe:
# ▪ Verificar si el libro está en el inventario y si la cantidad deseada está disponible.
# ▪ Si la compra es válida, restar la cantidad comprada al stock y mostrar el monto total de la compra.
# ▪ Si la cantidad solicitada es mayor al stock disponible, mostrar un mensaje de error

descuentos_autor = {
    "J. K. Rowling" : 0.15,
    "Han Kang" : 0.10
}

def comprar_libros(titulo, cantidad):
    for libro in libros:
        if libros['titulo'].lower() == titulo.lower():
            if libro['stock'] >= cantidad:
                precio_unitario = libro['precio']
                descuento = descuentos_autor.get(libro['autor'], 0)
                precio_total = precio_unitario * cantidad * (1 - descuento)
                ahorro = precio_unitario * cantidad * descuento
                libro['stock'] -= cantidad
                print(f"\n Compra exitosa: {cantidad} x {libro['titulo']}")
                print(f"Total pagado: ${precio_total: .2f}")
                print(f"Ahorro por descuento: ${ahorro: .2f}")
                return precio_total, ahorro
        else:
            print("No hay stock disponible.")
            return 0, 0
    print("Libro no encontrado.")
    return 0, 0