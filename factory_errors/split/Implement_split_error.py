from factory_errors.Ierrors_factory import IError


class ImplementSplitError(IError):
    """
        Esta clase concreta se encarga de implementar el error para la función split.
    """
    def create_error(self) -> str:
        """
            Método que crea el error.
        """
        return {"Message": "revise el path por favor, no se aceptan caracteres especiales."}
