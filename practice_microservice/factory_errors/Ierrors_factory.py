from abc import ABC, abstractmethod

class IError(ABC):
    """
        Esta Interfaz se encarga de definir el método que crear el error. 
    """

    @abstractmethod
    def create_error(self) -> dict:
        """
            Método a sobreescribir por las clases concretas. 
        """
        pass
