import csv
import os


def main():
   os.chdir(r"C:\Users\WeSEE 15\Desktop\Python Homework\AVI script try\batch22_27_8_15\test_results\not_Nudity")
   srcDir = os.getcwd()
   filesDir = os.path.join(srcDir ,"Nudity")
   filesLst = os.listdir(filesDir)

   with open('downloaded.csv', 'r', newline='') as csvfile:
      with open('output.csv', 'w') as csvwriter: #--append
         writerOutput = csv.writer(csvwriter)
         readerDownloaded = csv.reader(csvfile)
		 
         for row in readerDownloaded:
            ID = row[0]
            FileName = row[1]
            if FileName in filesLst:
               writerOutput.writerow(row)
			csvwriter.write(filesDir)

main()



# fd = open('document.csv','a')
# fd.write(myCsvRow)
# fd.close()