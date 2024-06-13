import socket
import struct


def ip_to_int(ip_addr):
    # convert the ip address to a 32-bit format
    load_ip = socket.inet_aton(ip_addr)
    # unload the binary format to a 32-bit integer
    return struct.unpack("!I", load_ip)[0]


# get the ip address from user input
ip_address = input("Enter an IP address: ")
try:
    ip_as_int = ip_to_int(ip_address)
    print(f"The integer representation of {ip_address} is {ip_as_int}")
except socket.error:
    print("Invalid IP address")
