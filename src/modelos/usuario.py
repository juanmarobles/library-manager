class Usuario:

    def __init__(self, nombre: str, contrasenia: str):
        self.nombre = nombre
        self.contrasenia = contrasenia
        ##self.libros_prestados =  libros_prestados

    @staticmethod
    def registrarse():
        print("\n=== Registro de usuario ===")

        nombre = input("Ingrese usuario: ")
        contrasenia = input("Ingrese contraseña: ")

        usuario = Usuario(nombre, contrasenia)
    
        print(f"Usuario {usuario.nombre} registrado correctamente en el sistema bibliotecario.")

        return usuario