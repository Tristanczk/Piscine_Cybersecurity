from bs4 import BeautifulSoup
import argparse
import requests
import sys

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
	return args

def main():
	extensions = ["jpeg", "jpg", "png", "gif", "bmp"]
	args = parse_arguments()
	try:
		request = requests.get(args.url)
	except:
		print('Provided URL is not valid.', file=sys.stderr)
		return
	print(request.text)
	
	

if __name__ == '__main__':
	main()