"""empty message

Revision ID: 6120e9e00bda
Revises: 
Create Date: 2021-08-02 19:19:10.979543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6120e9e00bda'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('datos_contagiados',
    sa.Column('DNI', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('Nombre', sa.String(length=250), nullable=True),
    sa.Column('Apellido', sa.String(length=250), nullable=True),
    sa.Column('Edad', sa.Integer(), nullable=True),
    sa.Column('Sexo', sa.String(length=25), nullable=True),
    sa.Column('Obra_social', sa.String(length=250), nullable=True),
    sa.Column('Asistencia', sa.String(length=5), nullable=True),
    sa.Column('Telefono', sa.Integer(), nullable=True),
    sa.Column('Email', sa.String(length=250), nullable=True),
    sa.Column('Domicilio', sa.String(length=250), nullable=True),
    sa.Column('Barrio', sa.String(length=250), nullable=True),
    sa.Column('Fecha_positivo', sa.String(length=250), nullable=True),
    sa.Column('Variante', sa.String(length=250), nullable=True),
    sa.Column('Fecha_primerosSintomas', sa.String(length=250), nullable=True),
    sa.Column('Sintomas', sa.String(length=250), nullable=True),
    sa.Column('Comorbilidad', sa.String(length=250), nullable=True),
    sa.Column('Fecha_alta', sa.String(length=250), nullable=True),
    sa.Column('Muerte', sa.String(length=15), nullable=True),
    sa.Column('Fecha_muerte', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('DNI')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('datos_contagiados')
    # ### end Alembic commands ###