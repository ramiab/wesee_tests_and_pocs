import argparse
import os
import shutil

# This script needs to be able to copy files fron a network location into a user provided folder
# Purhaps copy and move
# Purhps delete
# Purhaps check if file exists in new folder
# Check if there is a file with the same name in the folder. etc.
# Check if folder exists then create
# How do I choose which file to copy?
# Destination location must be writable.
# Do you want to copy files and subfolders?

def get_args():
	parser = argparse.ArgumentParser("This script can copy files from a network location to a local folder")
	parser.add_argument('source_dir', help="The source folder of the file")
#	parser.add_argument('file', help="What file/ files do you want to copy?")
	parser.add_argument('dest_dir', help="To what folder should the files be copied to?")
	parser.add_argument('-v', action="store_true", default=False, help='Optional. Verbose.')
	args_copy_network = parser.parse_args()
   
	return args_copy_network

def copy_files_network(source_dir,dest_dir,verbose):
	if not os.path.isdir(dest_dir):
		os.mkdir(dest_dir)
		if verbose:
			print('Directory created at: ' + dest_dir)
	source = os.listdir(source_dir)
	for file in source:
		full_file_name = os.path.join(source_dir, file)
		if verbose:	
			print('for file in source: '+file)
		if (os.path.isfile(full_file_name)):
			if verbose:
				print ('if os.path.isfile '+file)
			try:
				if verbose:
					print ('enter try loop')
				shutil.copy(full_file_name, dest_dir)
				if verbose:
					print ('File ' + file + ' copied.')
			except IOError:
				print('file "' + file + '" already exists')


	
def main():
	args_copy_network = get_args()
	copy_files_network(args_copy_network.source_dir,args_copy_network.dest_dir,args_copy_network.v)

	
if __name__ == '__main__':
   main()