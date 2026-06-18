from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca
biblioteca = Biblioteca()

def mostrar_menu_principal():
    print("\n|------------------------------------|")
    print("| Bienvenido a Biblioteca Municipal  |")
    print("|------------------------------------|")
    print("| 1. Registrarse                     |")
    print("| 2. Logearse                        |")
    print("| 0. Salir                           |")
    print("|------------------------------------|")




def main():
    opcion = -1  

    while opcion != 0:
        mostrar_menu_principal()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                usuario = Usuario.registrarse()
                biblioteca.agregar_usuario(usuario)
            elif opcion == 2:
                usuario = biblioteca.buscar_usuario()
                biblioteca.validar_usuario(usuario) 
                
            elif opcion == 0:
                print("Gracias por usar la Biblioteca Municipal.")

            else:
                print("Opción inválida.")

        except ValueError:
            print("Debe ingresar un número válido.")


if __name__ == "__main__":
    main()