import os
import zipfile
from src.check_path import check_path

def zip(current_path, data):
    dir = data[0]
    zip_name = data[1]

    dir_data = check_path(current_path, dir)
    dir_path = dir_data[1]

    if dir_data[0] in ["c", "rec./", "rec", "abs"]:
        zip_data = check_path(current_path, zip_name)
        zip_path = zip_data[1]

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:

            dir_name = os.path.basename(os.path.normpath(dir_path))
            
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file) #путь файла

                    relative_path = os.path.relpath(file_path, dir_path) #относ. путь от архивируемой директории до файла
                    arcname = os.path.join(dir_name, relative_path) #можно было делать вычитаем из check_path

                    zipf.write(file_path, arcname)

        print(f"Created zip file {zip_name} from dir {dir}")

    else:
        print("ERROR: dir not found")