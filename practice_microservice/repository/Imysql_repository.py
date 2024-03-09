from abc import ABC, abstractmethod

class IRepository(ABC):
    """Interfaz para la conexión con la base de datos."""
    
    @abstractmethod
    def query(self, path: str):
        """Interfaz para la query de apartamenteos en la base de datos."""
        raise NotImplementedError

    @abstractmethod
    def close(self):
        """Interfaz para cerrar la conexión con la base de datos."""
        raise NotImplementedError
