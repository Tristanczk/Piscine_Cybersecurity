import sys
import os
import PySimpleGUI as sg
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

def handle_file_metadata(file, window):
	_, file_extension = os.path.splitext(file)
	if file_extension not in extensions:
		window["status"].update("File extension is not valid. Accepted files are: .jpeg, .jpg, .png, .gif, .bmp.", visible=True)
		for key in fields:
			window[key].update("")
		return
	try:
		with open(file, "rb") as f:
			exifdata = exif.Image(f)
	except Exception as e:
		window["status"].update("Error opening the file", visible=True)
		for key in fields:
			window[key].update("")
		return
	window["status"].update("", visible=False)
	if exifdata.has_exif:
		for key, _ in fields.items():
			if key in exifdata.list_all():
				window[key].update(exifdata.get(key))
	else:
		window["status"].update("No EXIF data found in the image file.", visible=True)

def main():
	if (len(sys.argv) < 2):
		print('Usage: python3 File1 [File2 ...]', file=sys.stderr)
		return		
	sg.theme("DarkGrey5")
	sg_elements = [
		[
			sg.Text("Select an image: ", size=(25, 1)),
			sg.Combo(sys.argv[1:], size=(40, 1), key="image", enable_events=True),
		],
		[sg.Text("", key="status", text_color="red", visible=False, justification="center", size=(90, 1))]
	]
	for key, value in fields.items():
		sg_elements.append([sg.Text(f"{value}: ", size=(25, 1)), sg.Text("", size=(70, 1), key=key)])
	window = sg.Window("Scorpion", sg_elements)
	while True:
		event, values = window.read()

		if event == sg.WINDOW_CLOSED:
			break
		elif event == "image":
			selected_file = values["image"]
			handle_file_metadata(selected_file, window)

	window.close()

if __name__ == '__main__':
	main()