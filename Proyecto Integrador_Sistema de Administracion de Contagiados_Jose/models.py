from app import db


class Contagiados(db.Model):
    DNI = db.Column(db.Integer, primary_key=True, autoincrement=False)
    Nombre = db.Column(db.String(250))
    Apellido = db.Column(db.String(250))
    Edad = db.Column(db.Integer)
    Sexo = db.Column(db.String(25))
    Obra_social = db.Column(db.String(250))
    Asistencia = db.Column(db.String(5))
    # Datos de Contacto
    Telefono = db.Column(db.Integer)
    Email = db.Column(db.String(250))
    Domicilio = db.Column(db.String(250))
    Barrio = db.Column(db.String(250))
    # Datos Epidemeologicos
    Fecha_positivo = db.Column(db.String(250))
    Variante = db.Column(db.String(250))
    Fecha_primerosSintomas = db.Column(db.String(250))
    Sintomas = db.Column(db.String(250))
    Comorbilidad = db.Column(db.String(250))
    Fecha_alta = db.Column(db.String(250))
    Fecha_muerte = db.Column(db.String(250))

    def __str__(self):
        return (
            f'DNI: {self.DNI}, '
            f'Nombre: {self.Nombre}, '
            f'Apellido: {self.Apellido}, '
            f'Sexo: {self.Sexo}, '
            f'Obra social: {self.Obra_social}, '
            f'Asistencia requerida: {self.Asistencia}, '
            f'Telefono: {self.Telefono}, '
            f'Email: {self.Email}, '
            f'Domicilio: {self.Domicilio}, '
            f'Barrio: {self.Barrio}, '
            f'Fecha del positivo: {self.Fecha_positivo}, '
            f'Tipo de la variante: {self.Variante}, '
            f'Fecha de los primeros sintomas: {self.Fecha_primerosSintomas}, '
            f'Sintomas: {self.Sintomas}, '
            f'Comorbilidad: {self.Comorbilidad}, '
            f'Fecha del alta: {self.Fecha_alta}, '
            f'Fecha de muerte: {self.Fecha_muerte}'
        )
