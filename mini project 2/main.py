# file organizer project
import os
import shutil  # shutil is the module perform operations on the data (read, move, etc)

# organizing path
# FOLDER_PATH = os.getcwd() #this is used when the files are having individual folder
FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))  # current working directory


# file directory mapping
FILE_TYPES = {
    # you can add more types of file as based on your requirements
    "Images": [".jpg"],
    "Documents": [".pdf", ".docx"],
    "Videos": [".mp4"],
}

for folder in FILE_TYPES:  # create folders if not exist
    folder_path = os.path.join(
        FOLDER_PATH, folder
    )  # os.path.join() is used to join one or more path components together
    if not os.path.exists(
        folder_path
    ):  # os.path.exists(folder) checks if the folder already exists
        os.mkdir(
            folder_path
        )  # os.mkdir is used to create a new directory with the specified name

# organiziing file
for file in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file)

    # skip folders
    if os.path.isdir(file_path):
        continue

    # get file extensions
    file_ext = os.path.splitext(file)[
        1
    ].lower()  # splittext mein file ka naam aur uski extension dono aa jati h

    for folder, extensions in FILE_TYPES.items():
        if file_ext in extensions:
            # shutil.move(file, os.path.join(folder, file))
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file))
            break

print("FILES ARE ORGANIZED SUCESSFULLY✔️")
