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
 
for file in os.listdir(FOLDER_PATH):
    if os.path.isdir(file):
        continue
 
    ext = os.path.splitext(file)[1].lower()
 
    for folder, extensions in FILE_TYPES.items():
        if ext in extensions:
            shutil.move(file, os.path.join(folder, file))
            break
#run
#output
