from currency_converter import CurrencyConverter

from spyne.application import Application
from spyne.decorator import srpc
from spyne.model import String, Integer, Float
from spyne.protocol.soap import Soap11
from spyne.service import ServiceBase
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class SOAPService(ServiceBase):
    def __init__(self):
        self.converter = CurrencyConverter()

    @srpc(String, String, Integer, _returns=Integer)
    def convert_currency(self, in_cur: str, out_cur: str, amt: int) -> int:
        return self.converter.convert(in_cur, out_cur, amt)

    @srpc(String, String, _returns=Float)
    def exchange_rate(self, in_cur: str, out_cur: str) -> float:
        return self.converter.exchange_rate(in_cur, out_cur)


if __name__ == '__main__':
    app = Application([SOAPService],
                      'currency.soap.service',
                      in_protocol=Soap11(validator='lxml'),
                      out_protocol=Soap11()
                      )

    wsgi_app = WsgiApplication(app)

    port = 8182
    server = make_server('127.0.0.1', port, wsgi_app)

    print("listening to http://127.0.0.1:" + str(port))
    print("wsdl is at: http://localhost:" + str(port) + "/?wsdl")
    # Start the server
    server.serve_forever()

    # ========== HOW TO CALL ==========
    # from zeep import Client
    # port = 8182
    # client = Client('http://localhost:' + str(port) + "/?wsdl")
    # client.service.convert_currency(in_cur='USD', out_cur='EUR', amt=100)
