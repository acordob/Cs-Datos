"""
Sistema de Gestión para Librería "Libros & Bytes"
Desarrollado por: [Tu nombre]
Fecha: [Fecha]
"""

# 1. Lista de libros (diccionarios)
libros = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "precio": 25000, "stock": 5},
    {"titulo": "1984", "autor": "George Orwell", "precio": 18000, "stock": 3},
    {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "precio": 30000, "stock": 0},
    {"titulo": "Harry Potter y la piedra filosofal", "autor": "J.K. Rowling", "precio": 22000, "stock": 8},
    {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "precio": 15000, "stock": 2},
    {"titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "precio": 20000, "stock": 4}
]

# 6. Diccionario de descuentos por autor
descuentos_autores = {
    "Gabriel García Márquez": 10,  # 10% de descuento
    "J.K. Rowling": 5,             # 5% de descuento
    "George Orwell": 15            # 15% de descuento
}

# 2. Función para mostrar libros disponibles
def mostrar_libros_disponibles():
    print("\n=== LIBROS DISPONIBLES (stock > 0) ===")
    for libro in libros:
        if libro["stock"] > 0:
            print(f"{libro['titulo']} - {libro['autor']} - ${libro['precio']} - Stock: {libro['stock']}")
    print("=" * 50)

# 3. Función para filtrar por rango de precios
def filtrar_por_precio():
    try:
        min_precio = float(input("\nIngrese precio mínimo: "))
        max_precio = float(input("Ingrese precio máximo: "))
        
        print(f"\n=== LIBROS ENTRE ${min_precio} Y ${max_precio} ===")
        encontrados = False
        
        for libro in libros:
            if min_precio <= libro["precio"] <= max_precio and libro["stock"] > 0:
                print(f"{libro['titulo']} - ${libro['precio']} - Stock: {libro['stock']}")
                encontrados = True
        
        if not encontrados:
            print("No hay libros disponibles en ese rango de precios.")
            
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

# 4. Función para comprar libros
def comprar_libro(titulo, cantidad):
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if libro["stock"] >= cantidad:
                # Calcular precio base
                total = libro["precio"] * cantidad
                descuento = 0
                
                # 6. Aplicar descuento si corresponde
                if libro["autor"] in descuentos_autores:
                    porcentaje_descuento = descuentos_autores[libro["autor"]]
                    descuento = total * (porcentaje_descuento / 100)
                    total_con_descuento = total - descuento
                else:
                    total_con_descuento = total
                
                # Actualizar stock
                libro["stock"] -= cantidad
                
                return {
                    "exito": True,
                    "total": total_con_descuento,
                    "descuento": descuento,
                    "libro": libro["titulo"],
                    "autor": libro["autor"],
                    "cantidad": cantidad
                }
            else:
                return {
                    "exito": False,
                    "mensaje": f"Stock insuficiente. Solo hay {libro['stock']} unidades disponibles."
                }
    
    return {
        "exito": False,
        "mensaje": "Libro no encontrado en el inventario."
    }

# 7. Función para mostrar factura
def mostrar_factura(compras, total_general, total_descuentos):
    print("\n" + "=" * 60)
    print("                 FACTURA DE COMPRA")
    print("=" * 60)
    print("LIBRO\t\t\tCANT\tPRECIO\tTOTAL")
    print("-" * 60)
    
    for compra in compras:
        print(f"{compra['libro'][:20]}\t{compra['cantidad']}\t${compra['precio_unitario']}\t${compra['total']}")
    
    print("-" * 60)
    print(f"SUBTOTAL:\t\t\t\t${total_general + total_descuentos}")
    print(f"DESCUENTOS:\t\t\t\t-${total_descuentos}")
    print(f"TOTAL A PAGAR:\t\t\t\t${total_general}")
    print("=" * 60)
    print(f"¡Gracias por su compra en Libros & Bytes!")
    print("=" * 60)

# Función principal
def main():
    print("=== BIENVENIDO/A A LIBROS & BYTES ===")
    print("Sistema de gestión de inventario y compras")
    
    compras_realizadas = []
    total_general = 0
    total_descuentos = 0
    
    # 5. Bucle while para múltiples compras
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver libros disponibles")
        print("2. Filtrar por precio")
        print("3. Comprar libro")
        print("4. Ver descuentos disponibles")
        print("5. Finalizar compra y mostrar factura")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            mostrar_libros_disponibles()
            
        elif opcion == "2":
            filtrar_por_precio()
            
        elif opcion == "3":
            mostrar_libros_disponibles()
            titulo = input("\nIngrese el título del libro a comprar: ")
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                if cantidad <= 0:
                    print("Error: La cantidad debe ser mayor a 0.")
                    continue
                
                resultado = comprar_libro(titulo, cantidad)
                
                if resultado["exito"]:
                    print(f"\n✅ Compra exitosa!")
                    print(f"Libro: {resultado['libro']}")
                    print(f"Autor: {resultado['autor']}")
                    print(f"Cantidad: {resultado['cantidad']}")
                    print(f"Total: ${resultado['total']}")
                    
                    if resultado["descuento"] > 0:
                        print(f"Descuento aplicado: -${resultado['descuento']}")
                    
                    # Guardar compra para la factura
                    for libro in libros:
                        if libro["titulo"].lower() == titulo.lower():
                            compras_realizadas.append({
                                "libro": resultado["libro"],
                                "cantidad": resultado["cantidad"],
                                "precio_unitario": libro["precio"],
                                "total": resultado["total"],
                                "descuento": resultado["descuento"]
                            })
                    
                    total_general += resultado["total"]
                    total_descuentos += resultado["descuento"]
                    
                else:
                    print(f"\n❌ Error: {resultado['mensaje']}")
                    
            except ValueError:
                print("Error: Ingrese una cantidad válida.")
                
        elif opcion == "4":
            print("\n=== DESCUENTOS POR AUTOR ===")
            for autor, descuento in descuentos_autores.items():
                print(f"{autor}: {descuento}% de descuento")
                
        elif opcion == "5":
            if compras_realizadas:
                mostrar_factura(compras_realizadas, total_general, total_descuentos)
                break
            else:
                print("No hay compras realizadas.")
                
        elif opcion == "6":
            print("¡Gracias por visitar Libros & Bytes!")
            break
            
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    main()