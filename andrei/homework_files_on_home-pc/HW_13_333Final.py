import os
import sys
import shutil
#----------THIS WORKS-------------
print ("This program lets you copy or move files or folders from one folder to another \n")

SourcePath = r"C:\Users\Andrei64\Desktop\Python Homework\Python 13\tempFolder\FolderAwithFiles" #--input('Please enter your correct INPUT path: ')
DestinationPath = r"C:\Users\Andrei64\Desktop\Python Homework\Python 13\tempFolder\FolderBWithFIles" #--input('Please enter your correct OUTPUT path: ')


print ("\n This is your source path: \n",SourcePath)
print ("This is your destination path: \n",DestinationPath)

		
choose_either_move_or_copy = int(input('Please enter \n 1 to COPY FILES \n 2 to MOVE FILES \n 3 to COPY FOLDERS \n 4 to MOVE FOLDERS \n'))
print ("You chose option nr \n", choose_either_move_or_copy + 0)

onlyfiles = [ os.path.join(SourcePath,f) for f in os.listdir(SourcePath) if os.path.isfile(os.path.join(SourcePath,f)) ]
onlyfolders = [ os.path.join(SourcePath,f) for f in os.listdir(SourcePath) if os.path.isdir(os.path.join(SourcePath,f)) ]

number_of_items = 0

def copy_and_paste():
	if choose_either_move_or_copy == 1 or 2 or 3 or 4:
		global number_of_items
		if choose_either_move_or_copy == 3:                      #--copy returns FileExistsError
			for full_file_name in onlyfolders:
				number_of_items = number_of_items + 1
				shutil.copy(full_file_name, DestinationPath)
		elif choose_either_move_or_copy == 4:
			for full_file_name in onlyfolders:
				number_of_items = number_of_items + 1
				shutil.move(full_file_name, DestinationPath)
		elif choose_either_move_or_copy == 1:
			for full_file_name in onlyfiles:
				number_of_items = number_of_items + 1
				shutil.copy(full_file_name, DestinationPath)
		elif choose_either_move_or_copy == 2:
			for full_file_name in onlyfiles:
				number_of_items = number_of_items + 1
				shutil.move(full_file_name, DestinationPath)
		else:
			print ("You did not insert a valid number.Please run the script again.")			
copy_and_paste()

print ('You worked with:'+ str(number_of_items)+' items')

#-----open(OperationParameters.txt,'a')