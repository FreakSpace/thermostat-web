import socket
import re
from ts.models import LogThermostat

pattern = "temp=([0-9.]+); co2=([0-9.]+); hum=([0-9.]+); on=([01]); current_state=([0-9])"


def get_data_from_box():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)

    sock.connect(server_address)

    try:

        # Send data
        message = "1".encode()

        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(1024)
            amount_received += len(data)

            res = re.match(pattern, data.decode())
            obj = LogThermostat(
                temp=float(res.group(1)),
                co2=float(res.group(2)),
                on=bool(int(res.group(4))),
                current_state=res.group(5)
            )
            obj.save()

    finally:

        sock.close()
