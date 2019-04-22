import socket
import re
from ts.models import LogThermostat

pattern = r"([\d.]+)"


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
            print(data.decode())
            res = re.findall(pattern, data.decode())
            print(res[2])
            obj = LogThermostat(
                thermostat_state=bool(int(res[0])),
                current_state=res[1],
                temp=float(res[2]),
                set_temp=float(res[3]),
                co2=float(res[4]),
                set_co2=float(res[5]),
                light=bool(int(res[6])),
                light_R=int(res[7]),
                light_G=int(res[8]),
                light_B=int(res[9]),
            )
            obj.save()

    finally:

        sock.close()
