import argparse

__author__ = 'rami'


def get_args():
   parser = argparse.ArgumentParser(description='This tool copies X files from source-dir to destination-dir.')
   parser.add_argument('source_dir', help='From where to copy.')
   parser.add_argument('dest_dir', help='Where to copy to.')
   parser.add_argument('-num_files_to_copy', action='store', dest='num_files_to_copy', default=3,
                       help='Optional. Defaults to 3 files to copy.')
   parser.add_argument('-v', action="store_true", default=False, help='Optional. Verbose.')
   parser.add_argument('-force', action="store_true", default=False, help='Optional. Overwrite files if exist.')

   args = parser.parse_args()

   # args manipulation ...

   return args


def main():
   args = get_args()
   print("args = {}".format(args))

   # calculated_space = calculate_space( args.num_files_to_copy ) # TODO: code this..
   # if args.v:
   #    print("calculated space: ")
   #
   # copy_files( source_dir, dest_dir)  # TODO: code this..

if __name__ == '__main__':
   main()
