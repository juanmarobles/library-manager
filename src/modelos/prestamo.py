from datetime import datetime

class Prestamo:

    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        self.devuelto = False