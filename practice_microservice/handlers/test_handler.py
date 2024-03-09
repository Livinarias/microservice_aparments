"""Módulo para testear el handler de las peticiones HTTP."""
import unittest
import json
from io import BytesIO
from handler import HttpRequestHandler

constant = [{
                "Dirección": "calle 23 #45-67",
                "Ciudad": "bogota",
                "Estado": "pre_venta",
                "Precio de venta": 120000000,
                "Descripción": "Hermoso apartamento en el centro de la ciudad"
            }]

class TestTestHandler(unittest.TestCase):
    def setUp(self):
        self.handler = HttpRequestHandler(MockRequest(), ('0.0.0.0', 8888), MockServer())

    def test_do_GET(self):
        expected_response = json.dumps(constant).encode()
        self.assertEqual(self.handler.do_GET(), expected_response)


class MockRequest:
    def makefile(self, *args, **kwargs):
        return BytesIO(b"GET /")

class MockServer:
    def __init__(self):
        pass

if __name__ == '__main__':
    unittest.main()
