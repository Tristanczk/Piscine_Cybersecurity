import sys
import os
import pyexiv2
import PySimpleGUI as sg

extensions = [".jpeg", ".jpg", ".png", ".gif", ".bmp"]

def handle_file_metadata(file):
	print(f"-----Image: {file}-----")
		_, file_extension = os.path.splitext(file)
		if file_extension not in extensions:
			print(f'File {file} extension is not valid. Accepted files are: .jpeg, .jpg, .png, .gif, .bmp.\n', file=sys.stderr)
			continue
		try:
			metadata = pyexiv2.ImageMetadata(file)
			metadata.read()
		except Exception as e:
			print(f'Error opening the file: {e}\n', file=sys.stderr)
			continue
		for key in metadata.exif_keys:
			print(f"{key.split('.')[-1]:25}: {metadata[key].value}")
		print()

def main():
	if (len(sys.argv) < 2):
		print('Usage: python3 File1 [File2 ...]', file=sys.stderr)
		return		
	for arg in sys.argv[1:]:
		handle_file_metadata(arg)


if __name__ == '__main__':
	main()