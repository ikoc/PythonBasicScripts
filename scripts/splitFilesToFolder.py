import os , sys
from shutil import copyfile

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

img_path = sys.argv[1]
out = sys.argv[2]
file_number = 4900

img_list = os.listdir(img_path)
img_list.sort()
folder_id = 0
for count,image_name in enumerate(img_list):
    if count % file_number == 0:
        folder_id += 1
        create_folder(os.path.join(out,str(folder_id)))
    src = os.path.join(img_path,image_name)
    dst = "{}/{}/{}".format(out,folder_id,image_name)
    os.copyfile(src,dst)
