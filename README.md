# Offensive bits and pieces 
My offensive security code library.  


## ip_int
IP to integer converter 

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