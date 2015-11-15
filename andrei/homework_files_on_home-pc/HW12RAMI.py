import os
import shutil

def copy_and_paste():

	SOURCEPATH = r"C:\Users\WeSEE 15\Desktop\Python HW 12\Python 12 HW\Python 12 HW\tempFolder\FolderAwithFiles"
	DESTINATIONPATH =r"C:\Users\WeSEE 15\Desktop\Python HW 12\Python 12 HW\Python 12 HW\tempFolder\FolderOutput"

	print ("This program lets you copy or move files from one folder to another \n")
	print ("This is your source path: \n",SOURCEPATH)
	print ("This is your destination path: \n",DESTINATIONPATH)
	print ('\n')
	
	
	print ("These are the files affected by the script :\n")
	onlyfiles = [ os.path.join(SOURCEPATH,f) for f in os.listdir(SOURCEPATH) if os.path.isfile(os.path.join(SOURCEPATH,f)) ]
	print (onlyfiles)
	print ('\n')
	print ("These folders are not affected by the script :")
	onlyfolders = [ f for f in os.listdir(SOURCEPATH) if os.path.isdir(os.path.join(SOURCEPATH,f)) ]
	print (onlyfolders)
	print ('\n')
	
	
	choose_either_move_or_copy = int(input('Please enter 1 to copy your files or enter 2 to move them: \n'))
	print ("You chose option nr \n", choose_either_move_or_copy + 0)

	#src_files = os.listdir(SOURCEPATH) #--Works till here--
	#print ("These are the files and folders present in the directory \n", src_files)

	for full_file_name in onlyfiles:
		if choose_either_move_or_copy == 1:                    #----The integer input works
			shutil.copy(full_file_name, DESTINATIONPATH)
		elif choose_either_move_or_copy == 2: 
			shutil.move(full_file_name, DESTINATIONPATH)				
		else:
			print ("You did not insert a valid number.Please run script again.")      #-----WORKS!!---
copy_and_paste()


