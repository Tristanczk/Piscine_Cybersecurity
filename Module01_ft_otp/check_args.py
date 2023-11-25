import argparse
import sys
from cryptography.fernet import Fernet


def parse_arguments():
    '''parse the program arguments'''
    parser = argparse.ArgumentParser(prog='ft_otp',
                                     description='A program that generates one\
                                         time use password based on time.')
    parser.add_argument('file',
                        metavar='FILE',
                        type=str,
                        help='enter the path to the file you want to use')
    flags = parser.add_mutually_exclusive_group()
    flags.add_argument('-g', action='store_true',
                       help='use this flag to generate key')
    flags.add_argument('-k', action='store_true',
                       help='use this flag to generate one time use password')
    args = parser.parse_args()
    return args


def check_key(key):
    '''check the validity of the key'''
    if len(key) != 64:
        print("./ft_otp: error: key must be 64 hexadecimal characters",
              file=sys.stderr)
        return False
    '''we check if the string is convertible in an int in base 16 to
    see if we only have hexadecimal characters'''
    try:
        int(key, 16)
    except ValueError:
        print("./ft_otp: error: key must be 64 hexadecimal characters",
              file=sys.stderr)
        return False
    return True


def verify_key(file):
    '''verify the hexadecimal key given in the file'''
    try:
        with open(file, "rb") as f:
            s = f.read()
            if not check_key(s):
                return
    except Exception as e:
        print(f"./ft_otp: error: {e}", file=sys.stderr)
        return
    return s


def verify_key_file(file, encryption_key_file):
    '''verify the validity of the given key file'''
    if (file != "ft_otp.key"):
        print("Invalid file for key, file must be ft_otp.key", file=sys.stderr)
        return
    try:
        decryption_key = open(encryption_key_file, "rb").read()
        cipher = Fernet(decryption_key)
    except Exception as e:
        print(f"./ft_otp: error when accessing decryption key: {e}",
              file=sys.stderr)
        return
    try:
        with open(file, "rb") as f:
            key = f.read()
            key = cipher.decrypt(key)
        if not check_key(key):
            return
    except Exception as e:
        print(f"./ft_otp: error: {e}", file=sys.stderr)
        return
    return key


def verify_args(args, encryption_key_file):
    '''verify the validity of the arguments parsed'''
    if (not args.g and not args.k):
        print("Please specify a flag for usage (-g or -k)", file=sys.stderr)
        return
    if (args.g):
        key = verify_key(args.file)
        return key
    if (args.k):
        key = verify_key_file(args.file, encryption_key_file)
        return key
