import urllib.request
import os
import shutil
import argparse

url_list = ['http://www.ynet.co.il/home/0,7340,L-8,00.html','http://www.mako.co.il/','http://www.nana10.co.il/']


def get_args():
   parser = argparse.ArgumentParser(description='This tool copies X files from source-dir to destination-dir.')
#  parser.add_argument('source_dir', help='From where to copy.')
   parser.add_argument('-v', action="store_true", default=True, help='Optional. Verbose.') 

   args = parser.parse_args()

   # args manipulation ...

   return args


def extractHTML(url_list):
	args = get_args()
#    folder_path = r"C:\\Users\WeSEE_Eli\Desktop\RAMMI\test"
	counter = 1
	if args.v:

		for each in url_list:
			f = open('temphtml{0}.html'.format(counter), 'wb')
			print("Creating html file")
			page = urllib.request.urlopen(each)
			page = page.read()
			print ("We have imported the source code from the url")
			f.write(page)
			f.close()
			print("The page was saved")
	#       os.path.join(folder_path,'temphtml{0}.txt'.format(counter))
			counter = counter + 1
		else:
			f = open('temphtml{0}.html'.format(counter), 'wb')
			page = urllib.request.urlopen(each)
			page = page.read()
			f.write(page)
			f.close()
	#       os.path.join(folder_path,'temphtml{0}.txt'.format(counter))
			counter = counter + 1
        
   
def main():
   args = get_args()
   extractHTML(url_list)
 #  print("args = {}".format(args))


if __name__ == '__main__':
   main()
