import os
import shutil
import datetime
import schedule
import time

src_dir = ""
dest_dir = ""

def copy_folder_to_directory(source, destination):
    today = datetime.date.today()
    dest_dir = os.path.join(destination, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {destination}")

schedule.every().day.at("06:00").do(lambda: copy_folder_to_directory(src_dir, dest_dir))

while True:
    schedule.run_pending()
    time.sleep(60) 