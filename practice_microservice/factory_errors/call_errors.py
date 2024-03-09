from factory_errors.errors_class import CreatorErrors


def call_errors(creator: CreatorErrors) -> dict:
    """
        Método para implementar las clases concretas de los errores.
    """
    return creator.some_operation()
