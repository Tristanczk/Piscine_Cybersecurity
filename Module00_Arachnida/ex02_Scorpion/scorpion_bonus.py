import sys
import os
import PySimpleGUI as sg
from PIL import Image
from PIL.ExifTags import TAGS

extensions = [".jpeg", ".jpg", ".png", ".gif", ".bmp"]

fields = {
	"Make": "Camera Brand",
	"Model": "Camera Model",
	"XResolution": "Horizontal Resolution",
	"YResolution": "Vertical Resolution",
	"Software": "Software",
	"DateTime": "Last Modified",
	"ResolutionUnit": "Resolution Unit",
}

def handle_file_metadata(file, window):
	_, file_extension = os.path.splitext(file)
	if file_extension not in extensions:
		window["status"].update("File extension is not valid. Accepted files are: .jpeg, .jpg, .png, .gif, .bmp.", visible=True)
		for key in fields:
			window[key].update("")
		return
	try:
		image = Image.open(file)
	except Exception as e:
		window["status"].update("Error opening the file", visible=True)
		for key in fields:
			window[key].update("")
		return
	exifdata = image.getexif()
	window["status"].update("", visible=False)
	for tag_id in exifdata:
		tag = TAGS.get(tag_id, tag_id)
		data = exifdata.get(tag_id)
		if isinstance(data, bytes):
			try:
				data = data.decode()
			except:
				continue
		if tag in fields:
			window[tag].update(data)

def main():
	if (len(sys.argv) < 2):
		print('Usage: python3 File1 [File2 ...]', file=sys.stderr)
		return		
	sg.theme("DarkGrey5")
	sg_elements = [
		[
			sg.Text("Select an image: ", size=(20, 1)),
			sg.Combo(sys.argv[1:], size=(50, 1), key="image", enable_events=True),
		],
		[sg.Text("", key="status", text_color="red", visible=False, justification="center", size=(70, 1))]
	]
	for key, value in fields.items():
		sg_elements.append([sg.Text(f"{value}: ", size=(20, 1)), sg.Text("", size=(50, 1), key=key)])
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