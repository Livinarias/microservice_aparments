"""Clase para controlar las peticiones HTTPS"""
import json
from http import server
from helpers.helper_data import call_data


class HttpRequestHandler(server.BaseHTTPRequestHandler):
    """
        Esta clase se encarga de manejar las peticiones HTTP que llegan al servidor. \n
        aqui se implementa el patron de diseño singleton
    """

    def do_GET(self):
        """Esta función se encarga de manejar las petición GET que llegan al microservicio."""
        if self.path.split('/')[1].split('?')[0] == 'inmuebles':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            items = call_data(self.path.split('?')[1])
            self.wfile.write(json.dumps(items).encode())
