# M2 S6
# Alumna: Alejandra Córdoba Sepúlveda

# Crea la clase Libro con los atributos privados _titulo, _autor y _isbn (1 punto).
# Define un constructor para Libro que inicialice estos atributos al momento de crear un objeto (1 punto). 
# Implementa métodos get_titulo(), get_autor() y get_isbn() para obtener el valor de cada atributo desde fuera de la clase (2 puntos). 
# Crea un método descripcion() en la clase Libro  que retorne una cadena con los detalles del libro en el formato “Título: [titulo], Autor: [autor], ISBN: [isbn]” (2 puntos).

class Libro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo # Atributo privado
        self._autor = autor # Atributo privado
        self._isbn = isbn # Atributo privado

    def get_titulo(self):
        return self._titulo
    
    def get_autor(self):
        return self._autor
    
    def get_isbn(self):
        return self._isbn
    
    def descripcion(self):
        return f"Titulo: {self._titulo}, Autor: {self._autor}, ISBN: {self._isbn}"
    

# Crea una clase Biblioteca que permita gestionar una lista de libros. Define un método agregar_libro() para añadir un libro a la biblioteca (1 punto).
# Define un método mostrar_libro() en Biblioteca que recorra la lista de libros e imprima la descripción de cada libro (2 puntos). 
class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def mostrar_libros(self):
        print("=== Libros en la biblioteca ===")
        for libro in self.libros:
            print(libro.descripcion())

# Instancia la clase Biblioteca, crea al menos dos libros y añádelos a la biblioteca. Luego, muestra los detalles de los libros almacenados (1 punto). 
if __name__ == "__main__":
    mi_biblioteca = Biblioteca()

libro1 = Libro("La hora 25", "Virgil Gheorghiu", "8493778907")
libro2 = Libro("El mando amarillo", "Lobsang Rampa", "9789588220642")

mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)

mi_biblioteca.mostrar_libros()