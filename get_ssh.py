import socket
import sys
from prettytable import PrettyTable


def get_ssh(host, port, timeout=5):
    try:
        # open socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        # connect to host
        sock.connect((host, port))

        # receive banner
        banner = sock.recv(1024).decode().strip()

        # close socket
        sock.close()

        return banner
    except Exception:
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 get_ssh.py <host1> <host2> ... <hostN>")
        sys.exit(1)

    hosts = sys.argv[1:]
    # iterate standard and non-standard ports
    ports = [22, 2200, 2222]

    # create table
    table = PrettyTable()
    table.field_names = ["Host", "Port", "Banner"]

    for host in hosts:
        for port in ports:
            banner = get_ssh(host, port)
            if banner:
                table.add_row([host, port, banner])

    print(table)
