import urllib.request
import urllib.error
import argparse
import os

def get_args():
	parser = argparse.ArgumentParser('This tool copies X files from source-dir to destination-dir.')
	parser.add_argument('-v', action="store_true", default=False, help='Optional. Verbose.')
	parser.add_argument('url_str', help="input comma delimited string of urls")
	parser.add_argument('dest_dir', help="Would you like to save to a specific folder?")
	args_write = parser.parse_args()

	return args_write
    
# types of error this code can throw
# IO error cannot find folder
# httperror in finding the url
# try except finally

def extractHTML(url_list,dest_dir,is_verbose):
	counter = 1
	try:
		for url in url_list:
			page = urllib.request.urlopen(url)
			page = page.read()
			os.chdir(dest_dir)
			os.getcwd()
			if is_verbose:
				print("Printing data to file")
			with open ('File_{0}.html'.format(counter), 'wb') as f:
				if is_verbose:
					print("Creating HTML File")
				f.write(page)
				counter = counter + 1
				if is_verbose:
					print("Saving file")
	except urllib.error.URLError:
		print ('EXEPTION There was an error opening this page: \n'+url)
		pass
	except ValueError:
		print ('EXEPTION Unknown URL type: \n'+url)
		pass
	except IOError:
		print ('EXEPTION Cannot find this destination directory: \n'+dest_dir)


def main():
	args_write = get_args()
	urls_string = args_write.url_str
	print (urls_string) #for Debug
	urls = urls_string.split(';')
	print (urls) #for Debug
	extractHTML(urls,args_write.dest_dir,args_write.v)
  

if __name__ == '__main__':
   main()

   
# new_dir = args_write.dest_dir
# os.chdir(new_dir)
# os.getcwd()