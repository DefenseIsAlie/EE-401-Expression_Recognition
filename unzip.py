import zipfile
import os




current_dir = os.getcwd()

data_zip = current_dir + "/data.zip"
data_path = current_dir + "/data"


with zipfile.ZipFile(data_zip,"r") as zip:
    zip.extractall(data_path)