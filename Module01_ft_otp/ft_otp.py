#!/usr/bin/python3
import sys
from check_args import parse_arguments, verify_args
from cryptography.fernet import Fernet


encryption_key_file = "encryption_key.key"


def generate_encryption_key():
    encryption_key = Fernet.generate_key()
    try:
        with open(encryption_key_file, "wb") as f:
            f.write(encryption_key)
        return encryption_key
    except Exception as e:
        print(f"./ft_opt: error with the encryption key: {e}",
              file=sys.stderr)
        return


def generate_key_file(key):
    encryption_key = generate_encryption_key()
    if not encryption_key:
        return
    try:
        cipher = Fernet(encryption_key)
        with open("ft_otp.key", "wb") as f:
            f.write(cipher.encrypt(key))
    except Exception as e:
        print(f"./ft_otp: error: {e}", file=sys.stderr)


def generate_password(key):


def main():
    args = parse_arguments()
    key = verify_args(args, encryption_key_file)
    if not key:
        return
    if args.g:
        generate_key_file(key)
    else:
        generate_password(key)


if __name__ == "__main__":
    main()
