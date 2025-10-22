import os
import shutil

# a = "/e/Cats/Done"
# b = "A".split("/")


# print("/".join(b[1:]))

# c = "a b"
# c.split()
# print(c)

st = "E:/Cats/LabaPython/python_lab2/tests"
dest = "E:/Cats/LabaPython/python_lab2/test_dir/tests.txt"
shutil.copytree(st, dest)  
