import argparse
import sys


class versionAction(argparse.Action):
    def __call__(self, parser, args, values, option_string=None):
        print("Version: 1.0")
        parser.exit()


def check_key(s, parser, silent):
    """check if key corresponds to the saved key"""
    try:
        with open("key.key", "r") as f:
            key = f.read()
    except Exception as e:
        if not silent:
            print(f"Error accessing the key file: {e}", file=sys.stderr)
        parser.exit()
    if s != key:
        if not silent:
            print("Provided key doesn't match encryption key", file=sys.stderr)
        parser.exit()


def parse_arguments():
    '''parse the program arguments'''
    parser = argparse.ArgumentParser(prog='stockholm', allow_abbrev=False,
                                     description='A program that simulates the\
                                        behaviours of a malware inspecting\
                                        files')
    parser.add_argument("-v", "--version", nargs=0, action=versionAction,
                        help="show program version")
    parser.add_argument("-r", "--reverse", metavar='key', type=str,
                        help="reverse malware infection using provided key")
    parser.add_argument("-s", "--silent", action='store_true',
                        help="silence program output")
    args = parser.parse_args()
    if (args.reverse):
        check_key(args.reverse, parser, args.silent)
    return args
