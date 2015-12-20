from __future__ import division
from ctypes import *
import os
import sys
import timeit
import numpy
from PIL import Image
import shutil


#home_dir=os.path.dirname(os.path.realpath(sys.argv[0])) #**testing** find working script directory 
home_dir="/root/EmmaTests/"

size = 500
path_so = os.path.join(home_dir, 'libyolo.so')
weights_file = c_char_p(os.path.join(home_dir, 'yolo_2000.weights'))
config_file = c_char_p(os.path.join(home_dir, 'yolo2.cfg'))
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
libyolo = pydll.LoadLibrary(path_so)
libyolo.init_yolo(config_file, weights_file)


def handle_one_img(image_path):
            image = Image.open(image_path)
            image = image.convert('RGB')
            np_image_array = numpy.asarray(image, dtype='uint8')
            image_width, image_height= image.size
            image_file = c_char_p(np_image_array.ctypes.data)
            classes_pointer = POINTER(c_int32)()
            libyolo.test_yolo(image_file, image_width, image_height, byref(classes_pointer))
            print str(classes_pointer[0]) + " " + str(classes_pointer[1])


            results = {}
            results['Budweiser'] = classes_pointer[0]
            results['Samsung'] = classes_pointer[1]
            return results

def write_to_file(result, image_path):
            str=image_path
            if result['Budweiser']>0:
                str+=", Budweiser"
            if result['Samsung']>0:
                str+=", Samsung"
            if result['Budweiser']==0 and result['Samsung']==0:
                str+=", Uncategorized"
            with open("test.csv", "a") as file:
                file.writelines(str + "\n")

def handle_folder(images_folder, destination_folder):
    for src_dir, dirs, files in os.walk(images_folder):
        for name in files:
            try:
                image_path=(os.path.join(src_dir,name))
                result=handle_one_img(image_path)
                write_to_file(result, image_path)

                dst_dir = src_dir.replace(images_folder, destination_folder)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)

                dst_file = os.path.join(dst_dir, name)
                print dst_file
                shutil.move(image_path, dst_file)
            except Exception as e:
                print e, name
                pass

def main():
    start = timeit.default_timer()
    images_folder="/root/EmmaTests/Images_Test/"
    destination_folder="/root/EmmaTests/Old_Images/"
    handle_folder(images_folder, destination_folder)

    print "Minutes to execute = ", (timeit.default_timer() - start)/60


if __name__ == '__main__':
    main()
