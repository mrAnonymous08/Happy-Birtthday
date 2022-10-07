import os
import subprocess
os.system("clear")
print("Please wait")
os.system("git clone https://github.com/mrAnonymous08/Happy-Birtthday.git")
os.chdir("./Happy-Birtthday")
os.system("python3 -m pip install -r ./requirements.txt")
print("Download Success")
os.system("python3 ./hbd.py")
