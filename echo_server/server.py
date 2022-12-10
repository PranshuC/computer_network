# Client <===> Server
# Client -> "Hello World" -> Server
# Server -> "HELLO WORLD" -> Client
import argparse
import socket

def run_server(server_host: str, server_port: int) -> None:

  # Step 1 - Create a socket
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Step 2 - Bind to a host and port
  server_socket.bind((server_host, server_port))

  # Step 3 - Start listening on port
  server_socket.listen()
  print(f"Listening on {server_port}")

  # Step 4 - Accept connections
  # Blocking call
  connection, addr = server_socket.accept()
  # Blocked until some client connects
  # Ephemeral client port
  print(f"Connected from {connection.getsockname()} to {connection.getpeername()}")

  # Step 5 - Receive data
  data = connection.recv(1024)
  print(f"Received {data}")

  # Step 6 - Send data
  connection.sendall(data.upper())

  # Step 7 - Close connection
  server_socket.close()
  connection.close()


if __name__ == '__main__':

  # Declare arguments
  parser = argparse.ArgumentParser(description='Socket Server')
  parser.add_argument('-H', '--host', help='Host to bind to', default='127.0.0.1', type=str)
  parser.add_argument('-p', '--port', help='Port to bind to', required=True, type=int)

  # Parse arguments
  args = parser.parse_args()
  host, port = args.host, args.port

  run_server(host, port)

# python server.py --port 6000