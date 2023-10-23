import sys
import os
from PIL import Image
from PIL.ExifTags import TAGS

# need to check how to do it for image formats other than jpeg

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
			image = Image.open(arg)
		except Exception as e:
			print(f'Error opening the file: {e}\n', file=sys.stderr)
			continue
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


if __name__ == '__main__':
	main()