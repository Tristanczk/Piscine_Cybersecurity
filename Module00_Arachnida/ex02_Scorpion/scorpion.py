import sys
import os
import pyexiv2

extensions = [".jpeg", ".jpg", ".png", ".gif", ".bmp"]

def main():
	if (len(sys.argv) < 2):
		print('Usage: python3 File1 [File2 ...]', file=sys.stderr)
		return		
	for arg in sys.argv[1:]:
		print(f"-----Image: {arg}-----")
		_, file_extension = os.path.splitext(arg)
		if file_extension not in extensions:
			print(f'File {arg} extension is not valid. Accepted files are: .jpeg, .jpg, .png, .gif, .bmp.\n', file=sys.stderr)
			continue
		try:
			metadata = pyexiv2.ImageMetadata(arg)
			metadata.read()
		except Exception as e:
			print(f'Error opening the file: {e}\n', file=sys.stderr)
			continue
		for key in metadata.exif_keys:
			print(f"{key.split('.')[-1]:25}: {metadata[key].value}")
		print()


if __name__ == '__main__':
	main()