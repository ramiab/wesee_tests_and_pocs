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
	parser.add_argument('file', help="What file/ files do you want to copy?")
	parser.add_argument('dest_dir', help="To what folder should the files be copied to?")
	parser.add_argument('-v', action="store_true", default=False, help='Optional. Verbose.')
	args_scripts_combined = parser.parse_args()
   
	return args_copy_network

def copy_files_network(file,dest_folder,verbose):
	if not os.path.isdir(dest_folder):
		os.mkdir(dest_folder)
		print('Directory created at: ' + dest_folder) #make verbouse




	
	
	
	
	
	
	
	
	
	
#        if not os.path.isfile(newLoc):
#            try:
#                shutil.copy2(oldLoc, newLoc)
#                print('File ' + f + ' copied.')
#            except IOError:
#                print('file "' + f + '" already exists')
	
	
def main():
	args_copy_network = get_args()

	
        
if __name__ == '__main__':
   main()