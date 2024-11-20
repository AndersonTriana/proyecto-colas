from datetime import datetime
from colas.solicitud import Solicitud
from colas.cola_emergencias import ColaEmergencias

class SistemaEmergencias:
    def __init__(self):
        self.cola = ColaEmergencias()

    def registrar_solicitud(self, id, gravedad, descripcion):
        hora_ingreso = datetime.now()
        solicitud = Solicitud(id, gravedad, hora_ingreso, descripcion)
        self.cola.encolar(solicitud)
        print(f"Solicitud registrada: \n{solicitud}")

    def atender_solicitud(self):
        solicitud = self.cola.desencolar()
        if solicitud:
            print(f"Atendiendo solicitud: \n{solicitud}")
        else:
            print("No hay solicitudes en la cola.")

    def mostrar_estado_cola(self):
        print("\nEstado actual de la cola:")
        if self.cola.esta_vacia():
            print("La cola está vacía.")
        else:
            self.cola.ver_cola()

    def ejecutar(self):
        while True:
            print("\n--- Sistema de Emergencias ---")
            print("1. Registrar solicitud")
            print("2. Atender solicitud")
            print("3. Mostrar estado de la cola")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                id = input("ID del solicitante: ")
                try:
                    gravedad = int(input("Gravedad (1: Alta, 2: Media, 3: Baja): "))
                    if gravedad not in [1, 2, 3]:
                        raise ValueError
                except ValueError:
                    print("Error: La gravedad debe ser 1, 2 o 3.")
                    continue

                descripcion = input("Descripción: ")
                self.registrar_solicitud(id, gravedad, descripcion)

            elif opcion == "2":
                self.atender_solicitud()

            elif opcion == "3":
                self.mostrar_estado_cola()

            elif opcion == "4":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    sistema = SistemaEmergencias()
    sistema.ejecutar()