from factory_errors.errors_class import CreatorErrors
from factory_errors.Ierrors_factory import IError
from factory_errors.split.Implement_split_error import ImplementSplitError


class CreatorSplitError(CreatorErrors):
    """
        Esta clase concreta se encarga de crear la fábrica de errores para la función split.
    """
    def factory_method(self) -> IError:
        """
            Método que crea la fábrica de errores.
        """
        return ImplementSplitError()
