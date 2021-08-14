# librerias
import Clases.Cursor as Cursor
import pandas as pd
from Clases.Empleado import Empleado
import Clases.Analisis as Analisis
from Clases.logger import log


class EmpleadoDAO:
    # consultas (CRUD)
    _INSERT = 'INSERT INTO employees(emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES ' \
              '(%s, %s, %s, %s, %s, %s)'
    _SELECT = 'SELECT emp_no, first_name, last_name, gender, birth_date, hire_date FROM employees WHERE emp_no=%s'
    _UPDATE = 'UPDATE employees SET birth_date=%s, first_name=%s, last_name=%s, gender=%s, hire_date=%s WHERE emp_no=%s'
    _DELETE = 'DELETE FROM employees WHERE emp_no=%s'
    _SALARIES = 'SELECT salary, from_date FROM salaries WHERE emp_no=%s'

    # metodos de clase
    @classmethod
    def insert(cls, empleado):
        with Cursor.Cursor() as cursor:
            valores = (
                empleado.id,
                empleado.nacimiento,
                empleado.nombre,
                empleado.apellido,
                empleado.sexo,
                empleado.contrato
            )

            cursor.execute(cls._INSERT, valores)
            log.info(f'Empleado insertado: {empleado}')
            return cursor.rowcount

    @classmethod
    def select(cls, id):
        with Cursor.Cursor() as cursor:
            cursor.execute(cls._SELECT, id)
            informacion_empleado = cursor.fetchall()

            log.info(f'Empleado seleccionado {informacion_empleado}')
            return informacion_empleado

    @classmethod
    def update(cls, empleado):
        with Cursor.Cursor() as cursor:
            valores = (
                empleado.nacimiento,
                empleado.nombre,
                empleado.apellido,
                empleado.sexo,
                empleado.contrato,
                empleado.id
            )

            cursor.execute(cls._UPDATE, valores)
            log.info(f'Empleado actualizado: {empleado}')
            return cursor.rowcount

    @classmethod
    def delete(cls, empleado):
        with Cursor.Cursor() as cursor:
            valores = (empleado.id,)

            cursor.execute(cls._DELETE, valores)
            log.info(f'Empleado Eliminado: {empleado}')
            return cursor.rowcount

    @classmethod
    def salaries(cls, id):
        with Cursor.Cursor() as cursor:
            cursor.execute(cls._SALARIES, id)
            informacion_salario = cursor.fetchall()

            log.info(f'Informacion salarial {informacion_salario}')
            return informacion_salario

    @staticmethod
    def menu_empleadoDAO():
        opcion = None

        while opcion != 6:
            print("""
                    Opciones:
                    1. Cargar empleado
                    2. Mostrar empleado
                    3. Editar empleado
                    4. Eliminar empleado
                    5. Analizar empleado
                    6. Salir
                    """)
            opcion = int(input("Ingrese una opcion: "))

            if opcion == 1:
                EmpleadoDAO.insert(Empleado(
                    int(input("Ingrese el numero de Id: ")),
                    input("Ingrese el Nombre: "),
                    input("Ingrese el Apellido: "),
                    input("Ingrese el Sexo <M o F>: "),
                    input("Ingrese la fecha de nacimineto <año-mes-dia>: "),
                    input("Ingrese la fecha de alta <año-mes-dia>: ")
                ))

            elif opcion == 2:
                df = pd.DataFrame(EmpleadoDAO.select(int(input("Ingrese el numero de Id: "))))
                df.columns = ['Id', 'Nombre', 'Apellido', 'Genero', 'Fecha de Nacimiento', 'Fecha de Alta']
                print(df)

            elif opcion == 3:
                EmpleadoDAO.update(Empleado(
                    int(input("Ingrese el numero de Id: ")),
                    input("Ingrese el Nombre: "),
                    input("Ingrese el Apellido: "),
                    input("Ingrese el Sexo <M o F>: "),
                    input("Ingrese la fecha de nacimineto <año-mes-dia>: "),
                    input("Ingrese la fecha de alta <año-mes-dia>: ")
                ))

            elif opcion == 4:
                EmpleadoDAO.delete(Empleado(
                    int(input("Ingrese el numero de Id: ")),
                    None,
                    None,
                    None,
                    None,
                    None
                ))

            elif opcion == 5:
                informacion_empleado = EmpleadoDAO.salaries(int(input("Ingrese el numero de Id: ")))
                Analisis.analisis(informacion_empleado)

            elif opcion == 6:
                break


# test
if __name__ == '__main__':
    pass
