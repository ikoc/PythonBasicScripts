import shutil
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', type=str, required=True,help="Select the main folder which includes files to be zipped")
parser.add_argument('--output_folder', type=str, required=True,help="Select folder which zip files to place")

args = parser.parse_args()

folder_list = os.listdir(args.input_folder)
folder_list.sort()

for folder_name in folder_list:
    zip_path = os.path.join(args.output_folder,folder_name)
    folder_path = os.path.join(args.input_folder,folder_name)
    print("{} will be zipped as {}.".format(folder_path,zip_path))
    shutil.make_archive(zip_path, 'zip', folder_path)