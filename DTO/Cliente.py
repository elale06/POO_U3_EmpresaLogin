from DTO.SocioNegocio import SocioNegocio

class Cliente(SocioNegocio):
    def __init__(self, run, nombre, apellido, direccion, fono, correo,
                montoCredito=500, deuda=0, tipo=None):
        super().__init__(run, nombre, apellido, direccion, fono, correo)
        self.montoCredito = montoCredito
        self.deuda = deuda
        self.tipo = tipo

    def get_tipo_descripcion(self):
        if self.tipo == 1:
            return "1 - Cliente Normal"
        elif self.tipo == 2:
            return "2 - VIP"
        elif self.tipo == 3:
            return "3 - Empresa"
        else:
            return f"{self.tipo} - Desconocido"

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.get_tipo_descripcion()}"
