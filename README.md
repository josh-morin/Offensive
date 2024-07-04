# Offensive bits and pieces 
My offensive security code library.  


## ip_int
IP to integer converter 

## get_mDNS
This script uses the Scapy library to capture Multicast DNS packets on port 5353, including the necessary packet fields for recon and spoofing/MITM. The script distinguishes between DNS queries and responses, printing relevant information for each. Saves the output to a file named output.txt.

Output example:
```
Source IP: 192.168.237.133
Destination IP: 192.168.237.134
Source Port: 5353
Destination Port: 5353
Source MAC: 40:XX:XX:XX:XX:XX
Destination MAC: 01:00:XX:XX:XX:XX
RDATA: [b'ModelName=Apple\xc2\xa0TV', b'AllowPairing=YES', b'BluetoothAddress=@XXXX', b'macAddress=40:XX:XX:XX:XX:XX', b'Name=Apple TV', b'UniqueIdentifier=XXXX', b'SystemBuildVersion=21L580', b'LocalAirPlayReceiverPairingIdentity=XXXX']
RDATA: b'Apple TV._mediaremotetv._tcp.local.'
RDATA: [b'model=J105aAP']
RDATA: [b'rpMac=1', b'rpHN=XXXX', b'rpFl=XXXX', b'rpMd=AppleTV6,2', b'rpVr=550.9.2', b'rpMRtID=XXXX', b'rpAD=XXXX', b'rpBA=73:D0:XX:XX:XX:XX']
RDATA: b'Apple TV._companion-link._tcp.local.'
RDATA: b'Apple TV._airplay._tcp.local.'
RDATA: [b'cn=0,1,2,3', b'da=true', b'et=0,3,5', b'ft=0x4A7FDFD5,0xBC175FDE', b'sf=0x244', b'md=0,1,2', b'am=AppleTV6,2', b'pk=XXXX', b'tp=UDP', b'vn=65537', b'vs=770.8.1', b'ov=17.5.1', b'vv=1']
```

## get_ssh
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
