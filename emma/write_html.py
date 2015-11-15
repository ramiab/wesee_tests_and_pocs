import urllib.request, argparse, os

def get_args():
    parser = argparse.ArgumentParser('This tool copies X files from source-dir to destination-dir.')
    parser.add_argument('-v', action="store_true", default=False, help='Optional. Verbose.')
    parser.add_argument('url_str', help="input comma delimited string of urls")
    parser.add_argument('dest_folder', help="Destination folder")
    args = parser.parse_args()
    return args

def extractHTML(url_list, is_verbose, new_folder):
    if is_verbose:
        print("Creating working directory")
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    else:
        print ("Folder exists")
    os.chdir(new_folder)
    if is_verbose:
        print("Downloading URL source")
    for url in url_list:
       try:
           page = urllib.request.urlopen(url)
           page = page.read()
           with open ("url_file.txt", "wb") as url_file_list:
               url_file_list.write(page)
       except Exception as e:
            print("Wrong URL input: ", e)

def main():
    args = get_args()
    urls_string = args.url_str
    list_of_urls = urls_string.split(';')
    extractHTML(list_of_urls, args.v, args.dest_folder)

if __name__ == '__main__':
   main()
