from factory_errors.errors_class import CreatorErrors
from factory_errors.Ierrors_factory import IError
from factory_errors.mysql.Implement_mysql_error import ImplementMysqlError


class CreatorMysqlError(CreatorErrors):
    """
        Esta clase concreta se encarga de crear la fábrica de errores para la función mysql.
    """
    def factory_method(self) -> IError:
        """
            Método que crea la fábrica de errores.
        """
        return ImplementMysqlError()
