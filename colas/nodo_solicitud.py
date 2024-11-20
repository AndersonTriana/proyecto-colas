from .solicitud import Solicitud

class NodoSolicitud:
    def __init__(self, solicitud: Solicitud):
        self.solicitud = solicitud
        self.siguiente = None