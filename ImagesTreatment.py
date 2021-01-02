import os, sys, getopt
import glob
from pprint import pprint
from PIL import Image
from os import path


def determine_ratio(width, height):
    return width/height


def determine_size(calculated_ratio):
    # Landscape image
    if calculated_ratio > 1:
        return 1920, 1080
    # Square image
    elif calculated_ratio == 1:
        return 1000, 1000
    # portrait image
    elif calculated_ratio < 1:
        return 1080, 1920


def main(argv):

    inputFolder = 'Images/*.jpg'
    outputFolder = 'Thumbnail/'
    compressionRate = 50

    try:
      opts, args = getopt.getopt(argv,"h:i:o:c:")
    except getopt.GetoptError:
      print('Usage : python ImagesTreatment.py -i <inputFolder> -o <outputFolder> -c <compressionRate>')
      print('Example : python ImagesTreatment.py -o /Users/SamSepi0l/Documents/outputTest/ -i /Users/SamSepi0l/Documents/Python/ImagesTreatment/Images/ ')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('Usage : python ImagesTreatment.py -i <inputFolder> -o <outputFolder> -c <compressionRate>')
         print('Example : python ImagesTreatment.py -o /Users/SamSepi0l/Documents/outputTest/ -i /Users/SamSepi0l/Documents/Python/ImagesTreatment/Images/ ')
         sys.exit()
      elif opt in ("-i"):

         inputFolder = arg
         intputFolderExist = path.exists(arg)

         if intputFolderExist == False:
             print("Specified input path doesn't exist :( ")
             sys.exit(2)
         else:
             inputFolder = inputFolder + "/*.jpg"
      elif opt in ("-o"):
         outputFolder = arg
         outputFolderExist = path.exists(arg)

         if outputFolderExist == False:
             print("Specified output path doesn't exist :( ")
             sys.exit(2)
      elif opt in ("-c"):
         compressionRate = int(arg)

    images = glob.glob(inputFolder)
    for image in images:
       with open(image, 'rb') as file:
           img = Image.open(file)
           ratio = determine_ratio(img.size[0], img.size[1])

           print('---------------')
           print("Name : " + file.name)
           print("Ratio : " + str(ratio))
           size = determine_size(ratio)
           print("New image dimension : " + str(size))

           try:
               img.thumbnail(size, Image.ANTIALIAS)
               imgName = os.path.basename(file.name)
               img.save(outputFolder + imgName, optimize=True, quality=compressionRate)
           except IOError:
               print("Cannot create thumbnail for '%s'" % file.name)

    print('---------------')
    print("Script finished")


if __name__ == "__main__":
    main(sys.argv[1:])
