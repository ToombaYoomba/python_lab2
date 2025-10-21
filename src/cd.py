import stat
from datetime import datetime
from os import listdir, scandir, getcwd
import os

current_path = getcwd().replace('\\', '/')
print(f"current path: {current_path}")

data = input().split('/')
# print(data)

# if os.path.exists(current_path.replace('\\', '/')):
#     print("yes")
# else:
#     print("no")

def cd(current_path):

    if data[0] == '.':

        if len(data[1].strip()) == 0 or len(data[1]) == 0:
            print(f"Stay in current directory {current_path}")
            pass

        else:
            new_path = current_path + '/' + '/'.join(data[1:])
            if os.path.exists(new_path):
                current_path = new_path
                print(f"new path: {current_path}")
            
            else:
                print(f"Error bad path ./{'/'.join(data[1:])}")

    elif data[0] == '..':

        new_path = '/'.join(current_path.split('/')[:-1])

        if os.path.exists(new_path):
                current_path = new_path
                print(f"new path back {current_path}")

        else:
            print(f"Error bad path ..")



    elif data[0] == '~':

        current_path = os.path.expanduser("~")
        print(f"new path source {current_path}")


    else:

        directories = [item.name for item in scandir(current_path) if item.is_dir()]
        # print(directories)

        added_path = '/'.join(data)

        # от текущего
        if data[0] in directories:
            new_path = current_path + '/' + '/'.join(data)
            if os.path.exists(new_path):
                current_path = new_path
                print(f"new path from current: {current_path}")
            
            else:
                print(f"Error bad path ./{'/'.join(data[1:])}")

        #абсолютный путь
        elif os.path.exists(added_path):
                current_path = added_path
                print(f"new path absolute: {current_path}")

        else:
            print(f"Error bad path {'/'.join(data)}")

        

cd(current_path)