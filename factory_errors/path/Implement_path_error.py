from factory_errors.Ierrors_factory import IError


class ImplementPathError(IError):
    """
        Esta clase concreta se encarga de implementar el error para el path.
    """
    def create_error(self) -> dict:
        """
            Método que crea el error.
        """
        return {
            "Code": 404,
            "Message": "No se encuentran datos, por favor corrija el path."
            }
