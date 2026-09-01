# file organizer project
import os
import shutil  # shutil is the module perform operations on the data (read, move, etc)

# organizing path
FOLDER_PATH = os.getcwd()  # current working directory


# file directory mapping
FILE_TYPES = {
    # you can add more types of file as based on your requirements
    "Images": [".jpg"],
    "Documents": [".pdf", ".docx"],
    "Videos": [".mp4"],
}

for folder in FILE_TYPES:  # create folders if not exist
    folder_path = os.path.join(FOLDER_PATH , folder) #os.path.join() is used to join one or more path components together
    if not os.path.exists(folder_path):  # os.path.exists(folder) checks if the folder already exists
        os.mkdir(folder_path)  # os.mkdir is used to create a new directory with the specified name

# for file in os.listdir(FOLDER_PATH):
#     if os.path.isdir(file):
#         continue

#     ext = os.path.splitext(file)[1].lower()

#     for folder, extensions in FILE_TYPES.items():
#         if ext in extensions:
#             shutil.move(file, os.path.join(folder, file))
#             break

