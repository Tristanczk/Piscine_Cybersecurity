import argparse
import sys


class versionAction(argparse.Action):
    def __call__(self, parser, args, values, option_string=None):
        print("Version: 1.0")
        parser.exit()


def check_key(s, parser):
    """check if key is valid: at least 16 characters,
    only alphanumeric characters"""
    if len(s) < 16:
        print("Provided encryption key must be at least 16 characters long",
              file=sys.stderr)
        parser.exit()
    for c in s:
        if not c.isalnum():
            print("Encryption key must be only alphanumeric characters",
                  file=sys.sdterr)
            parser.exit()


def parse_arguments():
    '''parse the program arguments'''
    parser = argparse.ArgumentParser(prog='stockholm', allow_abbrev=False,
                                     description='A program that simulates the\
                                        behaviours of a malware inspecting\
                                        files')
    parser.add_argument("key", metavar="KEY", type=str,
                        help="program encryption key")
    parser.add_argument("-v", "--version", nargs=0, action=versionAction,
                        help="show program version")
    parser.add_argument("-r", "--reverse", action='store_true',
                        help="reverse malware infection using provided key")
    parser.add_argument("-s", "--silent", action='store_true',
                        help="silence program output")
    args = parser.parse_args()
    check_key(args.key, parser)
    return args
