from abc import ABC, abstractmethod


class CreatorErrors(ABC):
    """
        Esta clase abstracta crear los metodos que llamaran las clases concretas
        para crear las fábricas de errores.
    """

    @abstractmethod
    def factory_method(self):
        """
            Método a sobreescribir por las fábricas concretas. 
        """
        pass

    def some_operation(self) -> dict:
        """
            Método para instanciar la interfaz y llamar el método que crea el error.
        """

        # Call the factory method to create a Product object.
        error = self.factory_method()

        # Now, use the product.
        result = error.create_error()

        return result