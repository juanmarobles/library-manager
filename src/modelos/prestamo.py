class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.devuelto = False