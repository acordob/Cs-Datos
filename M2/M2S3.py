# ACTIVIDAD PRACTICA MÓDULO 2 SESIÓN 3
# Alejandra Córdoba
# Fecha: 30/07/2025

# Te piden que desarrolles un programa en Python para evaluar las calificaciones y determinar si cada estudiante ha aprobado o necesita mejorar en alguna asignatura.

# 1. Solicita al usuario que ingrese el nombre y la calificación de un estudiante. Evalúa si la calificación es aprobatoria (nota mayor o igual a 60) usando una condición if else. Imprime si el estudiante ha aprobado o no (1 punto).

estudiantes = []


nombre = input("Ingresa el nombre del Estudiante")
calificacion = int(input("Ingresa Calificación"))

if calificacion >= 60:
      print(f"El estudiante: {nombre}, esta aprobado.")
else:
      print(f"El estudiante: {nombre}, esta desaprobado.")

# 2. Usa un bucle while para permitir la entrada de datos de varios estudiantes, hasta que el usuario decida salir (2 puntos).

while True:
    nombre = input("Ingresa tu Nombre")
    if nombre.lower() == 'exit':
        break
    #calificacion = int(input("Ingresa tu calificación"))

# 3. Dentro del bucle while, solicita las calificaciones de tres materias diferentes para cada estudiante (por ejemplo, Matemáticas, Ciencias e Inglés). Calcula el promedio de las tres notas (2 puntos).

    materias = ["Matemáticas", "Ciencias", "Inglés"]
    cal1 = int(input("Ingresa tu calificación en Matemáticas"))
    cal2 = int(input("Ingresa tu calificación en Ciencias"))
    cal3 = int(input("Ingresa tu calificación en Inglés"))
    promedio = (cal1 + cal2 + cal3) / 3
    print(f"El promedio de {nombre} es: {promedio}. Para salir escribe exit.") 

# 4. Usa una estructura if elif else para evaluar el promedio obtenido y asignar un comentario: “Excelente” si el promedio es 90 o más, “Bueno” si el promedio está entre 75 y 89, y “Necesita mejorar” si es menos de 75 (2 puntos).
    
    if promedio >= 90:
        comentario ="Excelente"
    elif promedio >= 75:
        comentario="Bueno"
    else:
        comentario="Necesita mejorar"

# 5. Implementa un bucle for para mostrar el nombre y los comentarios de todos los estudiantes ingresados (2 puntos).

    estudiantes.append(nombre)

    comentarios=[]
    for i in range(len(estudiantes)):
      print(f"Estudiante: {estudiantes[i]}, Comentario: {comentarios[i]}")





# 6. Usa una expresión ternaria para agregar una nota adicional en los comentarios si el estudiante tiene un promedio de 100 “¡Puntuación perfecta!” (1 punto).