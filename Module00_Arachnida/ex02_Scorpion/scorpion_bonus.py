import sys
import os
import pyexiv2
import PySimpleGUI as sg

extensions = [".jpeg", ".jpg", ".png", ".gif", ".bmp"]

fields = {
	"Make": "Camera Brand",
	"Model": "Camera Model",
	"XResolution": "Horizontal Resolution",
	"YResolution": "Vertical Resolution",
	"Software": "Software",
	"DateTime": "Last Modified",
	"ExposureTime": "Exposure Time",
	"FNumber": "F-Number",
	"ISOSpeedRatings": "ISO Speed Ratings",
	"DatetimeOriginal": "Date Taken",
	"ShutterSpeedValue": "Shutter Speed",
	"ApertureValue": "Aperture",
	"BrightnessValue": "Brightness",
	"ExposureBiasValue": "Exposure Bias",
	"Flash": "Flash",
	"FocalLength": "Focal Length",
	"PixelXDimension": "Width",
	"PixelYDimension": "Height",
	"FocalPlaneXResolution": "Focal Plane X-Resolution",
	"FocalPlaneYResolution": "Focal Plane Y-Resolution",
	"BodySerialNumber": "Body Serial Number",
}

def handle_file_metadata(file):
	print(f"-----Image: {file}-----")
	_, file_extension = os.path.splitext(file)
	if file_extension not in extensions:
		print(f'File {file} extension is not valid. Accepted files are: .jpeg, .jpg, .png, .gif, .bmp.\n', file=sys.stderr)
		return
	try:
		metadata = pyexiv2.ImageMetadata(file)
		metadata.read()
	except Exception as e:
		print(f'Error opening the file: {e}\n', file=sys.stderr)
		return
	for key in metadata.exif_keys:
		print(f"{key.split('.')[-1]:25}: {metadata[key].value}")
	print()

def main():
	if (len(sys.argv) < 2):
		print('Usage: python3 File1 [File2 ...]', file=sys.stderr)
		return		
	
	sg_elements = [
		[
			sg.Text("Select an image: ", size=(20, 1)),
			sg.Combo(sys.argv[1:], size=(50, 1), key="image", enable_events=True),
		],
		[sg.Button("OK")]
	]
	window = sg.Window("Scorpion", sg_elements)
	# for arg in sys.argv[1:]:
	# 	handle_file_metadata(arg)
	while True:
		event, values = window.read()

		if event == sg.WINDOW_CLOSED:
			break
		elif event == "OK":
			selected_file = values["image"]
			sg.popup(f"You selected: {selected_file}")

	window.close()


if __name__ == '__main__':
	main()