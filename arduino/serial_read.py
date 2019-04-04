import socket
import sys

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
            print(f'::: {data.decode()}')

    finally:

        sock.close()

