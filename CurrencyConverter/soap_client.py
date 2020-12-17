from zeep import Client

port = 8182
client = Client('http://localhost:' + str(port) + "/?wsdl")
print(client.service.convert_currency(in_cur='USD', out_cur='EUR', amt=100))
print(client.service.exchange_rate(in_cur='USD', out_cur='EUR'))
