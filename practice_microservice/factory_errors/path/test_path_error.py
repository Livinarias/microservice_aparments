from factory_errors.split.split_error import CreatorSplitError
from factory_errors.split.Implement_split_error import ImplementSplitError

def test_factory_method():
    creator = CreatorSplitError()
    error_factory = creator.factory_method()

    assert isinstance(error_factory, ImplementSplitError)

test_factory_method()