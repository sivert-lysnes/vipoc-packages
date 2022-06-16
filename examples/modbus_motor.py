from umodbus.server.tcp import RequestHandler, get_server

from socketserver import TCPServer

import vipoc.motor as motor

TCPServer.allow_reuse_address = True

# 0-8 retning (0 ned, 1 opp)
# 9-16 status (0 av, 1 på)

app = get_server(TCPServer, ("0.0.0.0", 502), RequestHandler)

@app.route(slave_ids=[1], function_codes=[1, 2, 3, 4], addresses=list(range(0, 8)))
def read_direction(slave_id, function_code, address):
    return motor.get_direction(address)

@app.route(slave_ids=[1], function_codes=[1, 2, 3, 4], addresses=list(range(8, 16)))
def read_status(slave_id, function_code, address):
    return motor.get_power(address - 8)

@app.route(slave_ids=[1], function_codes=[5, 6, 15, 16], addresses=list(range(0, 8)))
def write_direction(slave_id, function_code, address, value):
    motor.set_direction(address, value)

@app.route(slave_ids=[1], function_codes=[5, 6, 15, 16], addresses=list(range(8, 16)))
def write_direction(slave_id, function_code, address, value):
    motor.set_power(address - 8, value)

app.serve_forever()