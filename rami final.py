import argparse
import os
#rami final script
def find_file():
    args = get_args()
    SourceFolder = args.src_folder
    
    for file in os.listdir(SourceFolder):
        if os.path.isfile (os.path.join(SourceFolder,file)):
            print(file)

def get_args():
    parser = argparse.ArgumentParser('This tool returns list of filenames and calculates a Factorial Function')
    parser.add_argument('src_folder', help='The folder you would like to list')
    parser.add_argument('-x', default=3, help='The number of iterations you would like to use (only integers)', type=int)
    parser.add_argument('-v', action='store_true', default=False, help='Optional. Verbose.')

    args = parser.parse_args()
    return args

students = ['nico', 'emma', 'alina', 'andrei', 'alina', 'clarisa', 'eli']
def get_students_list():
	return students


def main():
    args = get_args()
    
    counter = 1
    for i in range(args.x - 1):
        counter = counter * (i+1)
        if args.v:
            print ("Calculating {0} X {1}".format(i+1,i+2))
			print("The sum of the function equals to: {0}".format(counter))
	print("The sum of the function equals to: {0}".format(counter))
     
    find_file()
            
        
        
if __name__ == '__main__':
   main()