from modelos.usuario import Usuario
from modelos.libro import Libro
class Biblioteca:

    def mostrar_menu_usuario(self, nombre: str):
        print("\n|------------------------------------------|")
        print(f"| Bienvenido {nombre} a Biblioteca Municipal|")
        print("|--------------------------------------------|")                      
        print("| 1. Préstamo de libros                      |")
        print("| 2. Devoluciones                            |")
        print("| 3. Control de disponibilidad               |")
        print("| 4. Cálculo de multas por demora            |")
        print("| 5. Libros más solicitados                  |")
        print("| 6. Cantidad de préstamos                   |")
        print("| 0. Salir                                   |")
        print("|--------------------------------------------|")
    
   

    def __init__(self):
        self.usuarios = []
        self.libros = [
            Libro("Clean Code", "Robert Martin"),
            Libro("1984", "George Orwell"),
            Libro("El Principito", "Antoine de Saint-Exupéry"),
            Libro("Python Crash Course", "Eric Matthes")
        ]        
        self.prestamos = []

    def buscar_usuario(self):
        print("\n=== Login ===")
        nombre = input("Ingrese usuario: ")
        contrasenia = input("Ingrese contraseña: ")

        for usuario in self.usuarios:

            if (usuario.nombre == nombre and
                    usuario.contrasenia == contrasenia):
                return usuario
            
        return None 

    def agregar_usuario(self, usuario: Usuario):

        self.usuarios.append(usuario)    

    def validar_usuario(self, usuario: Usuario):
        if usuario is None:
            print("Credenciales incorrectas")
            return

        opcion = -1

        while opcion != 0:
            self.mostrar_menu_usuario(usuario.nombre)

            try:
                opcion = int(input("Seleccione una opción: "))
                self.validar_opcion(opcion, usuario)

            except ValueError:
                print("Debe ingresar un número válido.")

    def validar_opcion(self, opcion:int, usuario: Usuario):
            try:
                if opcion == 1: ##prestamo libros
                    self.prestar_libro(usuario);
                
                if opcion == 3: ##control de disponibilidad
                    self.mostrar_libros();
               
                elif opcion == 0:
                    print("Cerrado sesion...")

                else:
                    print("Opción inválida.")

            except ValueError:
                print("Debe ingresar un número válido.")

    def prestar_libro(self, usuario):
        self.mostrar_libros_disponibles()
        opcion = int(input("Seleccione un libro: ")) - 1
        if opcion < 0 or opcion >= len(self.libros):
            return
        libro = self.libros[opcion]
        if libro.disponible:
            libro.disponible = False
            libro.veces_prestado += 1
            self.prestamos.append((usuario, libro)) ##falta pasar fecha_prestado, ver libreria o alguna funcion

            print(f"Prestamo realizado: {libro.titulo}")
        else:
                print("El libro ya está prestado")

    
    
    def mostrar_libros(self):
        for i, libro in enumerate(self.libros):
            estado = "Disponible" if libro.disponible else "Prestado"

            print(
                f"{i + 1}. {libro.titulo} - "
                f"{libro.autor} ({estado})"
            )

    def mostrar_libros_disponibles(self):
        for i, libro in enumerate(self.libros):
            if libro.disponible:
                print(
                    f"{i + 1}. {libro.titulo} - "
                    f"{libro.autor} (Disponible)"
                )


    



