from factory_errors.errors_class import CreatorErrors
from factory_errors.Ierrors_factory import IError
from factory_errors.path.Implement_path_error import ImplementPathError


class CreatorPathError(CreatorErrors):
    """
        Esta clase concreta se encarga de crear la fábrica de errores para el path.
    """
    def factory_method(self) -> IError:
        """
            Método que crea la fábrica de errores.
        """
        return ImplementPathError()
