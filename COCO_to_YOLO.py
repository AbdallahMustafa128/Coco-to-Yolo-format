# Code for converting from Coco annotation (json) to yolo format (txt).
# I used it to convert this dataset https://github.com/up2metric/tomatOD to yolo format.
# I edit this code from https://github.com/kozolex/COCO_to_YOLO .

import os
import json
from PIL import Image

# Put both json file and images in one directory 

# Directory for imgs
DIR_IMG_PREFIX = r"C:\Users\Abdallah\Desktop\test\\"
# Directory for json file
ADNOTATION_PREFIX = r"C:\Users\Abdallah\Desktop\test\\"
# Directory for outputs
DIR_OUTPUT_PREFIX = r"C:\Users\Abdallah\Desktop\test\\"

if not os.path.exists(DIR_OUTPUT_PREFIX):
    os.makedirs(DIR_OUTPUT_PREFIX)

# json file
with open(ADNOTATION_PREFIX + "\\tomatOD_test.json") as f:
  data_adnotation = json.load(f)
print(json.dumps(data_adnotation, indent = 4, sort_keys=True))


# Action

# n no of images
n=len(data_adnotation["images"])
# m no of annotations 
m=len(data_adnotation["annotations"])

# n no of images
for data_files in range(n):
    img_filename = data_adnotation["images"][data_files]["file_name"]
    img = Image.open(DIR_IMG_PREFIX + str(img_filename))
    size_x, size_y = img.size
    print('filename: {} resolution(x,y): {},{}'.format(img_filename, size_x, size_y))
    with open(DIR_OUTPUT_PREFIX + os.path.splitext(img_filename)[0] + '.txt', "w") as text_file:
# m no of annotations      
        for annotations in range(m):
            if data_adnotation["images"][data_files]["id"]==data_adnotation["annotations"][annotations]["image_id"]:
                x = data_adnotation["annotations"][annotations]["bbox"][0]
                y = data_adnotation["annotations"][annotations]["bbox"][1]
                width = data_adnotation["annotations"][annotations]["bbox"][2]            
                height = data_adnotation["annotations"][annotations]["bbox"][3]
                x_center = x + int(width/2)
                y_center = y + int(height/2)
                norm_x = x_center/size_x
                norm_y = y_center/size_y
                norm_width = width / size_x
                norm_height = height / size_y
                category_id=(data_adnotation["annotations"][annotations]["category_id"])-1
                print(category_id, norm_x, norm_y, norm_width, norm_height)
                text_file.write('{} {} {} {} {}\n'.format( category_id, norm_x, norm_y, norm_width, norm_height))
                print()