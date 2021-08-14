class Persona:
    """Esta clase tiene la responsabilidad de crear objetos del tipo Persona"""

    def __init__(self, id_persona, nombre, apellido, sexo, nacimineto):
        self._id = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._sexo = sexo
        self._nacimiento = nacimineto

    def __str__(self):
        return f'''
            Id: {self._id},
            Nombre: {self._nombre},
            Apellido: {self._apellido},
            Sexo: {self._sexo},
            Fecha de nacimineto: {self._nacimiento}'''

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id_persona):
        self._id = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    @property
    def nacimiento(self):
        return self._nacimiento

    @nacimiento.setter
    def nacimiento(self, nacimiento):
        self._nacimiento = nacimiento


# test
if __name__ == '__main__':
    persona1 = Persona(
        1,
        'Juan',
        'Perez',
        'M',
        '1995-03-01'
    )

    print(persona1.__str__())
