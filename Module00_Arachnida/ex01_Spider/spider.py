from bs4 import BeautifulSoup
import argparse
import requests
import sys
import os
from urllib.parse import urlsplit

extensions = [".jpeg", ".jpg", ".png", ".gif", ".bmp"]
count = 0

def parse_arguments():
	parser = argparse.ArgumentParser(prog='Spider', description='A program that downloads image from a given URL.')
	parser.add_argument('url', metavar='URL', type=str, help='enter the URL that you want to download images from')
	
	parser.add_argument('-r', action='store_true', help='use this flag to download the images recursively')
	parser.add_argument('-l', metavar='LEVEL', type=int, help='use this flag to specify the maximum depth level of the recursive download. Default depth level is 5. This flag can only be used with -r')
	parser.add_argument('-p', metavar='PATH', type=str, default='./data/', help='use this flag to specify the output directory for the images. Default output directory is ./data/')
	args = parser.parse_args()
	if args.l and not args.r:
		parser.error('-l option cannot be used without -r')
	elif args.r and not args.l:
		args.l = 5
	elif args.r and args.l < 1:
		parser.error('Depth level cannot be less than 1')
	return args

def make_output_dir(path):
	if not os.path.exists(path):
		try:
			os.mkdir(path)
		except FileNotFoundError:
			print(f'Provided path for output directory is not valid: {path}', file=sys.stderr)
			sys.exit(1)

def scrape_images(url, output_dir, depth_level, max_depth_level):
	global count
	if depth_level > max_depth_level:
		return
	try:
		request = requests.get(url)
	except:
		print(f'Provided URL is not valid: {url}', file=sys.stderr)
		return
	soup = BeautifulSoup(request.text, 'html.parser')
	split_url = urlsplit(url)

	images = soup.find_all('img')
	for image in images:
		image_url = image.attrs.get('src')
		if not image_url:
			print('Could not find image URL', file=sys.stderr)
			continue
		_, file_extension = os.path.splitext(image_url)
		if file_extension not in extensions:
			continue
		if not (image_url.startswith('http')):
			if image_url.startswith('//'):
				image_url = split_url.scheme + ':' + image_url
			elif image_url.startswith('/'):
				image_url = split_url.scheme + '://' + split_url.netloc + image_url
			else:
				image_url = split_url.scheme + '://' + split_url.netloc + '/' + image_url
		with open(output_dir + 'image' + str(count) + file_extension, 'wb') as f:
			try:
				r = requests.get(image_url)
				f.write(r.content)
				count += 1
				print(f"{count} images downloaded", end="\r")
			except:
				continue

def main():
	args = parse_arguments()
	make_output_dir(args.p)
	if args.r:
		scrape_images(args.url, args.p, 1, args.l)
	else:
		scrape_images(args.url, args.p, 1, 1)
	print(f'{count} images downloaded')
	
if __name__ == '__main__':
	main()