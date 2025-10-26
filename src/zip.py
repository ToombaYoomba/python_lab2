import os
import zipfile
from src.check_path import check_path

def zip(current_path, data):

    dir = data[0]
    zip = data[1]

    dir_data = check_path(current_path, dir)
    dir_path = dir_data[1]

    if dir_data[0] in ["c", "rec./", "rec", "abs"]:

        zip_data = check_path(current_path, zip)
        zip_path = zip_data[1]

        zipf = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)

        for root, dirs, files in os.walk(dir_path):
            for file in files:
                zipf.write(os.path.join(root, file))

        zipf.close()

        print(f"Created zip file {zip} from dir {dir}")

    else:
        print("ERROR: dir nor found")