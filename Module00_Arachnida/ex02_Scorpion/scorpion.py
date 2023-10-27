import sys
import os
from PIL import Image
from PIL.ExifTags import TAGS

extensions = [".jpeg", ".jpg", ".png", ".gif", ".bmp"]

def handle_file_metadata(file):
	print(f"-----Image: {file}-----")
	_, file_extension = os.path.splitext(file)
	if file_extension not in extensions:
		print(f'File {file} extension is not valid. Accepted files are: .jpeg, .jpg, .png, .gif, .bmp.\n', file=sys.stderr)
		return
	try:
		image = Image.open(file)
	except Exception as e:
		print(f'Error opening the file: {e}\n', file=sys.stderr)
		return
	exifdata = image.getexif()
	for tag_id in exifdata:
		tag = TAGS.get(tag_id, tag_id)
		data = exifdata.get(tag_id)
		if isinstance(data, bytes):
			try:
				data = data.decode()
			except:
				continue
		print(f"{tag:20}: {data}")
	print()

def main():
	if (len(sys.argv) < 2):
		print('Usage: python3 File1 [File2 ...]', file=sys.stderr)
		return		
	for arg in sys.argv[1:]:
		handle_file_metadata(arg)


if __name__ == '__main__':
	main()