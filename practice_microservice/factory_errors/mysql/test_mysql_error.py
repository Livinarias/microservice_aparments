from factory_errors.mysql.mysql_error import CreatorMysqlError
from factory_errors.mysql.Implement_mysql_error import ImplementMysqlError

def test_factory_method():
    creator = CreatorMysqlError()
    error_factory = creator.factory_method()

    assert isinstance(error_factory, ImplementMysqlError)

test_factory_method()