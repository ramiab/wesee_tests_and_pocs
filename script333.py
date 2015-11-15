import urllib.request
import os
import shutil
import argparse

url_list = ['http://www.ynet.co.il/home/0,7340,L-8,00.html','https://clients6.google.com/static/proxy.html?jsh=m%3B%2F_%2Fscs%2Fabc-static%2F_%2Fjs%2Fk%3Dgapi.gapi.en.xjOqtrB8Fx8.O%2Fm%3D__features__%2Fam%3DAAQ%2Frt%3Dj%2Fd%3D1%2Frs%3DAItRSTOblpNtoWHpPOhBTtm7mc3TCZFA0g#parent=https%3A%2F%2Fwww.youtube.com&amp','http://www.nana10.co.il/']


def get_args():
   parser = argparse.ArgumentParser(description='This tool copies X files from source-dir to destination-dir.')
#  parser.add_argument('source_dir', help='From where to copy.')
   parser.add_argument('-v', action="store_false", default=True, help='Optional. Verbose.') 

   args = parser.parse_args()

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
