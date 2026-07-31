import os
import shutil

# organizing path
FOLDER_PATH = os.getcwd()  # current working directory


# file directory mapping
FILE_TYPES = {
    "Images": [".jpg"],
    "Documents": [".pdf", ".docx"],
    "Videos": [".mp4"],
}

for folder in FILE_TYPES:  # create folders if not exist
    if not os.path.exists(folder):  #os.path.exists(folder) checks if the folder already exists
        os.mkdir(folder) #os.mkdir is used to create a new directory with the specified name
