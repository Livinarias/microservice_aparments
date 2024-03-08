from .constants import connect_db, query
import mysql.connector as connection
from .Imysql_repository import IRepository


class MysqlRepository(IRepository):
    """Clase para manejar la conexión con la base de datos MySQL."""

    def __init__(self):
        self.cnx = connection.connect(
            **connect_db
        )
        self.cursor = self.cnx.cursor()

    def query(self, path: str):
        """Esta función se encarga de hacer la consulta a la base de datos."""
        self.cursor.execute(query + path)
        return self.cursor.fetchall()

    def close(self):
        """Esta función se encarga de cerrar la conexión con la base de datos."""
        self.cursor.close()
        self.cnx.close()
