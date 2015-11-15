__author__ = 'Ilan Z'
import csv
import os

def main():
    #----------------------- Input pornography path and sub-folder name------------
	
   os.chdir(r"C:\Users\WeSEE 15\Desktop\AVI script try\batch22_27_8_15\test_results")
   
   srcDir = os.getcwd()
   
   filesDir = os.path.join(srcDir ,"Pornography")
   filesDir2 = os.path.join(srcDir ,"Sex")
   filesDir3 = os.path.join(srcDir ,"Partial Ndity")
   filesDir4 = os.path.join(srcDir ,"Nudity")
   filesDir5 = os.path.join(srcDir ,"Hentai")
   
   filesLst = os.listdir(filesDir)
   filesLst2 = os.listdir(filesDir2)
   filesLst3 = os.listdir(filesDir3)
   filesLst4 = os.listdir(filesDir4)
   filesLst5 = os.listdir(filesDir5)
      
   with open('downloaded.csv', 'r', newline='') as csvfile:
      with open('output.csv', 'w') as csvwriter:
         writerOutput = csv.writer(csvwriter)
         readerDownloaded = csv.reader(csvfile)
         for row in readerDownloaded:
            ID = row[0]
            FileName = row[1]
            if FileName in filesLst:
               writerOutput.writerow(row)
			   
	with open('downloaded.csv', 'r', newline='') as csvfile:
      with open('output.csv', 'w') as csvwriter:
         writerOutput = csv.writer(csvwriter)
         readerDownloaded = csv.reader(csvfile)
         for row in readerDownloaded:
            ID = row[0]
            FileName = row[1]
            if FileName in filesLst2:
               writerOutput.writerow(row)
	
	with open('downloaded.csv', 'r', newline='') as csvfile:
      with open('output.csv', 'w') as csvwriter:
         writerOutput = csv.writer(csvwriter)
         readerDownloaded = csv.reader(csvfile)
         for row in readerDownloaded:
            ID = row[0]
            FileName = row[1]
            if FileName in filesLst3:
               writerOutput.writerow(row)

main()
#
# for root, dirs, files in os.walk(".", topdown=False):
#   for name in files:
#       print(os.path.join(root, name))
#   for name in dirs:
#       print(os.path.join(root, name))
