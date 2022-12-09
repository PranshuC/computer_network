import socket
from colorama import init, Fore
import argparse

# Port open = socket can connect


def is_port_open(host: str, port: int) -> bool:
    """
      Try to connect to a server socket.
      If can connect, port is open.
    """
    # Step 1 - Create a socket
    # Address family - Networking layer : IPv4/IPv6 
    # Transport Layer - TCP/UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Step 2 - Check if socket can connect or not
    try:
        client_socket.connect((host, port))
        return True
    except:
        return False


if __name__ == '__main__':
    init()

    # Declare arguments
    parser = argparse.ArgumentParser(description='Port Scanner')
    parser.add_argument('-H', '--host', help='Host to scan',
                        required=True, type=str)
    parser.add_argument(
        '-s', '--start', help='Starting port', default=1, type=int)
    parser.add_argument('-e', '--end', help='Ending port',
                        default=1024, type=int)

    # Parse arguments
    args = parser.parse_args()
    host, start, end = args.host, args.start, args.end

    for port in range(start, end):
        is_open = is_port_open(host, port)
        if not is_open:
            print(f"{Fore.RED}Port {port} is closed{Fore.RESET}")
        else:
            print(f"{Fore.GREEN}Port {port} is open{Fore.RESET}")

# python port-scanner.py --host 127.0.0.1 --start 6000 --end 7000