from colas.nodo_solicitud import NodoSolicitud

class ColaEmergencias:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamano = 0

    def esta_vacia(self):
        return self.inicio is None

    def encolar(self, solicitud):
        nodo_nuevo = NodoSolicitud(solicitud)
        if self.esta_vacia():
            self.inicio = self.final = nodo_nuevo
        else:
            actual = self.inicio
            anterior = None
            while actual and (actual.solicitud.gravedad < solicitud.gravedad or 
                            (actual.solicitud.gravedad == solicitud.gravedad and 
                            actual.solicitud.hora_ingreso <= solicitud.hora_ingreso)):
                anterior = actual
                actual = actual.siguiente

            if anterior is None:
                nodo_nuevo.siguiente = self.inicio
                self.inicio = nodo_nuevo
            else:
                anterior.siguiente = nodo_nuevo
                nodo_nuevo.siguiente = actual
                if actual is None:
                    self.final = nodo_nuevo
        self.tamano += 1

    def desencolar(self):
        if self.esta_vacia():
            return None
        solicitud = self.inicio.solicitud
        self.inicio = self.inicio.siguiente
        self.tamano -= 1
        if self.inicio is None:
            self.final = None
        return solicitud

    def ver_cola(self):
        actual = self.inicio
        while actual:
            print(actual.solicitud)
            actual = actual.siguiente