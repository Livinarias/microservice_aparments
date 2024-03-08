from factory_errors.Ierrors_factory import IError


class ImplementMysqlError(IError):
    """
        Esta clase concreta se encarga de implementar el error para la función mysql.
    """
    def create_error(self) -> dict:
        """
            Método que crea el error.
        """
        return {"message": "Datos no encontrados, por favor revise los filtros utilizados."}
