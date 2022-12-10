import argparse
import socket

def connect_to_server(server_host: str, server_port: int) -> None:
  # Step 1 - Create a socket
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Step 2 - Connect to the server
  client_socket.connect((server_host, server_port))

  print(f"Connected from {client_socket.getsockname()} to {client_socket.getpeername()}")

  # Step 3 - Send data
  # TCP Segments
  client_socket.sendall(b"Hello World")

  # Setp 4 - Receive data
  data =  client_socket.recv(1024)
  print(f"Received {data}")

  # Setp 5 - Close socket
  client_socket.close()



if __name__ == '__main__':
  # Declare arguments
  parser = argparse.ArgumentParser(description='Socket Client')
  parser.add_argument('-H', '--host', help='Target Host', default='127.0.0.1', type=str)
  parser.add_argument('-p', '--port', help='Target Port', required=True, type=int)

  # Parse arguments
  args = parser.parse_args()
  host, port = args.host, args.port

  connect_to_server(host, port)

# python client.py --port 6000