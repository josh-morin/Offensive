## My offensive security code library.  


#### [ip_int](https://github.com/josh-morin/Offensive/blob/main/ip_int.py)
IP to integer converter


#### [get_mDNS](https://github.com/josh-morin/Offensive/blob/main/get_mDNS.py)
This script uses the Scapy library to capture Multicast DNS packets on port 5353, including the necessary packet fields for recon and spoofing/MITM. The script distinguishes between DNS queries and responses, printing relevant information for each. Saves the output to a file named output.txt.

Output example:
```
Source IP: 192.168.237.133
Destination IP: 192.168.237.134
Source Port: 5353
Destination Port: 5353
Source MAC: 40:00:xx:xx:xx:xx
Destination MAC: 01:00:xx:xx:xx:xx
RDATA: b'_mediaremotetv._tcp.local.'
RDATA: [b'model=J105aAP']
RDATA: b'_companion-link._tcp.local.'
RDATA: b'_airplay._tcp.local.'
RDATA: b'_raop._tcp.local.'
RDATA: b'_sleep-proxy._udp.local.'
```

#### [get_ssh](https://github.com/josh-morin/Offensive/blob/main/get_ssh.py)
The script iterates over the list of hosts and ports, attempting to grab an SSH banner. If a banner is found, it adds the host, port, and banner to a table printed at the end.


Usage:
```
python3 get_ssh.py <host1> <host2> ... <hostN>
```

Output example:
```
+-----------------+------+--------------------------------+
|       Host      | Port |             Banner             |
+-----------------+------+--------------------------------+
| 192.168.237.133 |  22  | SSH-2.0-OpenSSH_9.7p1 Debian-5 |
| 192.168.237.134 |  22  |      SSH-2.0-OpenSSH_8.0       |
+-----------------+------+--------------------------------+
```
