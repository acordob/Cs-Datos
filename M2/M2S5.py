# Crea una lista productos que contenga al menos cinco nombres de productos (1 punto). 

productos = ["Notebook", "Mouse", "Audífonos", "Teclado", "Impresora"]

# Agrega dos productos más a la lista productos y luego rescata los primeros tres elementos en una nueva lista llamada productos_destacados (1 puntos).

productos.append("Joystick")
productos.append("Monitor")

productos_destacados = productos[:3]

# Crea un diccionario inventario donde cada clave sea el nombre de un producto y el valor sea la cantidad en stock. Incluye al menos cinco productos con sus cantidades (2 puntos). 
inventario = {
    "Notebook": 10,
    "Mouse": 30,
    "Audífonos": 100,
    "Teclado": 50,
    "Impresora": 5
}

# Agrega un nuevo producto al diccionario inventario y muestra la cantidad en stock de un producto específico (elige cualquiera de los cinco productos iniciales) (1 punto).
inventario["Joystick"] = 25
print("Stock de Teclados:", inventario["Teclado"])

# Crea una tupla categorías que contenga las categorías de los productos (por ejemplo, “Electrónica”, “Ropa”, “Alimentos”). Rescata y muestra la segunda categoría (1 punto).

categorias = ("Electrónica", "Ropa", "Alimentos")
print("La segunda categoría de la tupla es", categorias[1])

# Empaqueta las categorías en una tupla y luego desempaquétalas en variables individuales para que cada categoría quede asignada a una variable (2 puntos).
cat1, cat2, cat3 = categorias
print(f"Categoria 1: {cat1}")
print(f"Categoria 2: {cat2}")
print(f"Categoria 3: {cat3}")

# Crea un set productos_unicos a partir de la lista productos y verifica que no existan elementos duplicados (1 punto).
productos_unicos = set(productos)
print("Productos Únicos:", productos_unicos)

# Usa comprensión de listas para crear una lista productos_mayusculas que contenga los nombres de productos en mayúsculas (1 punto)
productos_mayusculas = [producto.upper() for producto in productos]
print("Productos en mayúsculas:", productos_mayusculas)