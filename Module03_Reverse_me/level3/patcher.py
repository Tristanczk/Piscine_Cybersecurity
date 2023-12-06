import os

'''here we change the approach and we just change a line
so after the call to scanf,
we jump to the part of the program where
we call the right ____syscall_malloc function at the end'''


def main():
    try:
        with open("level3", 'rb') as f:
            data = bytearray(f.read())
            data[0x1352:0x1352+5] = b'\xe9\07\x02\x00\x00'
    except Exception as e:
        print(f"Error opening the level1 file: {e}")
    try:
        with open("level3_patched", 'wb') as f:
            f.write(data)
        os.chmod("level3_patched", 0o755)
        print("Patched file saved as level3_patched")
    except Exception as e:
        print(f"Error writing the patched file: {e}")


if __name__ == "__main__":
    main()
