import os


def main():
    try:
        with open("level1", 'rb') as f:
            data = bytearray(f.read())
            '''change the hex value at emplacement 0x1234
            to change one of the strcmp argument
            as a result, strcmp doesn't compare the input entered
            to another sentence but to itself, always returning 1
            apply a modification obtained by modifying the file on ghidra'''
            data[0x1234] = 0x94
            print("Patch applied...")
    except Exception as e:
        print(f"Error opening the level1 file: {e}")
    try:
        with open("level1_patched", 'wb') as f:
            f.write(data)
        os.chmod("level1_patched", 0o755)
        print("Patched file saved as level1_patched")
    except Exception as e:
        print(f"Error writing the patched file: {e}")


if __name__ == "__main__":
    main()
