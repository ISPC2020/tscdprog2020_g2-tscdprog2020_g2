from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from database import db
from fomrs import FormularioContagiados
from models import Contagiados

# Objeto principal
app = Flask(__name__)

# Configuracion de la bd
USER_DB = 'jose'
PASS_DB = 'MyLinuxSQL'
URL_DB = 'localhost'
NAME_DB = 'ProyectoIntegrador'
FULL_URL_DB = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializacion del objeto db de sqlalchemy
db.init_app(app)
# Configuracion de flask-migrate
migrate = Migrate()
migrate.init_app(app, db)
# Configuracion de flask-wtf
app.config['SECRET_KEY'] = 'llave_secreta'


@app.route('/')
def index():
    # Listado de personas
    contagiados = Contagiados.query.all()
    total_contagiados = Contagiados.query.count()
    # Logger
    app.logger.debug(f'Listado de contagiados {contagiados}')
    app.logger.debug(f'Total de contagiados {total_contagiados}')

    return render_template('index.html', contagiados=contagiados, total_contagiados=total_contagiados)


@app.route('/ver/<int:DNI>')
def ver_detalle(DNI):
    # Recuperamos la persona segun el DNI proporcionado
    persona = Contagiados.query.get_or_404(DNI)
    app.logger.debug(f'Ver persona: {persona}')

    return render_template('detalle.html', persona=persona)


@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    persona = Contagiados()
    formularioPersona = FormularioContagiados(obj=persona)
    if request.method == 'POST':
        if formularioPersona.validate_on_submit():
            formularioPersona.populate_obj(persona)
            app.logger.debug(f'Persona a insertar: {persona}')
            # Insertamos el registro en la db
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('agregar.html', formulario=formularioPersona)


@app.route('/editar/<int:DNI>', methods=['GET', 'POST'])
def editar(DNI):
    # Recuperamos la persona a editar
    persona = Contagiados.query.get_or_404(DNI)
    formularioPersona = FormularioContagiados(obj=persona)
    if request.method == 'POST':
        if formularioPersona.validate_on_submit():
            formularioPersona.populate_obj(persona)
            app.logger.debug(f'Persona a editar: {persona}')
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('editar.html', formulario=formularioPersona)


@app.route('/eliminar/<int:DNI>')
def eliminar(DNI):
    persona = Contagiados.query.get_or_404(DNI)
    app.logger.debug(f'Persona a eliminar: {persona}')
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('index'))
