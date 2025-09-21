# Listas para almacenar la información
nombres_estudiantes = []      # Solo nombres
calificaciones_estudiantes = []  # Lista de listas con calificaciones
comentarios_estudiantes = []   # Comentarios de cada estudiante

print("=== SISTEMA DE CALIFICACIONES ===")

while True:
    # Solicitar nombre
    nombre = input("\nIngrese el nombre del estudiante (o 'salir' para terminar): ")
    
    if nombre.lower() == 'salir':
        break
    
    # Agregar nombre a la lista
    nombres_estudiantes.append(nombre)
    
    # Solicitar calificaciones
    calificaciones = []
    materias = ["Matemáticas", "Ciencias", "Inglés"]
    
    for materia in materias:
        nota = float(input(f"Nota de {materia} para {nombre}: "))
        calificaciones.append(nota)
    
    # Calcular promedio
    promedio = sum(calificaciones) / len(calificaciones)
    
    # Determinar comentario
    if promedio >= 90:
        comentario = "Excelente"
    elif promedio >= 75:
        comentario = "Bueno"
    else:
        comentario = "Necesita mejorar"
    
    # Agregar a las listas
    calificaciones_estudiantes.append(calificaciones)
    comentarios_estudiantes.append(comentario)
    
    print(f"{nombre} - Promedio: {promedio:.1f} - {comentario}")

# Mostrar todos los nombres ingresados
print("\n" + "="*50)
print("NOMBRES DE ESTUDIANTES INGRESADOS:")
print("="*50)

for i, nombre in enumerate(nombres_estudiantes, 1):
    print(f"{i}. {nombre}")

print(f"\nTotal: {len(nombres_estudiantes)} estudiantes")