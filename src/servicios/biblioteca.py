from modelos.usuario import Usuario

class Biblioteca:

    def __init__(self):
        self.usuarios = []
        self.libros = []
        self.prestamos = []

    def buscar_usuario(self, nombre: str, contrasenia: str):

        for usuario in self.usuarios:

            if (usuario.nombre == nombre and
                    usuario.contrasenia == contrasenia):
                return usuario

        return None

    def agregar_usuario(self, usuario: Usuario):

        self.usuarios.append(usuario)

    def agregar_prestamo(self, prestamo):

        self.prestamos.append(prestamo)

    def cantidad_prestamos_realizados(self):

        return len(self.prestamos)

