from umodbus.server.tcp import RequestHandler, get_server

from socketserver import TCPServer

TCPServer.allow_reuse_address = True

app = get_server(TCPServer, ("0.0.0.0", 502), RequestHandler)

@app.route(slave_ids=[1], function_codes=[1, 2, 3, 4], addresses=list(range(0, 64)))
def read_data(slave_id, function_code, address):
    print(f"Read: address {address}")
    return address + function_code * 8

@app.route(slave_ids=[1], function_codes=[5, 6, 15, 16], addresses=list(range(0, 64)))
def write_data(slave_id, function_code, address, value):
    print(f"write: address {address}, value {value}")

app.serve_forever()