import argparse
import re

def get_args():
	parser = argparse.ArgumentParser("This script gets urls from list")
	parser.add_argument('file', help="Should be file with .txt format only")
	args_get_urls = parser.parse_args()
   
	return args_get_urls


def get_urls_from_file(my_file):
	url_list = []
	with open (my_file) as f:
		lines=f.readlines()
		for line in lines:
			if re.match("http[s]?://", line):
				url = line.rstrip()
				url_list.append(url)

	return url_list

	
def main():
	args_get_urls = get_args()
	get_urls_from_file(args_get_urls.file)
	print (url_list) # Just for Debug
    
    
if __name__ == '__main__':
   main()