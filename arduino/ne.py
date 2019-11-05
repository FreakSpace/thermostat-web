import socket
import re
from ts.models import Thermostat
from .settings import *

pattern = r"([\d.]+)"
SOCK_HOST = 'localhost'
SOCK_PORT = 10000

GET_DATA = "get_data"


class ThermostatBox:
    def __init__(self):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (SOCK_HOST, SOCK_PORT)

        self.sock.connect(server_address)

    def send_data_to_box(self, text):
        try:
            self.sock.sendall(text.encode())

        finally:
            self.sock.close()

    def get_data_from_box(self):
        try:

            # Send data
            message = GET_DATA.encode()

            self.sock.sendall(message)

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(1024)
                amount_received += len(data)
                print(data.decode())
                res = re.findall(pattern, data.decode())
                print(res[2])

                obj = Thermostat(
                    thermostat_state=bool(int(res[TS_STATE])),
                    current_state=res[CURRENT_STATE],
                    temp=float(res[CURRENT_TEMP]),
                    set_temp=float(res[SET_TEMP]),
                    co2=float(res[CO2_STATE]),
                    set_co2=float(res[CO2_SETTED]),
                    light=int(res[LIGHT_STATE]),
                    light_UV=int(res[UV]),
                    light_R=int(res[R]),
                    light_G=int(res[G]),
                    light_B=int(res[B]),
                )
                obj.save()

        finally:

            self.sock.close()

def f():
    o = ThermostatBox()
    o.get_data_from_box()
    del o
