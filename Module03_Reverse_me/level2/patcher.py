import os

'''here we will patch the file by changing every calls
to the no function to call to the ok function'''


def main():
    try:
        with open("level2", 'rb') as f:
            data = bytearray(f.read())
            # compare 2nd char of input to itself instead of to '0'
            data[0x134f] = 0xc0
            # idem for 1st char of input
            data[0x1336] = 0xc0
            # at the end, replace the call to strcmp by a XOR EAX,EAX
            # so that EAX becomes 0 and the CMP operation after is always true
            # x90 bytes are NOP (no operation bytes and act as placeholder)
            data[0x1465:0x1465 + 5] = b'\x31\xc0\x90\x90\x90'
    except Exception as e:
        print(f"Error opening the level1 file: {e}")
    try:
        with open("level2_patched", 'wb') as f:
            f.write(data)
        os.chmod("level2_patched", 0o755)
        print("Patched file saved as level2_patched")
    except Exception as e:
        print(f"Error writing the patched file: {e}")


if __name__ == "__main__":
    main()
