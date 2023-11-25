#!/usr/bin/python3
import sys
from check_args import parse_arguments, verify_args
from cryptography.fernet import Fernet
import hmac
from datetime import datetime


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
        return
    print("Key was successfully saved in ft_otp.key.")


# based on https://www.rfc-editor.org/rfc/rfc4226#section-5.3
# and https://medium.com/zeals-tech-blog/implementing-your-own\
# -time-based-otp-generator-3b971a31330b
def hotp(key, count):
    '''generate hotp password'''
    count_bytes = count.to_bytes(8, byteorder="big")
    hmac_result = hmac.new(key, count_bytes, "sha1").digest()
    offset = hmac_result[19] & 15
    bin_code = ((hmac_result[offset] & 127) << 24 |
                (hmac_result[offset + 1] & 255) << 16 |
                (hmac_result[offset + 2] & 255) << 8 |
                (hmac_result[offset + 3] & 255)
                )
    return bin_code % 10**6


def generate_password(key):
    '''generate hotp password based on time passed since unix epoch'''
    today = datetime.today()
    count = int(today.timestamp() // 30)
    return hotp(key, count)


def main():
    args = parse_arguments()
    key = verify_args(args, encryption_key_file)
    if not key:
        return
    if args.g:
        generate_key_file(key)
    else:
        print(generate_password(key))


if __name__ == "__main__":
    main()
