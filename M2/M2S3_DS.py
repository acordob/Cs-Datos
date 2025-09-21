# Gestión de Calificaciones - Usando solo control de flujo
print("=== SISTEMA DE GESTIÓN DE CALIFICACIONES ===")
print("Instrucciones:")
print("- Ingrese el nombre del estudiante")
print("- Ingrese las 3 calificaciones (0-100)")
print("- Escriba 'salir' como nombre para terminar")
print("=" * 40)

# Lista para almacenar estudiantes
lista_estudiantes = []

# Bucle principal - while para múltiples estudiantes
continuar = True
while continuar:
    # Solicitar nombre del estudiante
    nombre = input("\nIngrese el nombre del estudiante: ")
    
    # Condición para salir del bucle
    if nombre.lower() == 'salir':
        continuar = False
        continue
    
    # Solicitar las tres calificaciones
    print(f"\nIngrese las calificaciones para {nombre}:")
    
    # Materias a evaluar
    materias = ["Matemáticas", "Ciencias", "Inglés"]
    calificaciones = []
    
    # Bucle for para las 3 materias
    for i in range(3):
        while True:
            try:
                nota = float(input(f"{materias[i]}: "))
                
                # Validar que la nota esté entre 0 y 100
                if nota < 0:
                    print("Error: La nota no puede ser negativa")
                elif nota > 100:
                    print("Error: La nota no puede ser mayor a 100")
                else:
                    calificaciones.append(nota)
                    break
                    
            except ValueError:
                print("Error: Ingrese un número válido")
    
    # Calcular el promedio
    suma_notas = 0
    for nota in calificaciones:
        suma_notas += nota
    promedio = suma_notas / 3
    
    # Determinar si aprobó (if-else)
    if promedio >= 60:
        resultado = "APROBADO"
    else:
        resultado = "NO APROBADO"
    
    # Asignar comentario según promedio (if-elif-else)
    if promedio >= 90:
        comentario = "Excelente"
    elif promedio >= 75:
        comentario = "Bueno"
    else:
        comentario = "Necesita mejorar"
    
    # Expresión ternaria para puntuación perfecta
    comentario_extra = " ¡Puntuación perfecta!" if promedio == 100 else ""
    comentario_final = comentario + comentario_extra
    
    # Guardar datos del estudiante
    estudiante = {
        "nombre": nombre,
        "calificaciones": calificaciones,
        "promedio": promedio,
        "resultado": resultado,
        "comentario": comentario_final
    }
    
    lista_estudiantes.append(estudiante)
    
    # Mostrar resultado inmediato
    print(f"\n--- RESULTADO PARA {nombre.upper()} ---")
    print(f"Calificaciones: {calificaciones}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {resultado}")
    print(f"Comentario: {comentario_final}")
    print("-" * 30)

# Mostrar resumen final de todos los estudiantes
if lista_estudiantes:
    print("\n" + "=" * 50)
    print("RESUMEN FINAL DE TODOS LOS ESTUDIANTES")
    print("=" * 50)
    
    # Bucle for para mostrar todos los estudiantes
    for estudiante in lista_estudiantes:
        print(f"\nEstudiante: {estudiante['nombre']}")
        print(f"Calificaciones: {estudiante['calificaciones']}")
        print(f"Promedio: {estudiante['promedio']:.2f}")
        print(f"Estado: {estudiante['resultado']}")
        print(f"Comentario: {estudiante['comentario']}")
        print("-" * 30)
    
    print(f"\nTotal de estudiantes procesados: {len(lista_estudiantes)}")
else:
    print("\nNo se ingresaron datos de estudiantes.")

print("\n¡Programa terminado!")