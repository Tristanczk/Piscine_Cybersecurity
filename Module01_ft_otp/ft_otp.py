#!/usr/bin/python3
import sys
from check_args import parse_arguments, verify_args, \
                       verify_key, verify_key_file
from cryptography.fernet import Fernet
import hmac
from datetime import datetime
import base64
import PySimpleGUI as sg


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
        return False
    try:
        cipher = Fernet(encryption_key)
        with open("ft_otp.key", "wb") as f:
            f.write(cipher.encrypt(key))
    except Exception as e:
        print(f"./ft_otp: error: {e}", file=sys.stderr)
        return False
    print("Key was successfully saved in ft_otp.key")
    return True


# based on https://www.rfc-editor.org/rfc/rfc4226#section-5.3
# and https://medium.com/zeals-tech-blog/implementing-your-own\
# -time-based-otp-generator-3b971a31330b
def hotp(key, count):
    '''generate hotp password'''
    key = base64.b32encode(bytes.fromhex(key.decode('utf-8')))
    key = base64.b32decode(key)
    count_bytes = count.to_bytes(8, byteorder="big")
    hmac_result = hmac.new(key, count_bytes, "sha1").digest()
    offset = hmac_result[-1] & 0x0f
    bin_code = ((hmac_result[offset] & 0x7f) << 24 |
                (hmac_result[offset + 1] & 0xff) << 16 |
                (hmac_result[offset + 2] & 0xff) << 8 |
                (hmac_result[offset + 3] & 0xff)
                )
    return bin_code % 10**6


def generate_password(key):
    '''generate hotp password based on time passed since unix epoch'''
    now = datetime.now()
    count = int(now.timestamp() // 30)
    return hotp(key, count)


def manage_interface():
    sg.theme("DarkGrey14")
    sg_elements = [
        [sg.Text("", key="status", text_color="white", visible=False,
                 justification="center", size=(800, 1))],
        [sg.Text("Select a file containing your hexadecimal key: ",
                 size=(40, 1)),
            sg.Input(), sg.FileBrowse(key='hex_key_file'),
            sg.Submit(key="submit_hex_key")],
        [sg.Push(), sg.Column([[sg.Submit(
            button_text="Generate one-time password",
            key="generate_pwd")]], element_justification='c'), sg.Push()],
        [sg.Text("", key="password", text_color="white", visible=False,
                 justification="center", size=(800, 1))],
    ]
    window = sg.Window("ft_otp", sg_elements, size=(800, 200))
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "submit_hex_key":
            window["status"].update(visible=False)
            window["password"].update(visible=False)
            key = verify_key(values["hex_key_file"])
            if not key:
                window["status"].update("Impossible to generate key file",
                                        visible=True)
            else:
                if generate_key_file(key):
                    window["status"].update(
                        "Key was successfully saved in ft_otp.key",
                        visible=True)
                else:
                    window["status"].update(
                        "Error when trying to save key in ft_otp.key",
                        visible=True)
        elif event == "generate_pwd":
            window["status"].update(visible=False)
            window["password"].update(visible=False)
            key = verify_key_file("ft_otp.key", encryption_key_file)
            if not key:
                window["status"].update("Impossible to access encrypted key",
                                        visible=True)
            else:
                window["password"].update("Your password is: " +
                                          "{:06d}".format(
                                              generate_password(key)),
                                          visible=True)
    window.close()


def main():
    args = parse_arguments()
    if not args.b:
        key = verify_args(args, encryption_key_file)
        if not key:
            return
        if args.g:
            generate_key_file(key)
        else:
            print("{:06d}".format(generate_password(key)))
    else:
        manage_interface()


if __name__ == "__main__":
    main()
