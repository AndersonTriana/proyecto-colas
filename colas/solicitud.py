class Solicitud:
    def __init__(self, id, gravedad, hora_ingreso, descripcion):
        self.id = id
        self.gravedad = gravedad
        self.hora_ingreso = hora_ingreso
        self.descripcion = descripcion

    def __str__(self):
        return f"[{self.gravedad}] {self.id} - {self.descripcion} (Ingreso: {self.hora_ingreso})"