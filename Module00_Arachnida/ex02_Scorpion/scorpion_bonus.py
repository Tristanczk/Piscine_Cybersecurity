import sys
import os
import PySimpleGUI as sg
import exif
import argparse

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
		return False
	try:
		with open(file, "rb") as f:
			exifdata = exif.Image(f)
	except Exception as e:
		window["status"].update("Error opening the file", visible=True)
		for key in fields:
			window[key].update("")
		return False
	if exifdata.has_exif:
		window["status"].update("", visible=False)
		for key, _ in fields.items():
			if key in exifdata.list_all():
				window[key].update(exifdata.get(key))
			else:
				window[key].update("Unavailable data")
	else:
		window["status"].update("No EXIF data found in the image file.", visible=True)
		for key in fields:
			window[key].update("")
		return False
	return True

def edit_file_data(key, window, selected_file):
	if selected_file is None:
		window["status"].update("Please select a valid file to update values", visible=True)
		return
	new_value = sg.popup_get_text(f"Enter the new value for {fields[key]}: ")
	if new_value is None:
		return
	with open(selected_file, "rb") as f:
		exifdata = exif.Image(f)
	while True:
		try:
			exifdata[key] = new_value
			break
		except Exception as e:
			new_value = sg.popup_get_text(f"Error: {e}\nEnter the new value for {fields[key]}: ")
			if new_value is None:
				return
	with open(selected_file, "wb") as of:
		of.write(exifdata.get_file())
	window[key].update(new_value)

def erase_file_data(key, window, selected_file):
	if selected_file is None:
		window["status"].update("Please select a valid file to update values", visible=True)
		return
	check = sg.popup_yes_no(f"Are you sure you want to remove the {fields[key]} metadata from the file?")
	if check == "No":
		return
	else:
		with open(selected_file, "rb") as f:
			exifdata = exif.Image(f)
		exifdata.delete(key)
		with open(selected_file, "wb") as of:
			of.write(exifdata.get_file())
		window[key].update("Unavailable data")

def main():
	parser = argparse.ArgumentParser(prog='Scorpion', description='A program to see and manage exif metadata of an image file.')
	parser.add_argument('-m', action='store_true', help='use this flag to enable modification / deletion of the metadata')
	parser.add_argument('files', metavar='FILES', nargs='+', type=str, help='Enter the files that you want to see the metadata of (at least one file is required)')
	args = parser.parse_args()
		
	sg.theme("DarkGrey14")
	sg_elements = [
		[
			sg.Text("Select an image: ", size=(25, 1)),
			sg.Combo(args.files, size=(40, 1), key="image", enable_events=True),
		],
		[sg.Text("", key="status", text_color="red", visible=False, justification="center", size=(90, 1))]
	]
	# need to add option in the program to activate the edit and remove buttons
	for key, value in fields.items():
		if args.m:
			sg_elements.append([sg.Text(f"{value}: ", size=(25, 1)), sg.Text("", size=(70, 1), key=key), sg.Button(image_filename="pencil.png", image_size=(10, 10), key=f"edit_{key}", tooltip="Edit"), sg.Button(image_filename="eraser.png", image_size=(10, 10), key=f"remove_{key}", tooltip="Remove")])
		else:
			sg_elements.append([sg.Text(f"{value}: ", size=(25, 1)), sg.Text("", size=(70, 1), key=key)])
	window = sg.Window("Scorpion", sg_elements)
	selected_file = None
	while True:
		event, values = window.read()
		if event == sg.WINDOW_CLOSED:
			break
		elif event == "image":
			selected_file = values["image"]
			if not handle_file_metadata(selected_file, window):
				selected_file = None
		elif event.startswith("edit_"):
			key = event[5:]
			edit_file_data(key, window, selected_file)
		elif event.startswith("remove_"):
			key = event[7:]
			erase_file_data(key, window, selected_file)
	window.close()

if __name__ == '__main__':
	main()