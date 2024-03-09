"""Modulo para levantar el puerto."""
import socketserver
from handlers.handler import HttpRequestHandler


if __name__ == '__main__':
    handler_object = HttpRequestHandler
    PORT = 8000
    my_server = socketserver.TCPServer(("localhost", PORT), handler_object)
    print("serving at port", PORT)
    my_server.serve_forever()
