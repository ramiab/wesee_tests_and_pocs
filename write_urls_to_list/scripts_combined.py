import argparse
import get_urls
import write_html
import os

'''
1. Change the write_html script in a way that it will contain the “with as” function. Instead of: “f = open” and “f.close”
2. In write_html script. Set an argument of destination folder for the new files.
3. In write_html script, catch possible exceptions  with try & except functions in relevant places.
4. Finish the script_combined script.
'''

def get_args():
	parser = argparse.ArgumentParser("This script gets urls from list")
	parser.add_argument('file', help="Should be file with .txt format only")
	parser.add_argument('dest_dir', help="Would you like to save to a specific folder?")
	parser.add_argument('-v', action="store_true", default=False, help='Optional. Verbose.')
	args_scripts_combined = parser.parse_args()
   
	return args_scripts_combined

def main():
	args_scripts_combined = get_args()
	urls = get_urls.get_urls_from_file(args_scripts_combined.file)
	print (urls)
	write_html.extractHTML(urls,args_scripts_combined.dest_dir,args_scripts_combined.v)
	
        
if __name__ == '__main__':
   main()