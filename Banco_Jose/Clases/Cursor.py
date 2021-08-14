# librerias
from Clases.Conexion import Conexion
from Clases.logger import log


class Cursor:
    def __init__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        # log.info(f'With __enter__')

        self._connection = Conexion.obtener_conexion()
        self._cursor = self._connection.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # log.info(f'With __exit__')

        # En caso de exepciones
        if exc_val:
            self._connection.rollback()
            log.error(f'Transaccion fallida --> Rollback: {exc_val} {exc_type} {exc_tb}')
        else:
            self._connection.commit()
            log.debug(f'Successful transaction --> Commit')
        self._cursor.close()
