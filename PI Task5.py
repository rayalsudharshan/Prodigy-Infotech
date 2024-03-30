from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(TCP):
        print("Source IP: ", packet[IP].src)
        print("Destination IP: ", packet[IP].dst)
        print("Protocol: ", packet[TCP].proto)
        print("Payload: ", packet[TCP].payload)

sniff(filter="tcp", prn=packet_callback, store=0)