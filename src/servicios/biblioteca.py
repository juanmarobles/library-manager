from modelos.usuario import Usuario
from modelos.libro import Libro
from modelos.prestamo import Prestamo
from datetime import datetime, timedelta

DIAS_LIMITE = 7
TARIFA_POR_DIA = 10

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
                elif opcion == 2: ##devoluciones
                     self.devolver_libro(usuario) 
                elif opcion == 3: ##control de disponibilidad
                    self.mostrar_libros();
                elif opcion == 4: ##multas
                    self.calcular_multas(usuario) 
                elif opcion == 5: ##libros más solicitados
                    self.mostrar_libros_mas_solicitados()
                elif opcion == 6: ##cantidad de prestamos
                   cantidad = self.cantidad_prestamos_realizados()
                   print(f"Cantidad de préstamos realizados: {cantidad}")
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
            prestamo = Prestamo(usuario, libro)   
            ##prestamo.fecha_prestamo = datetime.now() - timedelta(days=10) ##descomentar para testear la multa, le puse 10 dias, cosa de q salga 3 dias de atraso 3x10=30
            self.prestamos.append(prestamo)
            print(f"Préstamo realizado: {libro.titulo}")
            print(f"Fecha de préstamo: {prestamo.fecha_prestamo.strftime('%d/%m/%Y')}")
            print(f"Devolver antes del: {(prestamo.fecha_prestamo + timedelta(days=DIAS_LIMITE)).strftime('%d/%m/%Y')}")
        else:
            print("El libro ya está prestado.")

    def devolver_libro(self, usuario):
        prestamos_usuario = [p for p in self.prestamos if p.usuario == usuario]

        if not prestamos_usuario:
            print("No tenés libros prestados.")
            return

        print("\n=== Tus libros prestados ===")
        for i, p in enumerate(prestamos_usuario):
            fecha_limite = p.fecha_prestamo + timedelta(days=DIAS_LIMITE)
            print(f"{i + 1}. {p.libro.titulo} - prestado el {p.fecha_prestamo.strftime('%d/%m/%Y')} (límite: {fecha_limite.strftime('%d/%m/%Y')})")

        try:
            opcion = int(input("Seleccione el libro a devolver (0 para cancelar): ")) - 1
        except ValueError:
            print("Opción inválida.")
            return

        if opcion == -1:
            return
        if opcion < 0 or opcion >= len(prestamos_usuario):
            print("Opción inválida.")
            return

        prestamo = prestamos_usuario[opcion]
        prestamo.libro.disponible = True
        self.prestamos.remove(prestamo)
        print(f"Libro '{prestamo.libro.titulo}' devuelto correctamente.")

        hoy = datetime.now()
        dias_atraso = (hoy - prestamo.fecha_prestamo - timedelta(days=DIAS_LIMITE)).days
        if dias_atraso > 0:
            multa = dias_atraso * TARIFA_POR_DIA
            print(f"Tenes {dias_atraso} día(s) de atraso. Multa: ${multa}")
        else:
            print("Devuelto en termino. Sin multa.")

    def calcular_multas(self, usuario):
        prestamos_usuario = [p for p in self.prestamos if p.usuario == usuario]

        if not prestamos_usuario:
            print("No tenes libros prestados.")
            return

        hoy = datetime.now()
        print("\n=== Cálculo de multas ===")
        hay_multas = False

        for p in prestamos_usuario:
            dias_atraso = (hoy - p.fecha_prestamo - timedelta(days=DIAS_LIMITE)).days
            if dias_atraso > 0:
                multa = dias_atraso * TARIFA_POR_DIA
                print(f"• {p.libro.titulo}: {dias_atraso} día(s) de atraso → ${multa}")
                hay_multas = True

        if not hay_multas:
            print("No tenes multas pendientes. Todos los libros están en termino.")



    
    
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

    def mostrar_libros_mas_solicitados(self):
        libros_ordenados = sorted(
            self.libros,
            key=lambda libro: libro.veces_prestado,
            reverse=True
        )

        if not libros_ordenados:
            print("No hay libros cargados.")
            return

        print("\n=== Libros más solicitados ===")
        for libro in libros_ordenados:
            print(f"{libro.titulo} - {libro.autor}: {libro.veces_prestado} préstamos")
                
    def cantidad_prestamos_realizados(self):
        return len(self.prestamos)


    



    def agregar_prestamo(self, prestamo):

        self.prestamos.append(prestamo)

    def cantidad_prestamos_realizados(self):

        return len(self.prestamos)

