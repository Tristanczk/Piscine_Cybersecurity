import argparse
import sys
import ipaddress
import re


# for regex:
# https://stackoverflow.com/questions/7629643/how-do-i-validate-the-format-of-a-mac-address
def verify_address(args, parser):
    try:
        ipaddress.IPv4Address(args.IP_src)
    except Exception:
        print("Error: wrong format for IP_src", file=sys.stderr)
        parser.exit()
    try:
        ipaddress.IPv4Address(args.IP_target)
    except Exception:
        print("Error: wrong format for IP_target", file=sys.stderr)
        parser.exit()
    if not re.match(r"[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\1[0-9a-f]{2}){4}$",
                    args.MAC_src.lower()):
        print("Error: wrong format for MAC_src", file=sys.stderr)
        parser.exit()
    if not re.match(r"[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\1[0-9a-f]{2}){4}$",
                    args.MAC_target.lower()):
        print("Error: wrong format for MAC_target", file=sys.stderr)
        parser.exit()


def parse_arguments():
    '''parse the program arguments'''
    parser = argparse.ArgumentParser(prog='inquisitor', allow_abbrev=False,
                                     description='A program to simulate \
                                        arp poisoning attacks')
    parser.add_argument("IP_src", metavar="IP_SRC", type=str,
                        help="source IP address (IPV4 only)")
    parser.add_argument("MAC_src", metavar="MAC_SRC", type=str,
                        help="source MAC address")
    parser.add_argument("IP_target", metavar="IP_TARGET", type=str,
                        help="target IP address (IPV4 only)")
    parser.add_argument("MAC_target", metavar="MAC_TARGET", type=str,
                        help="target MAC address")
    parser.add_argument("-v", "--verbose", action='store_true',
                        help="display all ftp actions")
    args = parser.parse_args()
    verify_address(args, parser)
    return args
