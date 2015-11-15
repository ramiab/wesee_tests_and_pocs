import os
import sys

#----------Create a program that recieves paths of a file opens a text file and writes all those paths in that file-----------

SourcePath = input('Please enter your INPUT path: ')

onlyfiles = [ os.path.join(SourcePath,f) for f in os.listdir(SourcePath) if os.path.isfile(os.path.join(SourcePath,f)) ]

file_locations = open(os.path.join(sys.path[0], "FileLocationsB.txt"), "a")

number_of_items = 0

def write_to_file(onlyfiles,file_locations):
	global number_of_items
	for full_file_name in onlyfiles:
		print("-working-")
		number_of_items = number_of_items + 1
		file_locations.write(full_file_name+"\n")
write_to_file(onlyfiles,file_locations)

#file_locations.close()
	
print ("You have written " + str(number_of_items) + " files using this script")

#--Interesting:--
#f = open(local_file,"r")
#for line in f:
#    searchphrase = '<span class="position'
#    if searchphrase in line:
#        print("found it\n")
#--search something in an html page---http://stackoverflow.com/questions/15656817/python-3-x-move-to-next-line