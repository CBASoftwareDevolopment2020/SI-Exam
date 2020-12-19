from currency_converter import CurrencyConverter

from spyne.application import Application
from spyne.decorator import srpc
from spyne.model import String, Integer, Float
from spyne.protocol.soap import Soap11
from spyne.service import ServiceBase
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class SOAPService(ServiceBase):
    converter = CurrencyConverter()

    @srpc(String, String, Integer, _returns=Integer)
    def convert_currency(in_cur: str, out_cur: str, amt: int) -> int:
        return SOAPService.converter.convert(in_cur, out_cur, amt)

    @srpc(String, String, Integer, _returns=Integer)
    def convert_currency_old(in_cur: str, out_cur: str, amt: int) -> int:
        return SOAPService.converter.convert_old(in_cur, out_cur, amt)

    @srpc(String, String, _returns=Float)
    def exchange_rate(in_cur: str, out_cur: str) -> float:
        return SOAPService.converter.exchange_rate(in_cur, out_cur)


if __name__ == '__main__':
    app = Application([SOAPService],
                      'spyne.examples.hello.http',
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
