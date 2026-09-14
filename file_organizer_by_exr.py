import os, shutil

folder = input("folder path: ")


for filename in os.listdir(folder):
    ext = filename.split(".")[-1]
    dest = f"{folder}/{ext}_files"

    os.makedirs(dest, exist_ok=True)
    shutil.move(f"{folder}/{filename}" f"{dest}/{filename}")

    print("Folder Organized ")
