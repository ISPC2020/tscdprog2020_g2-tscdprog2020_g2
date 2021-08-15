from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class FormularioContagiados(FlaskForm):
    # Campos del formulario
    DNI = IntegerField('DNI', validators=[DataRequired()])
    Nombre = StringField('Nombre', validators=[DataRequired()])
    Apellido = StringField('Apellido', validators=[DataRequired()])
    Edad = IntegerField('Edad')
    Sexo = StringField('Genero')
    Obra_social = StringField('Obra social')
    Asistencia = StringField('Asistencia')
        # Datos de Contacto
    Telefono = IntegerField('Telefono', validators=[DataRequired()])
    Email = StringField('Email')
    Domicilio = StringField('Domicilio', validators=[DataRequired()])
    Barrio = StringField('Barrio', validators=[DataRequired()])
        # Datos Epidemeologicos
    Fecha_positivo = StringField('Fecha del positivo', validators=[DataRequired()])
    Variante = StringField('Tipo de variante', validators=[DataRequired()])
    Fecha_primerosSintomas = StringField('Fecha de los primeros sintomas')
    Sintomas = StringField('Sintomas')
    Comorbilidad = StringField('Comorbilidad')
    Fecha_alta = StringField('Fecha del alta')
    Fecha_muerte = StringField('Fecha del deceso')

    # Botones
    enviar = SubmitField('Enviar')
