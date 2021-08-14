# librerias
import pymysql as mysql
from Clases.logger import log


class Conexion:
    # Atributos de clase
    _DATABASE = 'employees'
    _USER_NAME = 'jose'
    _PASSWORD = 'MyLinuxSQL'
    _DB_PORT = 3306
    _HOST = 'localhost'
    _Connection = None
    _Cursor = None

    # Metodos de clase
    @classmethod
    def obtener_conexion(cls):
        # Validacion de conexion existente
        if cls._Connection is None:
            try:
                cls._Connection = mysql.connect(
                    user=cls._USER_NAME,
                    password=cls._PASSWORD,
                    host=cls._HOST,
                    database=cls._DATABASE,
                    port=cls._DB_PORT
                )
                log.info(f'Conexion exitosa: {cls._Connection}')
                return cls._Connection
            except Exception as e:
                log.error(f'Conexion fallida: {cls._Connection}')
                cls._Connection.close()
        else:
            return cls._Connection

    @classmethod
    def obtener_cursor(cls):
        # Validacion de cursor existente
        if cls._Cursor is None:
            try:
                cls._Cursor = cls.obtener_conexion().cursor()
                log.info(f'Conexion de cursor exitosa: {cls._Cursor}')
                return cls._Cursor
            except Exception as e:
                log.error(f'Conexion de cursor exitosa: {cls._Cursor}')
                cls._Cursor.close()
        else:
            return cls._Cursor


# test
if __name__ == '__main__':
    Conexion.obtener_conexion()
    Conexion.obtener_cursor()
