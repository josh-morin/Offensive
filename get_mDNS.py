from scapy.all import *


# callback function to process each packet
def packet_callback(packet):
    if packet.haslayer(UDP) and packet[UDP].dport == 5353:
        output = []

        if packet.haslayer(IP):
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
        else:
            src_ip = "N/A"
            dst_ip = "N/A"

        if packet.haslayer(Ether):
            src_mac = packet[Ether].src
            dst_mac = packet[Ether].dst
        else:
            src_mac = "N/A"
            dst_mac = "N/A"

        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

        output.append(f"Source IP: {src_ip}")
        output.append(f"Destination IP: {dst_ip}")
        output.append(f"Source Port: {src_port}")
        output.append(f"Destination Port: {dst_port}")
        output.append(f"Source MAC: {src_mac}")
        output.append(f"Destination MAC: {dst_mac}")

        if packet.haslayer(DNS):
            dns_layer = packet[DNS]
            if dns_layer.qr == 0:  # DNS query
                qname = dns_layer.qd.qname.decode()
                qtype = dns_layer.qd.qtype
                output.append(f"QNAME: {qname}")
                output.append(f"QTYPE: {qtype}")
            elif dns_layer.qr == 1:  # DNS response
                for i in range(dns_layer.ancount):
                    if hasattr(dns_layer.an[i], 'rdata'):
                        rdata = dns_layer.an[i].rdata
                        output.append(f"RDATA: {rdata}")

        output.append("\n" + "-" * 50 + "\n")

        # write output to file
        with open("output.txt", "a") as f:
            for line in output:
                f.write(line + "\n")


# sniffing on all available interfaces
sniff(filter="udp port 5353", prn=packet_callback, store=0)
