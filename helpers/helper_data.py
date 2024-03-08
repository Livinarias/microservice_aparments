import re
from repository.mysql_repository import MysqlRepository
from repository.mysql_service import MysqlService
from factory_errors.mysql.mysql_error import CreatorMysqlError
from factory_errors.split.split_error import CreatorSplitError
from factory_errors.call_errors import call_errors
       
def call_data(path) ->list[dict] | dict:
    """
        Esta función llama el patron repository para establecer la conexión y traer los datos.\n
        El condicional llama un manejo de errores con el patron factory.
    """
    if any(rec in path for rec in ['1=1','$username', '$password', '= ?']):
        return call_errors(CreatorSplitError())
    service = MysqlRepository()
    items_service = MysqlService(service)
    convert_path = extract_and_remove_year_parameter(path)
    data = items_service.get_data(convert_path)
    if len(data) == 0:
        return call_errors(CreatorMysqlError())
    return [
        {
        "Dirección": item[0],
        "Ciudad": item[1],
        "Estado": item[2],
        "Precio de venta": item[3],
        "Descripción": item[4]
        }
        for item in data]

def extract_and_remove_year_parameter(text: str) -> str:
    """
        Esta función extrae el parámetro del año en el texto y lo elimina de la cadena.\n
        Además agrega comillas simples a los parametros de busqueda
    """
    match = re.search(r'year=[-\d]+', text)
    if len(match.group()) == 9:
        return process_path(re.sub(r'=([-\w]+)', r"='\1'",text))
    year_parameter = match.group().replace('=',' BETWEEN ').replace('-', ' AND ') if match else None
    text_without_year = re.sub(r'year=[-\d]+&?', '', text)
    format_text_without_year = re.sub(r'=([-\w]+)', r"='\1'", text_without_year)
    return process_path(format_text_without_year +' AND '+ year_parameter)


def process_path(path: str) -> str:
    """
        Esta función procesa el path para llamar la función call_data.
    """
    path_modify = ''.join(
        ('AND ', path.replace('&', ' AND ')
        .replace('year=', 'p.`year`=')
        .replace('estado=', 's.name='))
        )
    return path_modify