from factory_errors.path.path_error import CreatorPathError
from factory_errors.path.Implement_path_error import ImplementPathError

def test_factory_method():
    creator = CreatorPathError()
    error_factory = creator.factory_method()

    assert isinstance(error_factory, ImplementPathError)

test_factory_method()