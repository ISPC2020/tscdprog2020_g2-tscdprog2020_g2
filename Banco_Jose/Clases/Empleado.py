# librerias
from Clases.Persona import Persona


class Empleado(Persona):
    """Esta clase se encarga de crear un objeto del tipo Empleado"""

    def __init__(self, id, nombre, apellido, sexo, nacimineto, contrato):
        super().__init__(id, nombre, apellido, sexo, nacimineto)
        self._contrato = contrato

    def __str__(self):
        return f'''
            {super().__str__()},
            Fecha de contratacion: {self._contrato}
        '''

    @property
    def contrato(self):
        return self._contrato

    @contrato.setter
    def contrato(self, contrato):
        self._contrato = contrato
