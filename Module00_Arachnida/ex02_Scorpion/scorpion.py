import sys
import os
import exif

extensions = [".jpeg", ".jpg", ".png", ".gif", ".bmp"]

fields = {
	"make": "Camera Brand",
	"model": "Camera Model",
	"x_resolution": "Horizontal Resolution",
	"y_resolution": "Vertical Resolution",
	"software": "Software",
	"datetime": "Last Modified",
	"exposure_time": "Exposure Time",
	"f_number": "F-Number",
	"datetime_original": "Date Taken",
	"datetime_digitized": "Date Digitized",
	"shutter_speed_value": "Shutter Speed",
	"aperture_value": "Aperture",
	"brightness_value": "Brightness",
	"exposure_bias_value": "Exposure Bias",
	"focal_length": "Focal Length",
	"pixel_x_dimension": "Width (pixels)",
	"pixel_y_dimension": "Height (pixels)",
	"focal_plane_x_resolution": "Focal Plane X-Resolution",
	"focal_plane_y_resolution": "Focal Plane Y-Resolution",
	"body_serial_number": "Body Serial Number",
}

def handle_file_metadata(file):
	print(f"-----Image: {file}-----")
	_, file_extension = os.path.splitext(file)
	if file_extension not in extensions:
		print(f'File {file} extension is not valid. Accepted files are: .jpeg, .jpg, .png, .gif, .bmp.\n', file=sys.stderr)
		return
	try:
		with open(file, "rb") as f:
			exifdata = exif.Image(f)
	except Exception as e:
		print(f'Error opening the file: {e}\n', file=sys.stderr)
		return
	print(exifdata.list_all())
	if exifdata.has_exif:
		for key, value in fields.items():
			if key in exifdata.list_all():
				print(f"{value:25} : {exifdata.get(key)}")
		print()
	else:
		print("No EXIF data found in the image file.\n")

def main():
	if (len(sys.argv) < 2):
		print('Usage: python3 File1 [File2 ...]', file=sys.stderr)
		return		
	for arg in sys.argv[1:]:
		handle_file_metadata(arg)

if __name__ == '__main__':
	main()