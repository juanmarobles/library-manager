from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca
biblioteca = Biblioteca()

def mostrar_menu():
    print("\n|------------------------------------|")
    print("| Bienvenido a Biblioteca Municipal  |")
    print("|------------------------------------|")
    print("| 1. Registrarse                     |")
    print("| 2. Logearse                        |")
    print("| 3. Préstamo de libros              |")
    print("| 4. Devoluciones                    |")
    print("| 5. Control de disponibilidad       |")
    print("| 6. Cálculo de multas por demora    |")
    print("| 7. Libros más solicitados          |")
    print("| 8. Cantidad de préstamos           |")
    print("| 0. Salir                           |")
    print("|------------------------------------|")


def main():
    opcion = -1  # inicializar en contador con cualquier numero distinto de 0

    while opcion != 0:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                print("Registrarse") #llamar a registrarse dentro de usuario.
                usuario = Usuario.registrarse()
                biblioteca.agregar_usuario(usuario)
            elif opcion == 2:
                print("Logearse") #llamar a logearse dentro de usuario.
                ##usuario = biblioteca.buscar_usuario(nombre, contrasenia)
            
            elif opcion == 3:
                print("Préstamo de libros")#llamar a prestamos dentro de biblioteca.

            elif opcion == 4:
                print("Devoluciones")

            elif opcion == 5:
                print("Control de disponibilidad")

            elif opcion == 6:
                print("Cálculo de multas")

            elif opcion == 7:
                print("Libros más solicitados")

            elif opcion == 8:
                print("Cantidad de préstamos realizados")

            elif opcion == 0:
                print("Gracias por usar la Biblioteca Municipal.")

            else:
                print("Opción inválida.")

        except ValueError:
            print("Debe ingresar un número válido.")


if __name__ == "__main__":
    main()