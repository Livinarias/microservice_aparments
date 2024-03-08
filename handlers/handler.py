"""Clase para controlar las peticiones HTTPS"""
import json
from http import server
from factory_errors.path.path_error import CreatorPathError
from helpers.helper_data import call_data, validate_path
from factory_errors.call_errors import call_errors


class HttpRequestHandler(server.BaseHTTPRequestHandler):
    """
        Esta clase se encarga de manejar las peticiones HTTP que llegan al servidor. \n
        aqui se implementa el patron de diseño singleton
    """

    def do_GET(self):
        """Esta función se encarga de manejar las petición GET que llegan al microservicio."""
        if validate_path(self.path):
            response = call_errors(CreatorPathError())
            self.send_response(response['Code'])
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response['Message']).encode())
        else:
            items = call_data(self.path.split('?')[1])
            self.send_response(items['Code'])
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(items['Message']).encode())
